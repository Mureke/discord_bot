import discord
import asyncio
import music_player
import chat_commands

class ItaBot(discord.Client):
    def __init__(self):
        super(ItaBot, self).__init__()
        self.voice = None
        self.player = None

    @asyncio.coroutine
    def on_ready(self):
        channel = self.set_active_channel()
        self.voice = yield from self.join_voice_channel(channel)

    @asyncio.coroutine
    def on_message(self, message):
        # Play
        command = message.content
        if command.startswith('!player'):
            player_function = getattr(music_player, message.content.split()[1])
            self.player = player_function(self.voice, command)
        elif command.startswith('!bot'):
            bot_message = chat_commands.find_command(command)
            asyncio.sleep(2)
            yield from self.send_message(message.channel, bot_message)

    def set_active_channel(self):
        """
        Return selected voice channel object

        :return:
            Channel channel
        """

        channels = self.get_all_channels()
        for channel in channels:
            if channel.name == 'Vuosaari':
                print('Joining voice channel %s' % channel.name)
                return channel

    def bot_start(self, client_id):
        """
        Starts bot

        :return:
            None
        """
        self.run(client_id)
