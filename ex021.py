# Tocando um mp3
import pygame
from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3') #para a música tocar precisaria de um arquivo com este nome na pasta
mixer.music.play()