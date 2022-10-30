import os
import pygame

_sound_library = {}
_sound_on = True


def change_sound_on():
    global _sound_on
    _sound_on = not _sound_on


def get_sound_on():
    return _sound_on


def play_sound(path):
    if not _sound_on:
        return
    global _sound_library
    sound = _sound_library.get(path)
    if sound is None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        sound = pygame.mixer.Sound(canonicalized_path)
        _sound_library[path] = sound
    sound.play()
