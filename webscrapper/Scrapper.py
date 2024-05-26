from helpers.hlpCsv import write_csv
from webscrapper import Utils

#scrapper for each sub_option if have a suboption

# http://vitibrasil.cnpuv.embrapa.br/index.php?ano=2022&opcao=opt_03&subopcao=subopt_01

def embrapa_save_data(base_scrapper: Utils.EmbrapaScrapperResponses) -> None:
    embrapa_save_single(base_scrapper) if len(base_scrapper.btn_sopt_dict) == 0 else embrapa_save_classification(base_scrapper)

def embrapa_save_single(base_scrapper: Utils.EmbrapaScrapperResponses) -> None:
    list_output: list = base_scrapper.embrapa_data()
    save_name: str = base_scrapper.save_filename
    write_csv(save_name, list_output)

def embrapa_save_classification(base_scrapper: Utils.EmbrapaScrapperResponses) -> None:
    lista_sopt = base_scrapper.btn_sopt_dict.keys()
    save_name: str = base_scrapper.save_filename
    list_output: list = []

    for sopt in lista_sopt:
        remove_header = False if len(list_output) == 0 else True
        base_scrapper_sopt = Utils.EmbrapaScrapperResponses(base_scrapper.file_name, base_scrapper.ano, sopt, remove_header)
        list_output += base_scrapper_sopt.embrapa_data()

    write_csv(save_name, list_output)