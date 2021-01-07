import scrapy

class covidSpider(scrapy.Spider):
    name = 'worldometers'

    start_urls = ['https://www.worldometers.info/coronavirus/#countries']

    def parse(self, response):
        continentes = ['Asia', 'Europe', 'North America', 
                'South America', 'Africa', 'Australia/Oceania']
        
        saida_json = {"Local": "World", "Continents":[]}
        
        casos_mundo = 0
        mortes_mundo = 0 
        recuperados_mundo = 0
        
        for continente in continentes:
            dados = response.css('tr[data-continent="{}"] td'.format(continente))
            
            nome = continente.split('/')[1] if '/' in continente else continente
            total_casos = int(dados[2].css('::text').get().replace(',', ''))
            total_mortes = int(dados[4].css('::text').get().replace(',', ''))
            total_recuperados = int(dados[6].css('::text').get().replace(',', ''))

            saida_json["Continents"].append({
                    "Local": nome,
                    "cases": total_casos,
                    "Death": total_mortes,
                    "Recovered": total_recuperados
                }) 
            casos_mundo += total_casos
            mortes_mundo += total_mortes
            recuperados_mundo += total_recuperados

        saida_json["Cases"] = casos_mundo
        saida_json["Death"] = mortes_mundo
        saida_json["Recovered"] = recuperados_mundo
        return saida_json
            
            
        
        
