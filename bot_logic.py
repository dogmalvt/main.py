import random
import string

def gen_pass(length):
    """
    Gera uma senha aleatória com o tamanho especificado.
    A senha pode conter letras, números e símbolos.
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(length))
    return senha

# main.py
import discord
from bot_logic import gen_pass  # Importa a função gen_pass do outro arquivo

# Define as permissões (intents)
intents = discord.Intents.default()
intents.message_content = True

# Cria o cliente (bot)
client = discord.Client(intents=intents)

# Evento chamado quando o bot se conecta com sucesso
@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

# Evento chamado sempre que uma mensagem é enviada em um canal
@client.event
async def on_message(message):
    # Impede o bot de responder a si mesmo
    if message.author == client.user:
        return

    # Comando: $hello
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")

    # Comando: $bye
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")  # emoji 🙂

    # Comando: $genpass
    elif message.content.startswith('$genpass'):
        # Divide a mensagem por espaços → exemplo: "$genpass 12"
        partes = message.content.split()
        
        # Define o tamanho padrão como 10
        tamanho = 10

        # Se o usuário digitou um número depois, usa esse número
        if len(partes) > 1 and partes[1].isdigit():
            tamanho = int(partes[1])

        # Gera a senha usando a função importada
        senha = gen_pass(tamanho)
        await message.channel.send(f'Sua senha gerada ({tamanho} caracteres): {senha}')

    # Qualquer outra mensagem → o bot repete
    else:
        await message.channel.send(message.content)

# Executa o bot (coloque seu token real aqui)
client.run("SEU TOKEN DO BOT DEVE FICAR AQUI!")