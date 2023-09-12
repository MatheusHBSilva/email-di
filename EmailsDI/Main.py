import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

destinatarios = [
    '###############'
]

server.login(smtp_username, smtp_password)
#construção dos emails
for destinatario in destinatarios:
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = destinatario
    msg['Subject'] = 'Código de cadastro da criana do D.I. Recon'

    corpo_email = f'Place Holder'
    msg.attach(MIMEText(corpo_email, 'plain'))

    texto_email = msg.as_string()

    server.sendmail(smtp_username, destinatario, texto_email)
    print(f"Email enviado para: {destinatario}")

server.quit()
