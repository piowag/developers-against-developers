
import uuid
import base_handler
import base_interface
from base_interface import response_is_ok
from game_server_interface import create_game_server_interface
import constant
import k8s


def create_gameserver_interface_by_address(address: str):
	return base_interface.decorator(address)(create_game_server_interface())


class LobbyHandler:
	def __init__(self, public_uuid):
		self.public_uuid = public_uuid
		self.k8s = k8s.K8sApi()

	def echo(self, what_to_echo):
		return {'value': what_to_echo}

	def ping(self):
		return {'uuid': str(self.public_uuid)}

	def find_server(self):
		for addr in self.k8s.list_game_servers():
			serv = create_gameserver_interface_by_address(addr)
			serv_response = serv.initialize_new_game()
			if response_is_ok(serv_response):
				return serv_response

		return {'status': constant.STATUS_ERROR,
		        'msg': 'servers are busy'}

	def add_me_to_server(self, server_public_url):
		for addr in self.k8s.list_game_servers():
			if addr == server_public_url:
				token = uuid.uuid4()
				serv = create_gameserver_interface_by_address(addr)
				if response_is_ok(serv.add_player_to_game(token)):
					return {'status': constant.STATUS_OK,
					        'token': token}

		return {'status': constant.STATUS_ERROR,
		        'msg': 'bad server_public_url'}

def run():
	print(f'lobby started')
	base_handler.run(
		LobbyHandler(uuid.uuid4()),
		address=constant.LOBBY_DOMAIN_NAME,
		port=constant.LOBBY_PORT)

if __name__ == '__main__':
	run()
