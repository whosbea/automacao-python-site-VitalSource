from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import pandas as pd
import openpyxl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


load_dotenv()

# importar usuario e senha do arquivo env
USUARIO = os.getenv("usuario")
SENHA = os.getenv("senha")
EMAIL = os.getenv("usuarioEmail")
SENHAEMAIL = os.getenv("senhaEmail")
DESTINATARIO = os.getenv("destinatario")

navegador = webdriver.Firefox()
navegador.get("https://analyze.vitalsource.com/auth/vst/login")

# esperar o carregamento
navegador.implicitly_wait(5)
wait = WebDriverWait(navegador, 5)

# iniciar o acesso


def login():
    elemento_email = wait.until(
        EC.visibility_of_element_located(("id", "username")))
    elemento_email.send_keys(USUARIO)

    elemento_senha = wait.until(
        EC.visibility_of_element_located(("id", "password")))
    elemento_senha.send_keys(SENHA)

    botao_login = wait.until(
        EC.visibility_of_element_located(("id", "Sign in")))
    botao_login.click()

# abre a pagina inicial do Vital Source


def abrir_vitalsource():
    navegador.get('https://analyze.vitalsource.com/')
    navegador.implicitly_wait(10)

# faz o download da tabela em CSV


def arquivo_csv():
    abrir_vitalsource()
    botao_download = wait.until(EC.visibility_of_element_located(
        ("CLASS_NAME", ".export-link.export-link-right.trends-export-button")))
    botao_download.click()
# espera o dowload do arquivo .csv
    navegador.implicitly_wait(10)
# obtem a pasta de dowload do windows
    pasta_downloads = os.path.join(os.path.expanduser("~"), "Downloads")

# verificar se o arquivo csv ta na pasta
    caminho_arquivo_csv = None
    for nome_arquivo in os.listdir(pasta_downloads):
        if nome_arquivo.endswith(".csv"):
            caminho_arquivo_csv = os.path.join(pasta_downloads, nome_arquivo)
            break
    if caminho_arquivo_csv:
        df = pd.read_csv(caminho_arquivo_csv)

# caminho do novo arquivo
        caminho_arquivo_excel = os.path.join(
            pasta_downloads, "arquivoVitalSource.xlsx")

# ciar arquivo excel a partir do df
        df.to_excel(caminho_arquivo_excel, index=False)

# carrega o arquivo
        pasta_trabalho_excel = openpyxl.load_workbook(caminho_arquivo_excel)
        planilha = pasta_trabalho_excel.active

# ajustar largura das colunas
        for coluna in planilha.columns:
            tamanho_maximo = 0
            nome_coluna = coluna[0].column_letter
            for celula in coluna:
                try:
                    if len(str(celula.value)) > tamanho_maximo:
                        tamanho_maximo = len(celula.value)
                except:
                    pass
            largura_ajustada = (tamanho_maximo + 2) * 1.2
            planilha.column_dimensions[nome_coluna].width = largura_ajustada

        pasta_trabalho_excel.save(caminho_arquivo_excel)


def enviar_email(caminho_arquivo_excel):
    corpo_email = """
    <p>Segue em anexo o arquivo excel da tabela EXECUTIVE SUMMARY de hoje, do site VitalSource. Se esse email chegou ao senhor quer dizer que meu codigo deu certo!</p>
    """

    msg = MIMEMultipart()
    msg['Subject'] = "Arquivo Excel VitalSource"
    msg['From'] = EMAIL
    msg['To'] = DESTINATARIO

    msg.attach(MIMEText(corpo_email, 'html'))

# anexar o arquivo
    with open(caminho_arquivo_excel, 'rb') as arquivo:
        attachment = MIMEApplication(arquivo.read(), _subtype="xlsx")
        attachment.add_header('Content-Disposition', 'attachment',
                              filename=os.path.basename(caminho_arquivo_excel))
        msg.attach(attachment)

# tentar criar conexão com servidor
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.ehlo()
            server.starttls()
            server.login(EMAIL, SENHAEMAIL)
            server.sendmail(EMAIL, DESTINATARIO, msg.as_string())
        print('Email enviado')
    except Exception as e:
        print(f'Erro ao enviar o email: {e}')


# iniciar o processo
login()
arquivo_csv()
# caminho do arquivo excel
caminho_arquivo_excel = os.path.join(os.path.expanduser("~"), "Downloads", "arquivoVitalSource.xlsx")
enviar_email(caminho_arquivo_excel)

print("terminou")
# fecha o navegador
navegador.quit()
