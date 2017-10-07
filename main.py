import discord
import asyncio

client = discord.Client()


@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith('!verivetaa'):
        yield from asyncio.sleep(5)
        yield from client.send_message(message.channel, 'Veri vetää itään jos päihteistä pitää!')


if __name__ == '__main__':
    client.run('MzY0NTE1MTIxNzY4MTY5NDky.DLoqtg.HcALlv1bt6p8DYxdInMYC7SA3mI')
