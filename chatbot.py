import google.generativeai as genai
from config import api_key
import pyfiglet
import emoji


genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-pro-latest")


def iniciar_chat():
    chat = model.start_chat(history=[])
    ##########################
    ## CHAT
    ##########################
    inicio = 'CHATBOT KVN'

    ascii_art = pyfiglet.figlet_format(inicio)
    print('~=' * 40)
    print(ascii_art)
    print('                         IA GOOGLE - Gemini')
    print('~=' * 40)

    while True:
        user_input = input(emoji.emojize(":robot: Digite sua pergunta (ou 'fim' para sair): "))
        if user_input.lower() == 'fim':
            print('~=' * 40)
            print('Saindo...')
            print(emoji.emojize(':robot: Até mais :)'))
            break

        response = chat.send_message(user_input)
        print(response.text)
