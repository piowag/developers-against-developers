
import uuid
import base_handler
import constant


class LobbyHandler:
	def __init__(self, public_uuid):
		self.public_uuid = public_uuid

	def echo(self, what_to_echo):
		return {'value': what_to_echo}

	def ping(self):
		return {'uuid': str(self.public_uuid)}


if __name__ == '__main__':
	base_handler.run(
		LobbyHandler(uuid.uuid4()),
		address=constant.LOBBY_DOMAIN_NAME,
		port=constant.LOBBY_PORT)
