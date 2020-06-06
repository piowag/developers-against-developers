
import subprocess
from multiprocessing import Process, Queue
import game_server_handler
import constant
import os
import signal

TEST_FOLDER = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../tests'))

"""
Fake kubernetes API
"""

processes = Queue()

class K8sApi:

	def __init__(self):
		print('Fake API created')
		self.servers = []
		self.port_id = 4700

	def list_game_servers(self):
		return self.servers[:]

	def create_game_server(self):
		self.port_id += 1
		scheme = constant.LOBBY_SCHEME
		address = constant.LOBBY_DOMAIN_NAME
		port = self.port_id
		url = f'{scheme}{address}:{port}'
		self.servers.append(url)

		proc = Process(target=lambda: game_server_handler.run(scheme, address, port), args=())
		proc.start()
		processes.put(proc.pid)
		return True

	def _shutdown_all():
		while not processes.empty():
			os.kill(processes.get(), signal.SIGTERM)

	def run_code_and_get_results(self, question_id, code_object):
		results = dict()
		for (token, answer) in code_object.items():
			try:
				cmd = f"{answer}; /usr/bin/env python3 {TEST_FOLDER}/test{question_id}.py"
				print(f'executing "{cmd}"')
				subprocess.run(cmd, check=True, shell=True)
				results[token] = True
			except:
				results[token] = False
		return results

