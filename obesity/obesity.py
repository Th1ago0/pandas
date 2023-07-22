import pandas as pd
import numpy as np

df = pd.read_csv('Datasets/obesity_cleaned.csv', sep=',')
del df['Unnamed: 0']
#Limpe os dados do DataFrame, criando uma coluna de nome 'Obesity' que conterá os valores de obesidade. Transforme em float as colunas que porventura foram importadas como string
df['Obesity'] = df['Obesity (%)'].apply(lambda x: x.split()[0])
df.loc[df['Obesity'] == 'No', 'Obesity'] = np.nan
df['Obesity'].dropna()
df['Obesity'] = df['Obesity'].apply(lambda x: float(x))
df['Year'] = df['Year'].apply(lambda x: int(x))
del df['Obesity (%)']
#Qual o percentual médio de obesidade por sexo no mundo no ano de 2015?
#print(df[df['Year'] == 2015].groupby('Sex')[['Obesity']].mean())

#Quais são os 5 países com a maior e a menor taxa de aumento nos índices de obesidade no período observado?
df_start = df[df['Year'] == 1975]
df_end = df[df['Year'] == 2016]
df_start.set_index('Country',inplace=True)
df_end.set_index('Country',inplace=True)
df_ev = df_end[df_end['Sex'] == 'Both sexes']['Obesity'] - df_start[df_start['Sex'] == 'Both sexes']['Obesity']
#print(df_ev.sort_values().dropna())
#Quais os países com maiores e menores níveis percetuais de obesidade em 2015?
df_max = df[df['Year'] == 2015]
df_min = df[df['Year'] == 2015]
df_max = df_max.max()
df_min = df_min.min()
#print(df_max)
#print(df_min)

#Qual a diferença média percentual de obesidade entre sexos ao longo dos anos para o Brasil?
df_brazil = df[df['Country'] == 'Brazil']
df_brazil.set_index('Year', inplace = True)
df_diference = df_brazil[df_brazil['Sex'] == 'Female']['Obesity'] - df_brazil[df_brazil['Sex'] == 'Male']['Obesity']
print(df_diference)

#Você conseguiria plotar um gráfico mostrando a evolução da obesidade para ambos sexos no mundo?
df_both = df[df['Sex'] == 'Both sexes']
df_both.set_index('Year',inplace = True)
df_both = df_both.groupby('Year')['Obesity'].mean()
#print(df_both)