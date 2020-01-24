
import uuid
import base_handler
import base_interface
from game_server_interface import create_game_server_interface
import constant


def get_gameserver_addresses():
	"""
	Returns a list of strings which are game server addresses in format 'a.b.c.d:p'
	"""
	raise NotImplementedError()  # TODO: implement


def create_gameserver_interface_by_address(address: str):
	return base_interface.decorator(address)(create_game_server_interface())


def response_is_ok(response_dict):
	return 'status' in response_dict and response_dict['status'] == constant.STATUS_OK


class LobbyHandler:
	def __init__(self, public_uuid):
		self.public_uuid = public_uuid

	def echo(self, what_to_echo):
		return {'value': what_to_echo}

	def ping(self):
		return {'uuid': str(self.public_uuid)}

	def find_server(self):
		for addr in get_gameserver_addresses():
			serv = create_gameserver_interface_by_address(addr)
			serv_response = serv.initialize_new_game()
			if response_is_ok(serv_response):
				return serv_response

		return {'status': constant.STATUS_ERROR,
		        'msg': 'servers are busy'}


if __name__ == '__main__':
	base_handler.run(
		LobbyHandler(uuid.uuid4()),
		address=constant.LOBBY_DOMAIN_NAME,
		port=constant.LOBBY_PORT)
