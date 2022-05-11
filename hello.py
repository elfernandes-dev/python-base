#!/usr/bin/env python3

""" Olá Usuário Multi Linguas.

Dependendo da lingua configurado no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada, ex:
    export LANG=pt_BR
    
Digite o nome do usuário

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Evandro Fernandes"
__license__ = "Unlicense"

# Este programa imprime um "OLÁ" junto com o nome do usuário, no idioma do sistema
import os
current_language = os.getenv("LANG")[:5]

if current_language == "en_US":
    name = input('Type your name: ').upper()
    msg = f"HELLO, {name}!"
elif current_language == "pt_BR":
    name = input('Digite seu nome: ').upper()
    msg = f"OLÁ, {name}!"
elif current_language == "it_IT":
    name = input('Scrivi il tuo nome: ').upper()
    msg = f"CIAO, {name}!"
elif current_language == "es_SP":
    name = input('Escriba su nombre: ').upper()
    msg = f"HOLA, {name}!"
elif current_language == "fr_FR":
    name = input('Tapez votre nom: ').upper()
    msg = f"BONJOUR, {name}!"


print(msg)











