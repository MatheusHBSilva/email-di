import pandas as pd

planilha = 'Cadastro Crianças.xlsx'

df = pd.read_excel(planilha, usecols=['E-mail'])

print(df)