import requests
from xml.dom import minidom
#PROXIES = {
    #'http': '',
    #'https': '',
#}


def pegar_palavra():
    dicionario_url = "https://api.dicionario-aberto.net/random"
    dicionario_recebido = requests.get(dicionario_url) #proxies=PROXIES)
    palavra = dicionario_recebido.json()["word"]

    dica_url = f"https://api.dicionario-aberto.net/word/{palavra}"
    dica_recebido = requests.get(dica_url) #proxies=PROXIES)
    dicaxml = dica_recebido.json()[0]["xml"]
    dicaparse = minidom.parseString(dicaxml)
    dicamemoria = dicaparse.getElementsByTagName('def')
    for dica in dicamemoria:
        dicastring = dica.firstChild.nodeValue

    return palavra, dicastring

