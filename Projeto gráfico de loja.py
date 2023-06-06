import pandas as pd

#Carregar dados do excel
dados = pd.read_excel ("vendas.xlsx")

#Análise exploratória
dados.head()

#listar últimas linhas
dados.tail()

#tamanho da tabela de dados
dados.shape

#tipo de dados
dados.dtypes

#estatísticas
#gerando estatísticas
dados.describe()

#Análise, quantidade de pedidos por loja
dados.loja.value_counts()

#Total de pedidos por tamanho
dados.tamanho.value_counts()
#Podemos ver que o pote de 1000ml não vende muito. Podemos retirar o produto

#Forma de pagamentos-Total de vendas
dados.forma_pagamento.value_counts()
#criar uma campanha para incentivar o uso do pix, gerando menos taxas e evitando compras no cartão

#Faturamento por lojas
dados.groupby("loja").preco.sum()

#Faturamento por loja
dados.groupby("loja").preco.mean()

#Faturamento por estado
dados.groupby("estado").preco.mean()

#Faturamento por estado e cidade
dados.groupby(["estado","cidade"]).preco.sum().to_excel("Faturamento-estado.cidade.xlsx")

#Criar automação desses dados por email
dados.groupby(["estado","cidade"]).preco.mean().to_excel("Média de preços por cidade e estado.xlsx")

import plotly_express as px

#Criando gráficos
grafico = px.histogram(dados, x="estado", y="preco", text_auto=True, color="forma_pagamento")
grafico.show()
grafico.write_html("Gráfico lojas.html")



#Listas(estrutura de dados)
lista_colunas=["loja","cidade","estado","regiao","tamanho","local_consumo"]
for coluna in lista_colunas:
    grafico = px.histogram(dados, x=coluna, y="preco", text_auto=True, color="forma_pagamento")
    grafico.show()
    grafico.write_html(f"Gráfico-{coluna}.html")
for coluna in lista_colunas:
    print(coluna)
agrupado = dados.groupby(['loja', 'ano_mes']).preco.sum().to_frame()
agrupado.reset_index(inplace=True)
agrupado['acumulado'] = agrupado.groupby('loja').preco.cumsum()
fig = px.bar(agrupado,
             x='acumulado',
             y="loja",
             color='loja',
             text_auto=True,
             range_x=[0,123000],
             animation_frame='ano_mes')
fig.show()
fig.write_html("gráfico_animado.html")