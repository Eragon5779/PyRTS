import installdeps

def check() :
	deps = []
	try :
		import pygame
	except :
		print('PyGame not found! Adding to fetch list...')
		deps.append('pygame')
	if len(deps) > 0 :
		installdeps.install(deps)
