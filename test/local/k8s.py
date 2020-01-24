
"""
Fake kubernetes API
"""

class K8sApi:
	def __init__(self):
		print('Fake API created')

	def list_game_servers(self):
		for i in range(10):
			yield 'http://0.0.0.0:47' + str(10 + i)

