from helpers import hlpDownload, hlpEmbrapa


def test_download_return_expected_sucesso_no_arquivo_producao_csv():
    url = hlpEmbrapa.embrapa_file_list[0][1]
    savePath = hlpEmbrapa.save_path
    fileName = hlpEmbrapa.embrapa_file_list[0][2]

    assert hlpDownload.download(url, savePath, fileName) == f"Sucesso no arquivo - {fileName}"
