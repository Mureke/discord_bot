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
    # Play
    if message.content.startswith('!verivetää'):
        try:
            channel = message.author.voice.voice_channel
            voice = yield from client.join_voice_channel(channel)
            player = voice.create_ffmpeg_player('music/veri.mp3')
            yield from client.send_message(message.channel, "Veri vetää itään jos päihteistä pitää!")
            yield from asyncio.sleep(3)
            player.start()
        except Exception as e:
            print(e.message)

    # Disconnect
    if message.content.startswith('!moro'):
        try:
            voice_client = client.voice_client_in(message.server)
            yield from voice_client.disconnect()
        except AttributeError as attr_e:
            print(attr_e.message)


if __name__ == '__main__':
    client.run('MzY0NTE1MTIxNzY4MTY5NDky.DLoqtg.HcALlv1bt6p8DYxdInMYC7SA3mI')
