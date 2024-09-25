# BADA EUROCONTROL

## 1. Apresentação

Este projeto surgiu da necessidade de extrair a Base de Dados de aeronaves do Eurocontrol, disponível em [BADA](https://contentzone.eurocontrol.int/aircraftperformance/default.aspx?), em um arquivo .csv, para que seja utilizado em planilha.
O arquivo .csv gerado tem contém o indicativo ICAO de cada aeronave, bem como todas as 27 caracterísiticas de cada uma.

## 2. Dificuldades encontradas

Por ser uma grande quantidade de informações e, cada página ser associada a um tipo ICAO, creio que o programa não executou corretamente quando inseri todos os 391 tipos diferentes na variável "classe". Para que conseguisse todas as informações, dividi os tipos ICAO em grupos de 50, depois em grupos de 100 aeronaves (arquivo "TIPO ICAO BADA.txt"). Dessas duas maneiras, consegui rodar o código corretamente, extraindo as informações.

## 3. Varávies

O BADA apresenta uma série de variáveis. Segue abaixo a nomenclatura utilizada e a descrição da variável utilizada no arquivo .csv

| Ordem | Nomenclatura | Descrição |
| ----- | ------------ | --------- |
| 01 | ICAO | Tipo da aeronave padrão ICAO |
| 02 | V2IAS | Velocidade de decolagem (em kt) |
| 03 | DistDEPRWY | Distância utilizada para decolagem (em m) |
| 04 | WTC | Categoria de Esteira de Turbulência |
| 05 | RECAT-EU | Categoria peso segundo União Europeia |
| 06 | MTOW | Peso máximo de decolagem (em kg) |
| 07 | VelIAS5000FT | Velocidade Indicada até 5000 ft (em kt) |
| 08 | RazSub5000FT | Razão de subida até 5000 ft (em ft/min) |
| 09 | VelIASFL150 | Velocidade Indicada até nível de voo 150 (em kt) |
| 10 | RazSubFL150 | Razão de subida até nível de voo 150 (ft/min) |
| 11 | VelIASFL240 | Velocidade Indicada até nível de voo 240 (em kt) |
| 12 | RazSubFL240 | Razão de subida até nível de voo 240 (ft/min) |
| 13 | machSubCruz | Velocidade Mach até nível de voo de cruzeiro |
| 14 | RazSubCruz | Razão de subida até nível de voo de cruzeiro (ft/min) |
| 15 | VelTASCruzKT | Velocidade Verdadeira de cruzeiro (em kt) |
| 16 | VelCruzMach | Velocidade Mach em cruzeiro |
| 17 | FLmax | Nível de voo máximo |
| 18 | Range | Alcance (distância) máximo (em NM) |
| 19 | MachDescFL240 | Velocidade Mach de descida até nível de voo 240 |
| 20 | RazDescFL240 | Razão de descida até nível de voo 240 (ft/min) |
| 21 | VelIASDescFL100 | Velocidade Indicada na descida até nível de voo 100 (em kt) |
| 22 | RazDescFL100 | Razão de descida até nível de voo 100 (ft/min) |
| 23 | VelIASARR | Velocidade Indicada no trecho de aproximação (em kt) |
| 24 | RazARR | Razão de descida no trecho de aproximação (ft/min) |
| 25 | MCS | Velocidade mínima em configuração 'limpa" (em kt) |
| 26 | VelIASPouso | Velocidade Indicada utilizada no pouso (em kt) |
| 27 | DistPousoRWY | Distância de pista utilizada para pouso (em m) |
| 28 | APC | Categoria... |

## 5. Como rodar o programa
### 5.1 - Scrapy

Será necessário instalar o scrapy. Pode ser feito utilizando o comando:

`pip install scrapy`
