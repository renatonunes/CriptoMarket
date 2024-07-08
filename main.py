import telebot
from src.funcs import *
from src.gerenciar_usuarios import *
import json

CHAVE_API = "7497081184:AAEFfW-Hni5JIBAgdK8b0DxYJumw0FkXiIo"
apikey_opensea = "1314f8771e824f68a862b50bb2e8bd8c"
bd = "sqlite3.db"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["cadastrar"])
def cadastrar(mensagem):

    if usuario_existe(bd, mensagem.from_user.id):
        bot.send_message(mensagem.chat.id, 'Você já está cadastrado, utilize o BOT.')
    else:
        comando, codigo = mensagem.text.split(' ', 1)
        codigo = codigo.strip('"')
        
        first_name = mensagem.from_user.first_name
        last_name = mensagem.from_user.last_name
        id_telegram = mensagem.from_user.id
        
        if codigo == "123456":
            inserir_usuario(bd, first_name, last_name, id_telegram)
            bot.send_message(mensagem.chat.id, "Cadastrado com Sucesso")
        else:
            bot.send_message(mensagem.chat.id, "Codigo errado")

@bot.message_handler(commands=["start"])
def start(mensagem):
    if usuario_existe(bd, mensagem.from_user.id):
        bot.send_message(mensagem.chat.id, 'Olá, você já está cadastrado, utilize as funções do BOT')
    else:
        bot.send_message(mensagem.chat.id, 'Bem vindo! Cadastre-se utilizando /cadastrar "codigo de convidado"')



@bot.message_handler(commands=["buscarcolecao"])
def buscarcolecao(mensagem):
    comando, colecao = mensagem.text.split(' ', 1)
    colecao = colecao.strip('"')
    collection = get_collection(str(colecao), apikey_opensea)

    nome_collection = collection["nome"]
    colecao_collection = collection["colecao"]
    imagem_collection = collection["imagem"]
    data_criacao_collection = collection["data_criacao"]
    
    
    caption = f"Nome: {nome_collection}\nData de Criação: {data_criacao_collection}\nColeção: {colecao_collection}"


    bot.send_photo(mensagem.chat.id, imagem_collection, caption=caption)
#     retorno_mensagem = f""" {collection}


# """



#     bot.send_message(mensagem.chat.id, retorno_mensagem)
    

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
Escolha uma opção para continuar:
/buscarcolecao "nomecolecao"
"""
    bot.reply_to(mensagem, texto)
    
    
bot.polling()