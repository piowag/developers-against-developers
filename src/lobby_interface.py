
import base_interface
import constant

def create_lobby_interface(address: str):
	class LobbyInterface:
		def echo(what_to_echo):
			pass

		def ping():
			pass

		def find_server():
				"""
				Find available game server and return it's public IP
				"""

		def add_me_to_server(server_public_url):
				"""
				Sign new player for a game hosted by server at server_public_url
				Returns new player's token
				"""

	return base_interface.decorator(address)(LobbyInterface)
