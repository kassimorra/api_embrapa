# Fase 1 ML Ops FIAP

Este repositório tem como objetivo a realização da primeira fase do Tech Challenge do Curso de MLOps da FIAP. Nesta etapa, faz se necessário realizar o WebScrapping do site da Embrapa.
As informações que estamos buscando são:
- Produção
- Processamento
- Comercialização
- Importação
- Exportação

Este repositório trata-se de um BackEnd API com Python utilizando-se do framework FastAPI.

Existem duas soluções implantadas nesse momento, devido a algumas particularidades do site:
- Solução 1 (Solicitado): WebScrapping do site, podendo escolher o tipo da informação e o ano de extração.
- Solução 2 (Devido a instabilidade do site): Implementado uma solução de download direto dos arquivos do site.

Para testes unitários foi utilizado o PyTest. Com uma cobertura de 89%.

Name                         Stmts   Miss  Cover

helpers\__init__.py              0      0   100%
helpers\hlpCsv.py                8      0   100%
helpers\hlpDownload.py           9      1    89%
helpers\hlpEmbrapa.py           14      5    64%
tests\__init__.py                0      0   100%
tests\test_download.py           6      0   100%
tests\test_embrapafiles.py       0      0   100%
tests\test_helpers.py            0      0   100%
tests\test_hlpCsv.py            26      0   100%
tests\test_scrapper.py           4      2    50%
webscrapper\BaseOptions.py      15      0   100%
webscrapper\Utils.py            63      8    87%
webscrapper\__init__.py          0      0   100%


TOTAL                          145     16    89%


Os arquivos são gerados em csv e salvos em uma pasta padrão (/arquivos) do projeto.

# Desenho da ingestão de dados

![ingestao fase01](./imgs/fase01_ingestao.png)

# O que esperamos no futuro ?

Subir essa parte de ingestão na AWS como uma esteira automatizada 
