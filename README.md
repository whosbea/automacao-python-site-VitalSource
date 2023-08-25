
<h1 align="center">
  <br>
<!--   <img src="https://o.remove.bg/downloads/8627e5f8-24fd-4f91-b50f-5edd850290e9/VYUOzavSHKjBxTKAa4LA_cover-removebg-preview.png" alt="Imagem generica python, chrome, selenium" width="300"></a> -->
  <br>
 Automação Python Para o Site Vital Source 
  <br>
</h1>

<h4 align="center">Um projeto webcrawling da faculdade iCev para facilitar a extração de dados do site <a href="https://www.vitalsource.com" target="_blank">VitalSource</a>.</h4>

<div align= "center">
<br>
  <img src="https://www.vitalsource.com/assets/vitalsource-logo-md-c6ec6c03a2315842b4177bb3bd220c13b0851e6f7deda215c6a8b09e1bb4bf7f.png" alt="logo vital souce" width="300"></a>
  <br>
</div>
<p align="center">
  <a href="#objetivo-principal">Objetivo Principal</a> •
  <a href="#bibliotecas">Bibliotecas</a> •
  <a href="#download">Download</a> 
</p>

## Objetivo Principal

A automação deve entrar e logar no site, baixar um arquivo em CSV, formata-lo para uma tabela em Excel e logo após enviar esse arquivo para um email escolhido.

## Bibliotecas

- **Selenium**<br>
>_O Selenium Python é uma biblioteca com diversos métodos que ajudam na automação web. Em suma, as funções permitem controlar o funcionamento de uma página e a interação com ela de forma automática._ - [Documentação](https://www.selenium.dev/pt-br/documentation/overview/)

- **Dontev**<br>
>_O Dotenv é uma biblioteca Python poderosa e fácil de usar para carregar variáveis de ambiente em projetos. Com ele, você pode otimizar as configurações do seu projeto, mantendo informações sensíveis fora do código fonte._ - [Documentação](https://www.npmjs.com/package/dotenv)

- **Os**<br>
>_O módulo OS em Python é uma biblioteca padrão muito útil quando se trata de interagir com o sistema operacional. Ele nos fornece uma série de funcionalidades para executar ações específicas, como navegar por diretórios, criar novos diretórios, executar comandos no terminal e obter informações do sistema._ - [Documentação](https://docs.python.org/pt-br/3/library/os.html)

- **Pandas**
>_Pandas é uma biblioteca para Ciência de Dados de código aberto (open source), construída sobre a linguagem Python, e que providencia uma abordagem rápida e flexível, com estruturas robustas para se trabalhar com dados relacionais (ou rotulados), e tudo isso de maneira simples e intuitiva._ - [Documentação](https://pandas.pydata.org/docs/)

- **Openpyxl**
>_O Openpyxl é uma biblioteca Python de código aberto que permite manipular arquivos do Excel de forma programática. Essa biblioteca oferece diversas vantagens para quem trabalha com planilhas e deseja automatizar tarefas de rotina._ - [Documentação](https://openpyxl.readthedocs.io/en/stable/)

- **Smtplib**
>_O módulo smtplib do Python é basicamente tudo o que precisamos para enviar e-mails simples, sem linha de assunto ou outra informação adicional. Mas, para e-mails reais, precisamos de linhas de assunto e muitas outras informações - talvez até imagens e anexos._ - [Documentação](https://docs.python.org/3/library/smtplib.html)


## Download

Clone esse repositorio e abra o codigo em sua máquina. Antes de rodar certifique-se de criar um arquivo .env na mesma pasta do código com os seguintes dados.

- **Template Arquivo .env:**
```bash
usuario=seuemaildelogin@nosite.com

senha="suasenhaparaentrarnosite"

usuarioEmail=emailquevaienviar@oarquivo.com

senhaEmail="senhadesseemail"

destinatario=emaildo@destinatario.com

```
Alem disso faça a instalação das bibliotecas, digitando os seguintes comandos no terminal.
- **Instalação das bibliotecas**
```bash
pip install selenium
```
```bash
pip install python-dotenv
```
```bash
pip install pandas
```
```bash
pip install openpyxl
```
```bash
pip install secure-smtplib
```
<br>
<i>
<h3 align="center">Find me on</h3>
<p align="center"><a 
href="https://github.com/whosbea" target="_blank"><img alt="Github" 
src="https://img.shields.io/badge/GitHub-%2312100E.svg?&style=for-the-badge&logo=Github&logoColor=white" /></a> <a 
href="https://www.linkedin.com/in/beatriz-barreto-8b0076261/" target="_blank"><img alt="LinkedIn" 
src="https://img.shields.io/badge/linkedin-%2312100E.svg?&style=for-the-badge&logo=linkedin&logoColor=blue" /></a> <a 
href="https://www.instagram.com/whosbea3/" target="_blank"><img alt="Medium" 
src="https://img.shields.io/badge/Instagram-%2312100E?logo=instagram&.svg?&style=for-the-badge&logoColor=white" /></a><br><a 
href="https://discord.gg/h892wggshP" target="_blank"><img alt="StackOverflow" 
src="https://img.shields.io/badge/Discord-%2312100E?logo=discord&.svg?&style=for-the-badge&logoColor=white" /></a> 
</p>


