import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass, field

@dataclass
class EmbrapaBaseOptions:
    base_url: str = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02"

    base_options: dict = None # field(default_factory=dict)

    def __post_init__(self):
        self.base_options = self.embrapa_nav_options()

    def embrapa_nav_options(self) -> dict:
        page_url = requests.get(self.base_url)
        soup_page = BeautifulSoup(page_url.text, "html.parser")
        all_btn = soup_page.find_all("button", class_="btn_opt")

        options = {btn.text.strip() : btn['value'] for btn in all_btn if btn.text.strip() not in ["Apresentação", "Publicação"]}

        return options
    

