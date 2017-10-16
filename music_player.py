def play(voice, command):
    song = command.replace('!player play ', '')
    player = voice.create_ffmpeg_player('music/%s.mp3' % song)
    return player.start()


def ytplay(voice, command):
    song = command.replace('!player play ', '')
    player = voice.create_ffmpeg_player('music/%s.mp3' % song)
    return player.start()
