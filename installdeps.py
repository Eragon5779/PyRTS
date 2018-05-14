import pip
import subprocess

def install(deps) :
    for dep in deps :
        print('Installing {}...'.format(dep))
        subprocess.call(['pip','install', dep])
