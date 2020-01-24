
import sys
import os
from os import path
from multiprocessing import Process
import time

CUR_DIR = path.dirname(__file__)
SRC_DIR = path.normpath(path.join(CUR_DIR, '../../src'))
sys.path.insert(0, CUR_DIR)  # Fake API will be priotized
sys.path.append(SRC_DIR)

from lobby_interface import LobbyInterface
import lobby_handler
import k8s
import game_server_handler
import base_interface

import unittest

game_server_procs = []
lobby_proc = None

def setUpModule():
	global lobby_proc
	global game_server_procs

	for addr in k8s.K8sApi().list_game_servers():
		port = int(addr[-4:])
		proc = Process(target=lambda: game_server_handler.run(port))
		proc.start()
		game_server_procs.append(proc)

	time.sleep(1)  # lazy way to wait for servers to start up

	lobby_proc = Process(target=lambda: lobby_handler.run())
	lobby_proc.start()

	# wait for lobby to start up
	while True:
		try:
			LobbyInterface.ping()
			break
		except Exception as error:
			print(f'waiting for lobby')
			time.sleep(0.1)

def tearDownModule():
	global lobby_proc
	global game_server_procs

	for proc in game_server_procs:
			proc.terminate()

	lobby_proc.terminate()

class TestC1(unittest.TestCase):
	def test_lobby_echo(self):
		assert(LobbyInterface.echo('test1') == {'value': 'test1'})

	def test_lobby_find_server(self):
		available_server = LobbyInterface.find_server()
		assert(base_interface.response_is_ok(available_server))
		print(f'found server: {available_server}')

