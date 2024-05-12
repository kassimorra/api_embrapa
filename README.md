# Objetivo
Repositório para criação da API de consulta dados da embrapa - Trabalho pós
Esta API tem como objetivo realizar o download as informações da Embrapa e realizar o tratamento para de forma a viabilizar as análises e exploração dos dados.

# Dados a serem trabalhados

## Produção de Vinho
http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv
## Processamento de vinho
http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv
http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv
http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv
http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv
## Comercialização de vinho
http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv
## Dados sobre importação
http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv
http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv
http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv
http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv
http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv
## Dados sobre exportação
http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv
http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv
http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv
http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv

# Como será feito ?

Este repositório utilizará duas APIs **(Características XPTO)**:

* API Download
o Está API fará o download dos arquivos mencionados acima e os armazenará em um repositório.

* API ETL
o Está API terá a função de realizar o ETL nos dados baixados de forma a estruturar e limpar os arquivos, deixando estes em formato de tabelas prontas para a realização de Analytics. 

# Requisitos

flask3.0.3
pandas2.2.2
requests2.31.0
flask_jwt_extended4.6.0
flask_restx1.3.0

# Próximos passos

- Montar o requirements.txt
- Construir o get para download dos arquivos da embrapa
- Construir o ETL para tratamento dos arquivos
- Montar um analytics simples dos arquivos
- Montar autenticação das apis

- melhoria no tratamento de erro dos downloads