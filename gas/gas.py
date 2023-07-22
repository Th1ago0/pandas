import pandas as pd

df_2000 = pd.read_csv('Datasets/gasolina_2000+.csv',sep=',',low_memory=False)
df_2010 = pd.read_csv('Datasets/gasolina_2010+.csv',sep=',',low_memory=False)

df = pd.concat([df_2000,df_2010])
df['DATA INICIAL'] = pd.to_datetime(df['DATA INICIAL'])
df['DATA FINAL'] = pd.to_datetime(df['DATA FINAL'])
df['MÊS E ANO'] = df['DATA FINAL'].apply(lambda x:'{}'.format(x.year)) + df['DATA FINAL'].apply(lambda x:'/{:02d}'.format(x.month))
common_gas_info = df[df['PRODUTO'] == 'GASOLINA COMUM']
#Qual o preço médio de revenda da gasolina em agosto de 2008?
print(common_gas_info[common_gas_info['MÊS E ANO'] == '2008/05']['PREÇO MÉDIO REVENDA'])

#Qual o preço médio de revenda da gasolina em maio de 2014 em São Paulo?
print(common_gas_info[common_gas_info['MÊS E ANO'] == '2014/05'][common_gas_info['ESTADO'] == 'SAO PAULO']['PREÇO MÉDIO REVENDA'])

#Você conseguiria descobrir em qual(quais) estado(s) a gasolina ultrapassou a barreira dos R$ 5,00? E quando isso ocorreu?
print(common_gas_info[common_gas_info['PREÇO MÉDIO REVENDA'] > 5][['ESTADO','MÊS E ANO']])

#Qual a média de preço dos estados da região sul em 2012?
aux = common_gas_info[common_gas_info['DATA FINAL'].apply(lambda x: x.year) == 2012]
aux = aux[aux['REGIÃO'] == 'SUL']['PREÇO MÉDIO REVENDA'].mean()

