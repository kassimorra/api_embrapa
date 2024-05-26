from webscrapper import Utils
from helpers import hlpCsv

def test_if_download_producao_worked_with_default_values():
    file_name = 'Produção'
    ano = None
    subopt = None
    scrapper_base = Utils.EmbrapaScrapperResponses(file_name, ano, subopt)
    list_output: list[list[str]] = scrapper_base.embrapa_data()
    scrapper_base.save_filename = './arquivos/pytest/20XX_producao.csv'
    assert hlpCsv.write_csv(scrapper_base.save_filename, list_output) == True

def test_if_download_processamento_worked_with_default_values():
    file_name = 'Processamento'
    ano = 1999
    subopt = None
    scrapper_base = Utils.EmbrapaScrapperResponses(file_name, ano, subopt)
    list_output: list[list[str]] = scrapper_base.embrapa_data()
    scrapper_base.save_filename = './arquivos/pytest/1999_processamento.csv'
    assert hlpCsv.write_csv(scrapper_base.save_filename, list_output) == True    

def test_if_download_processamento_with_subopt_03_worked_with_default_values():
    file_name = 'Processamento'
    ano = 2001
    subopt = 'subopt_03'
    scrapper_base = Utils.EmbrapaScrapperResponses(file_name, ano, subopt)
    list_output: list[list[str]] = scrapper_base.embrapa_data()
    scrapper_base.save_filename = './arquivos/pytest/2001_processamento_subopt03.csv'
    assert hlpCsv.write_csv(scrapper_base.save_filename, list_output) == True    