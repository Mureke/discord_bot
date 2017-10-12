import discord
import asyncio


class ItaBot(discord.Client):
    def __init__(self):
        super(ItaBot, self).__init__()
        self.client_id = 'MzY0NTE1MTIxNzY4MTY5NDky.DLoqtg.HcALlv1bt6p8DYxdInMYC7SA3mI'
        self.voice = None

    @asyncio.coroutine
    def on_ready(self):
        channel = self.set_active_channel()
        self.voice = yield from self.join_voice_channel(channel)

    @asyncio.coroutine
    def on_message(self, message):
        # Play
        player = self.voice.create_ffmpeg_player('music/veri.mp3')
        if message.content.startswith('!verivetää'):
            try:
                player.start()
            except Exception as e:
                print(e.message)

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

    def bot_start(self):
        """
        Starts bot

        :return:
            None
        """
        self.run(self.client_id)
