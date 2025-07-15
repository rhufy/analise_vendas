import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('vendas.csv', parse_dates=['data_venda'])
print(df)
#calculando o total de vendas por produto
total_vendas_produto = df.groupby('produto').agg({'quantidade':'sum','total_vendas':'sum'})
print(total_vendas_produto)
#calculo de comissão por total de vendas 
df['comissao']= df['total_vendas'].apply(lambda x : x * 0.05 if x > 20000 else x*0.02)
print(df)
#usando pivot_table para fazer uma tabela usando loja e produto como index 
loja = df.groupby('loja').agg({'total_vendas':['sum','mean','max']})
tabela_loja = pd.pivot_table(df, index=['loja','produto'],values=['quantidade','comissao','total_vendas'],aggfunc='sum')
print(loja)
print(tabela_loja)
#frequência de produto por loja 
frequencia = pd.crosstab(df['produto'],df['loja'])
print(frequencia)

#gráficos de barras 
df.groupby('produto')['total_vendas'].sum().plot(kind='bar')
plt.title('Total de vendas por produto')
plt.xlabel('Produto')
plt.ylabel('Total (R$)')
plt.show()

#gráfico de pizza
df.groupby('produto')['total_vendas'].sum().plot(kind='pie' , autopct='%1.1f%%')
plt.title('Distribuição de vendas')
plt.ylabel('')
plt.show()

#usando idxmax para descobrir a data da maior quantidade de vendas
data_maior_venda = df.loc[df['total_vendas'].idxmax(), 'data_venda']
print(data_maior_venda)
#aqui salva um novo arquivo em csv
df.to_csv('analise_vendas_final.csv', index=False)
#usa o grouphy para organizar  produto por quantidade e sort_values para ordenar  de forma decrescente e pegar o top 3
top_vendidos = df.groupby("produto")['quantidade'].sum().sort_values(ascending=False).head(3)
print(top_vendidos)