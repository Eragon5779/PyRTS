import pip
import subprocess

def check() :
    deps = []
    try :
        import pygame
    except :
        print('PyGame not found! Adding to fetch list...')
        deps.append('pygame')

    if len(deps) > 0 :
        for dep in deps :
            print('Installing {}...'.format(dep))
            subprocess.call(['pip','install', dep])
