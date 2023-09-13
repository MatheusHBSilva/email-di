import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

#obtendo as informações da planilha
#OBS: as listas estão ordenadas em ordem de preenchimento da planilha, eu verifiquei por volta de 20 frase e todos batiam as informações da planilha
planilha = 'Cadastro Crianças.xlsx'
email_dataframe = pd.read_excel(planilha, usecols=['E-mail'])
crianças_dataframe = pd.read_excel(planilha, usecols=['Nome da Criança'])
pulseiras_dataframe = pd.read_excel(planilha, usecols=['Código Pulseira'])
lst_emails = []
lst_nomes = []
lst_pulseiras = []
for val in range(len(email_dataframe)):
    lst_pulseiras.append(pulseiras_dataframe.iat[val,0])
    lst_nomes.append(crianças_dataframe.iat[val,0])
    lst_emails.append(email_dataframe.iat[val, 0])

def gerar_textos(lst_p, lst_n):
    textos = []
    for val in range(len(lst_p)):
        texto = f'Olá responsável por {lst_n[val]}, segue o código de inscrição da criança no Departamento Infantil Recon: {lst_p[val]}'
        textos.append(texto)
    else:
        return textos
txt_ = gerar_textos(lst_pulseiras, lst_nomes)

#parte de servidor
# Configurações do servidor de email
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "#################"
smtp_password = "########" #essa senha tem que ser obtida nas configuraões do goole

# Criando a conexão com o servidor de email
server = smtplib.SMTP(smtp_server, smtp_port)
server.connect(smtp_server, smtp_port)
server.ehlo()
server.starttls()
server.login(smtp_username, smtp_password)

destinatarios = lst_emails

server.login(smtp_username, smtp_password)
#construção dos emails
for val in range(531):
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = destinatarios[val]
    msg['Subject'] = 'Código de cadastro da criana do D.I. Recon'

    corpo_email = txt_[val]
    msg.attach(MIMEText(corpo_email, 'plain'))

    texto_email = msg.as_string()

    server.sendmail(smtp_username, destinatarios[val], texto_email)
    print(f"Email enviado para: {destinatarios[val]}")

server.quit()
