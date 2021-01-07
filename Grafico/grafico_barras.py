import matplotlib.pyplot as plt
import numpy as np
import json

covid19 = json.loads(open('covid19.json').read())[0]

continentes = [covid19['Continents'][i]['Local'] for i in range(6)]
casos = [covid19['Continents'][i]['cases']/10**6 for i in range(6)]
mortes = [covid19['Continents'][i]['Death']/10**6 for i in range(6)] 
recuperados = [covid19['Continents'][i]['Recovered']/10**6 for i in range(6)] 

largura_barra = 0.25

fig, ax = plt.subplots()

#posição das barras
pos_casos = range(6)
pos_recuperados = [x + largura_barra for x in pos_casos]
pos_mortes = [x + largura_barra for x in pos_recuperados]

barra_casos = ax.bar(x=pos_casos, height=casos, color='blue',
                width=largura_barra, label='casos')

barra_recuperados = ax.bar(x=pos_recuperados, height=recuperados, color='green',
                width=largura_barra, label='recuperados')

barra_mortes = ax.bar(x=pos_mortes, height=mortes, color='red',
                width=largura_barra, label='mortes')


#nome em baixo de cada barra
ax.set_ylabel('casos, recuperação e mortes (em milhões)')
ax.set_title('Número de casos, recuperação e mortes de covid-19 por continente')
ax.set_xlabel('Continentes')
ax.set_xticks([pos + largura_barra for pos in range(6)])
ax.set_xticklabels(continentes)
ax.legend()


def autolabel(rects):
    """coloca o número emcima de cada barra"""
    for rect in rects:
        height = rect.get_height()
        ax.annotate(text='{:.3f}'.format(height),
                    xy=(rect.get_x() + largura_barra / 2, height),
                    xytext=(0, 3),
                    textcoords="offset pixels",
                    ha='center')


autolabel(barra_casos)
autolabel(barra_recuperados)
autolabel(barra_mortes)

#melhoram o layout o gráfico dentro da figura
fig.tight_layout() 

plt.show()




