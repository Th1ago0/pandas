import pandas as pd

#Limpe o conjunto de dados, convertendo strings em datas ou float, quando necessário.
df = pd.read_csv('Datasets/GDP.csv',decimal='.')
df['gdp_pp'] = df[' GDP_pp '].apply(lambda x: float(x.strip().replace(',','')))
df['Year'] = df['Year'].apply(lambda x: int(x.split('/')[-1]))
del df[' GDP_pp ']
#print(df['Year'])
#print(df['gdp_pp'])

#Você conseguiria informar o primeiro valor registrado de cada país?
df_first_value = df[df['Year'] == df['Year'].min()]
df_first_value.set_index('Country', inplace = True)
#print(df_first_value['gdp_pp'])

#Informe as regiões com maiores crescimentos de PIB per capita no século passado.
df_gdp_start = df[df['Year'] == 1901]
df_gdp_end = df[df['Year'] == 1996]
df_gdp_ev = ((df_gdp_end.groupby('Region')['gdp_pp'].mean() / df_gdp_start.groupby('Region')['gdp_pp'].mean()) * 100).sort_values()
#print(df_gdp_ev)

#Preecha os anos ausentes em cada país com uma estimativa, baseada na diferença entre o próximo registro e o anterior.