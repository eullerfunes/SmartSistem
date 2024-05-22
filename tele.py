
import telebot

CHAVE_API = "6887133827:AAFMysSFY8SyK5W-icH1z3f1R_PLTRVApAY"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "A pizza ta igual sua ex, dando pra 8")

@bot.message_handler(commands=["burger"])
def burger(mensagem):
    bot.send_message(mensagem.chat.id, "10 minuto ta pronto, maionese verde da caganeira")

@bot.message_handler(commands=["churrasco"])
def churrasco(mensagem):
    bot.send_message(mensagem.chat.id, "chama o pai pra resenha")

@bot.message_handler(commands=["opcao1"])
def responder(mensagem):
    print(mensagem)
    texto = """
    O que voce quer veinho?
    /pizza - Escolha nossas saborosas pizzas
    /burger - tem uns xinfarto que tem ate pelo de rato
    /churrasco - vai manda a braba pai?
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def responder(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, "É um pena que não conseguimos atender sua expectativa. Descreva melhor sua insatisfação:")

@bot.message_handler(commands=["opcao3"])
def responder(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, "Boa boa meu parceiro")

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
Escolha uma opção para continuar (clique no item):
/opcao1 Fazer um pedido
/opcao2 Reclamar de um pedido
/opcao3 Mandar um salve pro Euller
Responder qualquer outra coisa não vai funcionar, clique em uma das opções citadas 
"""
    bot.reply_to(mensagem, texto)

bot.polling()