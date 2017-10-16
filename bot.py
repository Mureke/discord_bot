import discord
import asyncio
import music_loader
import chat_commands


class ItaBot(discord.Client):
    INVALID_CH_MSG = 'Menehä jonnekki muualle huutelemaan täältä'

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
        command = message.content
        if message.channel.name == 'general' and command != self.INVALID_CH_MSG:
            asyncio.sleep(2)
            yield from self.send_message(message.channel, 'Menehä jonnekki muualle huutelemaan täältä')
        # Music player commands
        if command.startswith('!player'):
            func_name = command.split()[1]

            # Play
            if func_name == 'play' or func_name == 'ytplay':
                if self.player is not None and self.player.is_playing():
                    self.player.stop()
                player_function = getattr(music_loader, func_name)
                self.player = yield from player_function(self.voice, command)
                try:
                    self.player.start()
                except AttributeError as attre:
                    print(attre)

            # Start, stop or resume
            else:
                try:
                    allowed_methods = ['stop', 'pause', 'resume']
                    if func_name in allowed_methods:
                        player_function = getattr(self.player, func_name)
                        player_function()
                except Exception as e:
                    print(e)


        # Chat commands
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
