from helpers.download import downloadFiles
import pytest

def test_esperado_path_valor_de_arquivos():
    esperado = "./arquivos/"
    download = downloadFiles()
    assert download.path == esperado

def test_valor_aleatorio_nao_previsto_esperado_exception():
    download = downloadFiles()
    with pytest.raises(Exception):
        download.download("xpto")