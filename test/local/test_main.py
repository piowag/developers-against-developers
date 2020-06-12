
import sys
import os
from os import path
from multiprocessing import Process
import time
import tempfile

CUR_DIR = path.dirname(__file__)
SRC_DIR = path.normpath(path.join(CUR_DIR, '../../src'))
sys.path.insert(0, CUR_DIR)  # Fake API will be priotized
sys.path.append(SRC_DIR)

import lobby_interface
import lobby_handler
import k8s
import game_server_handler
import game_server_interface
import base_interface
from base_interface import response_is_ok

import unittest

game_server_procs = []
lobby_proc = None
lobby_address = '0.0.0.0'
lobby_port = 8833
lobby = lobby_interface.create_lobby_interface(f'http://{lobby_address}:{lobby_port}')

def setUpModule():
	global lobby_proc
	global game_server_procs

	lobby_proc = Process(target=lambda: lobby_handler.run(lobby_address, lobby_port))
	lobby_proc.start()

	# wait for lobby to start up
	while True:
		try:
			lobby.ping()
			break
		except Exception as error:
			print(f'waiting for lobby')
			time.sleep(0.1)

def tearDownModule():
	global lobby_proc
	global game_server_procs

	k8s.K8sApi._shutdown_all()
	lobby_proc.terminate()

def _start_new_game():
	available_server = lobby.find_server()
	assert(response_is_ok(available_server))
	print(f'found server: {available_server}')

	url = available_server['address']

	add1 = lobby.add_me_to_server(url)
	assert(response_is_ok(add1))
	add2 = lobby.add_me_to_server(url)
	assert(response_is_ok(add2))

	player1 = add1['token']
	player2 = add2['token']

	server = game_server_interface.create_game_server_interface_by_address(url)
	r = server.get_player_role(player1)
	assert(response_is_ok(r))
	r = server.get_player_role(player2)
	assert(response_is_ok(r))

	r = server.start_game()
	assert(response_is_ok(r))

	return (player1, player2, server, url)

class TestC1(unittest.TestCase):
	def test_lobby_echo(self):
		assert(lobby.echo('test1') == {'value': 'test1'})

	def test_lobby_find_server(self):
		available_server = lobby.find_server()
		assert(response_is_ok(available_server))
		print(f'available_server: {available_server}')

	def test_start_game(self):
		_start_new_game()

	def test_get_role(self):
		(p1, p2, server, url) = _start_new_game()
		assert(server.get_player_role(p1)['role'] == 'gm')
		assert(server.get_player_role(p2)['role'] == 'player')

	def test_get_task(self):
		(p1, p2, server, url) = _start_new_game()
		r = server.get_task()
		assert(response_is_ok(r))
		print(f'task 1 = {r["msg"]}')

	def test_get_answers(self):
		(p1, p2, server, url) = _start_new_game()

		r = server.send_answer(p1, 'echo answ1')
		assert(not(response_is_ok(r))) # p1 is a GM
		r = server.send_answer(p2, 'echo answ2')
		assert(response_is_ok(r))

		r = server.get_answers_from_players(p1)
		assert(response_is_ok(r))
		print(f'get_answers_from_players: {r}')
		r = server.get_answers_from_players(p2)
		assert(not(response_is_ok(r))) # Not a GM

	def test_send_answers(self):
		(p1, p2, server, url) = _start_new_game()

		r = server.send_answer(p2, 'echo 5 > ~/task_two')
		assert(response_is_ok(r))
		r = server.choose_winner(p1, p2)
		assert(response_is_ok(r))

		r = server.get_round_results(p2)
		assert(r['msg'] == 1)

