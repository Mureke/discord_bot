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
        self.player = music_player.Player(self.voice)

    @asyncio.coroutine
    def on_message(self, message):
        command = message.content
        if message.channel.name == 'general':
            return

        # Music player commands
        if command.startswith('!player'):
            self.player.command = command
            func_name = command.split()[1]
            player_function = getattr(self.player, func_name)
            yield from player_function()

        # Chat commands
        elif command.startswith('!chat'):
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
                return channel
