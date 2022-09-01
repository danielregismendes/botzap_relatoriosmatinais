#IMPORTAÇÃO DE PACOTES
from time import sleep
from whatsapp_api import WhatsApp

#INICIA WHATSAPP
wp = WhatsApp()

#AGUARDA O ENTER DO USUÁRIO PRA CONTINUAR
input("Escaneie o QR Code:")

#LISTA DE CONTATOS
ctt_zap = ["Pessoal", "Máquinas","VEM NO SOCO F.C"]

#MENSAGEM A SER ENVIADA
msg = f'Opa {ctt_zap}'

#ENVIA MENSAGENS AOS CONTATOS
for i in range(len(ctt_zap)):
    wp.search_contact(ctt_zap[i])
    wp.send_message(msg)

#ESPERA 10 SEGUNDOS E FECHA JANELA DO CHROME
sleep(10)
wp.driver.close()