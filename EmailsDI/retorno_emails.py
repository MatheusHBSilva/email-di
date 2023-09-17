#aqui foi feito o teste do código que foi aplicadono arquivo 'main.py'
#a primeira criança está sem nome na planilha, por isso que fica como 'nan'
import pandas as pd

planilha = 'Cadastro Crianças.xlsx'

#tranforma em dataframe as colunas de email, nome da criança e pulseira
email_framework = pd.read_excel(planilha)
crianças_framework = pd.read_excel(planilha, usecols=['Nome da Criança'])
pulseiras_dataframe = pd.read_excel(planilha, usecols=['Código Pulseira'])

print(email_framework)

'''
#cria listas vazias para comportar os dataframes
lst_emails = []
lst_nomes = []
lst_pulseiras = []

#tranforma os data frames em listas
for val in range(len(email_framework)):
    lst_pulseiras.append(pulseiras_dataframe.iat[val,0])
    lst_nomes.append(crianças_framework.iat[val,0])
    lst_emails.append(email_framework.iat[val, 0])

#gera os textos individuais para cada criança
def gerar_textos(lst_p, lst_n, lst_e):
    textos = []
    for val in range(len(lst_p)):
        texto = f'Olá responsável por {lst_n[val]}, segue o código de inscrição da criança no Departamento Infantil Recon: {lst_p[val]}'
        textos.append(texto)
    else:
        return textos

txt_ = gerar_textos(lst_pulseiras, lst_nomes, lst_emails)

print(txt_)
'''
