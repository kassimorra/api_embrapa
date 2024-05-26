from fastapi import Response
import requests
from bs4 import BeautifulSoup
import re
from unidecode import unidecode
from dataclasses import dataclass
from webscrapper import BaseOptions

embrapa_base_options = BaseOptions.EmbrapaBaseOptions()

def embrapa_get_link(file_name: str, ano: int, suboption: str) -> str:
    base_link = "http://vitibrasil.cnpuv.embrapa.br/index.php?"
    output_link = base_link + f'opcao={embrapa_base_options.base_options[file_name]}' 
    if ano != None:
        output_link += f'&ano={str(ano)}'
    if suboption != None: 
        output_link += f'&subopcao={suboption}'
    return output_link

@dataclass
class EmbrapaScrapperResponses:
    file_name: str
    ano: int = None
    suboption: str = None
    remove_header: bool = None

    save_path: str = "./arquivos/scrapper/"       

    def __post_init__(self):
        self.getLink = embrapa_get_link(self.file_name, self.ano, self.suboption)
        self.page_url: Response = requests.get(self.getLink)
        self.soup_page: BeautifulSoup = BeautifulSoup(self.page_url.text, "html.parser")
        self.page_label = self.soup_page.find(class_="lbl_pesq")
        self.text_page = self.soup_page.find(class_="content_center").find(class_="text_center").text

        self.table = self.soup_page.find(class_='tb_base tb_dados')
        self.table_head = self.table.find('thead').find_all('th')
        self.table_rows = self.table.find_all('td')
        self.table_foot = self.table.find('tfoot').find_all('td')
        self.table_header = self.soup_page.find(class_='tb_base tb_header no_print')

        self.btn_sopt = self.table_header.find_all(class_='btn_sopt')
        self.btn_sopt_dict: dict = {subsopt['value'] : subsopt.text.strip() for subsopt in self.btn_sopt}
        self.year_page: int = self.embrapa_current_year()
        self.save_filename = self.embrapa_get_save_filename()

    def embrapa_get_save_filename(self) -> str:
        fileformat = ".csv"
        return self.save_path + str(self.year_page) + "_" + unidecode(self.file_name.lower()) + fileformat

    def verify_date(self) -> bool:
        valid = True
        if self.ano != None:
            if self.ano < self.embrapa_get_hist_range()[0]: valid = False
            if self.ano > self.embrapa_get_hist_range()[1]: valid = False
        return valid

    def embrapa_get_hist_range(self) -> list:
        years = re.findall(r'\b\d{4}\b', self.page_label.text)
        years = [int(year) for year in years]
        return years

    def embrapa_current_year(self) -> int:
        year = int(re.search(r'\b\d{4}\b', self.text_page).group())
        return year
    
    def embrapa_data(self) -> list[list[str]]:
        list_output: list[list[str]] = []

        if self.remove_header != True:
            list_output.append(
                ['ano'] +
                ['tipo_item'] + 
                ['classificação'] + 
                [header.text.strip() for header in self.table_head]
            )

        for i in range(0, len(self.table_rows), 2):
            list_output.append([
                self.year_page,
                'subtotal' if self.table_rows[i].get('class', [''])[0] == 'tb_item' else 'item',
                self.btn_sopt_dict[self.suboption] if self.suboption else None, 
                self.table_rows[i].text.strip(), 
                self.table_rows[i + 1].text.strip()
            ])

        list_output.append([self.year_page, 'total', self.btn_sopt_dict[self.suboption] if self.suboption else None, self.table_foot[0].text.strip(), self.table_foot[1].text.strip()])

        list_id_output = [['id'] + list_output[0]] + [[index] + sublist for index, sublist in enumerate(list_output[1:], start=1)]

        return list_id_output