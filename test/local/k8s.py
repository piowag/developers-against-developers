
import subprocess
import os

TEST_FOLDER = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../tests'))

"""
Fake kubernetes API
"""

class K8sApi:
	def __init__(self):
		print('Fake API created')

	def list_game_servers(self):
		for i in range(10):
			yield 'http://0.0.0.0:47' + str(10 + i)


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

