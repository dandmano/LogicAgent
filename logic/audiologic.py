from os import sep
from pygame.mixer import Sound

_sound_library = {}
_sound_on = True


#  Funkcja do wlaczania/wylaczania dzwieku
def change_sound_on():
    global _sound_on
    _sound_on = not _sound_on


def get_sound_on():
    return _sound_on


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
