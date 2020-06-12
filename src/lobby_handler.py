
import uuid
import base_handler
from base_interface import response_is_ok
from game_server_interface import create_game_server_interface_by_address
import constant
import k8s
import argparse

class LobbyHandler:
	def __init__(self, public_uuid):
		self.public_uuid = public_uuid
		self.k8s = k8s.K8sApi()

	def echo(self, what_to_echo):
		return {'value': what_to_echo}

	def ping(self):
		return {'uuid': str(self.public_uuid)}

	def find_server(self):
		def loop():
			for addr in self.k8s.list_game_servers():
				print(self.k8s.list_game_servers())
				serv = create_game_server_interface_by_address(addr)
				serv_response = serv.initialize_new_game()
				if response_is_ok(serv_response):
					return addr

		addr = loop()
		if addr:
			return {'status': constant.STATUS_OK,
			        'address': addr}
		else:
			# No available servers. Try to create one
			if not self.k8s.create_game_server():
				return {'status': constant.STATUS_ERROR,
				        'msg': 'could not create new server'}

			# Search again
			addr = loop()
			if addr:
				return {'status': constant.STATUS_OK,
				        'address': addr}
			else:
				return {'status': constant.STATUS_ERROR,
				        'msg': 'servers are busy'}

	def add_me_to_server(self, server_public_url):
		for addr in self.k8s.list_game_servers():
			if addr == server_public_url:
				token = str(uuid.uuid4())
				serv = create_game_server_interface_by_address(addr)
				if response_is_ok(serv.add_player_to_game(token)):
					return {'status': constant.STATUS_OK,
					        'token': token}

		return {'status': constant.STATUS_ERROR,
		        'msg': 'bad server_public_url'}

def run(address, port):
	scheme = 'http://'
	url = f'{scheme}{address}:{port}'
	print(f'lobby started on {url}')
	base_handler.run(
		LobbyHandler(uuid.uuid4()),
		address=address,
		port=port)

if __name__ == '__main__':
	PARSER = argparse.ArgumentParser()
	PARSER.add_argument('-a', '--address', help='url domain name to run lobby on', default=constant.LOBBY_DOMAIN_NAME)
	PARSER.add_argument('-p', '--port', type=int, help='port to run lobby on', default=constant.LOBBY_PORT)
	ARGS = PARSER.parse_args()
	run(ARGS.address, ARGS.port)
