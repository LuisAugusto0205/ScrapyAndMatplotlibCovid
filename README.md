# Web Crawling para dados do covid por continente
código feito em python usando scrapy extrair os dados da quantidade de casos, morte e recuperadoos da covid-19 do site  https://www.worldometers.info/coronavirus/#countries​  e plotar um gráfico de barras usando matplotlib


Requirementos
============

* Python 3
* scrapy 2.4.1
* matplotlib 3.3.3

Instalar Requerimentos
=======

Escreva no seu terminal o comando::

    pip install -r requeriments.txt


Extrair dados sobre covid19
=======
 
Vá para pasta raiz onde está a pasta Covid19 e Grafico. 
Escreva no seu terminal o comando::
    
    scrapy crawl worldometers -O Grafico/covid19.json

Isso irá inicializar um spider para extrair os dados do site https://www.worldometers.info/coronavirus/#countries​. 
Os dados seram guardados em formato json no arquivo covid19.json dentro da pasta Grafico.

Criando um gráfico de barras
=======

Para criar um gráfico de barras. vá até a pasta Grafico e execute o seguinte comando no terminal::

    py grafico_barras.py
 
