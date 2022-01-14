import telebot

CHAVE_API = '5001884190:AAGXqed2tQu8QbP9a1O1CP19NOgwucCNX6I'

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handlers(commands=['pizza'])
def fazer_pedido_pizza(mensagem):
    """Retorna o parâmetro de enviar a mensagem, quando o comando /pizza for executado
    Para conferir o dicionário que contém as caracterísica da mensagem, execute um print da variável mensagem"
    parâmetro 1: mensagem.chat.id = id do chat
    parâmetro 2: a mensagem que você irá responder"""
    bot.send_message(mensagem.chat.id, "Saindo a pizza para a sua casa: Tempo médio de espera é de 20min")

@bot.message_handlers(commands=['hamburguer'])
def fazer_pedido_hamburguer(mensagem):
    """Retorna o parâmetro de enviar a mensagem, quando o comando /hamburger for executado
    Para conferir o dicionário que contém as caracterísica da mensagem, execute um print da variável mensagem"
    parâmetro 1: mensagem.chat.id = id do chat
    parâmetro 2: a mensagem que você irá responder"""
    bot.send_message(mensagem.chat.id, "Saindo a o BRABOOOOO para a sua casa: Tempo médio de espera é de 35min")

@bot.message_handlers(commands=['salada'])
def fazer_pedido_salada(mensagem):
    """Retorna o parâmetro de enviar a mensagem, quando o comando /salada for executado
    Para conferir o dicionário que contém as caracterísica da mensagem, execute um print da variável mensagem"
    parâmetro 1: mensagem.chat.id = id do chat
    parâmetro 2: a mensagem que você irá responder"""
    bot.send_message(mensagem.chat.id, "Saindo uma saladinha FIT para você: Tempo médio de espera é de 15min")

@bot.message_handlers(commands=['fazer_pedido'])
def fazer_pedido(mensagem):
    """Retorna o parâmetro de enviar a mensagem, quando o comando /fazer_pedido for executado, sendo executado em seguida uma outra resposta com o tempo de espera do produto
    Para conferir o dicionário que contém as caracterísica da mensagem, execute um print da variável mensagem"
    parâmetro 1: mensagem.chat.id = id do chat
    parâmetro 2: a mensagem que você irá responder"""
    texto = """
    Escolha uma das opções abaixo para fazer o pedido:
        /pizza
        /hamburguer
        /salada
        /consultar_precos
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handlers(commands=['reclamar_de_um_pedido'])
def reclamar_de_um_pedido(mensagem):
    """Retorna o parâmetro de enviar a mensagem, quando o comando /reclamar_de_um_pedido for executado
    Para conferir o dicionário que contém as caracterísica da mensagem, execute um print da variável mensagem"
    parâmetro 1: mensagem.chat.id = id do chat
    parâmetro 2: a mensagem que você irá responder"""
    bot.send_message(mensagem.chat.id, 'para enviar uma reclamação, mande um e-mail para ....')

@bot.message_handlers(commands=['mandar_abraco'])
def fazer_pedido(mensagem):
    """Retorna o parâmetro de enviar a mensagem, quando o comando /reclamar_de_um_pedido for executado
    Para conferir o dicionário que contém as caracterísica da mensagem, execute um print da variável mensagem"
    parâmetro 1: mensagem.chat.id = id do chat
    parâmetro 2: a mensagem que você irá responder"""
    bot.send_message(mensagem.chat.id,)


#
def verificar(mensagem):
    """Retorna o parâmetro True, para que seja iniciado a função de resposta"""
    return True

# o modo irá dizer quando a função será executada
# quando a pessoa digitar /ola a função abaixo retornará a função, se caso a function "verificar" seja verdadeiro
@bot.message_handlers(func=verificar)
def responder(mensagem):
    """Retorna o parâmetro para escolher quais das opções o cliente deseja seguir
    Cada opção que retorna como resposta, deverá conter outra função com o que deverá ser executado"""
    texto = """
    Escolha uma opção para continuar:
        /fazer_pedido
        /reclamar_de_um_pedido
        /mandar_abraco
    """
    bot.reply_to(mensagem, texto)


# esse comando irá criar um loop infinito com o bot
# o que irá garantir em que o bot esteja conversando o tempo todo com o telegram
bot.polling()