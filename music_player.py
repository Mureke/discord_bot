import asyncio


class Player:
    def __init__(self, voice):
        self.voice = voice
        self.player_instance = None
        self.command = ''

    @asyncio.coroutine
    def play(self):
        """
        Plays song from file
        """
        self.player_check()
        song = self.command.replace('!player play ', '')
        self.player_instance = self.voice.create_ffmpeg_player('music/%s.mp3' % song)
        self.player_instance.volume = 0.25
        self.player_instance.start()

    @asyncio.coroutine
    def ytplay(self):
        """
        Plays song with youtube-dl
        """
        self.player_check()
        if 'youtube.com' in self.command:
            yt_link = self.command.replace('!player ytplay ', '')
        else:
            yt_link = 'https://www.youtube.com/watch?v=%s' % self.command.replace('!player ytplay ', '')

        try:
            self.player_instance = yield from self.voice.create_ytdl_player(yt_link)
            self.player_instance.volume = 0.25
            self.player_instance.start()
        except Exception as e:
            print(e)

    @asyncio.coroutine
    def stop(self):
        self.player_instance.stop()

    @asyncio.coroutine
    def pause(self):
        self.player_instance.pause()

    @asyncio.coroutine
    def resume(self):
        self.player_instance.resume()

    # TODO: Do this somewhere else... or add queue... ;)
    def player_check(self):
        if self.player_instance is not None and self.player_instance.is_playing():
            self.player_instance.stop()
