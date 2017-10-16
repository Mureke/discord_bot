import asyncio

@asyncio.coroutine
def play(voice, command):
    """
    Plays song from file
    :param voice:
    :param command:
    :return: player
    """
    song = command.replace('!player play ', '')
    player = voice.create_ffmpeg_player('music/%s.mp3' % song)
    return player


@asyncio.coroutine
def ytplay(voice, command):
    """
    Plays song with youtube-dl
    :param voice:
    :param command:
    :return: player:
    """

    yt_link = 'https://www.youtube.com/watch?v=%s' % command.replace('!player ytplay ', '')
    try:
        player = yield from voice.create_ytdl_player(yt_link)
        return player
    except Exception as e:
        print(e)
