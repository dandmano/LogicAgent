from os import sep

from pygame.mixer import Sound, music

_sound_library = {}
_sound_on = True


#  Funkcja do wlaczania/wylaczania dzwieku
def change_sound_on():
    global _sound_on
    _sound_on = not _sound_on
    if _sound_on:
        play_music()
    else:
        stop_music()


def get_sound_on():
    return _sound_on


def load_backgroundmusic():
    music.load("audio\\background.mp3".replace('\\', sep))
    play_music()


def play_music():
    if not _sound_on:
        return
    music.set_volume(0.1)
    music.play(-1)


def stop_music():
    music.stop()


#  Funkcja otrzymuje sciezke projektowa do pliku dzwiekowego i ja odtwarza
def play_sound(path):
    if not _sound_on:
        return
    global _sound_library
    sound = _sound_library.get(path)
    if sound is None:
        canonicalized_path = path.replace('/', sep).replace('\\', sep)
        sound = Sound(canonicalized_path)
        _sound_library[path] = sound
    sound.play()
