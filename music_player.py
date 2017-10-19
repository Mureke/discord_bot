import asyncio


class Player:
    def __init__(self, voice):
        self.player_instance = None
        self.command = ''
        self._voice = voice
        self._queue = []
        self.queue_next

    @asyncio.coroutine
    def play(self):
        """
        Plays song from file
        """
        self._player_check()
        song = self.command.replace('!player play ', '')
        self.player_instance = self._voice.create_ffmpeg_player('music/%s.mp3' % song)
        self.player_instance.volume = 0.18
        self.player_instance.start()

    @asyncio.coroutine
    def ytplay(self):
        """
        Plays song with youtube-dl
        """
        self._player_check()
        if 'youtu' in self.command:
            yt_link = self.command.replace('!player ytplay ', '')
        else:
            yt_link = 'https://www.youtube.com/watch?v=%s' % self.command.replace('!player ytplay ', '')

        try:
            self.player_instance = yield from self._voice.create_ytdl_player(yt_link)
            self.player_instance.volume = 0.18
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

    # TODO: Do this somewhere else... or add queue feature... ;)
    def _player_check(self):
        print(self._voice)
        if self.player_instance is not None and self.player_instance.is_playing():
            self.player_instance.stop()

    @asyncio.coroutine
    def queue_add(self):
        print('asdding')
        self._queue.append(self.command)
        print(self._queue)

    @asyncio.coroutine
    def queue_next(self):
        print(self._queue[1])
        yield from asyncio.sleep(5)
        self.queue_next
