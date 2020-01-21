
import json

from http.server import (
	BaseHTTPRequestHandler,
	HTTPServer,
	)

from http import (
	HTTPStatus,
	)

from urllib.parse import (
	urlsplit,
	parse_qs,
	)

from constant import (
	HTTP_REQUEST_TYPE_ID,
	)

def unlist_arguments(query):
	for (k, value) in query.items():
		if isinstance(value, list):
			if len(value) == 1:
				query[k] = value[0]
			else:
				raise Exception('Bad format')

class BaseHandler(BaseHTTPRequestHandler):
	# this name is enforced by BaseHandler
	# pylint: disable=C0103
	def do_GET(self):
		if self.server.handler_obj is None:
			self.send_error(HTTPStatus.INTERNAL_SERVER_ERROR, 'Server not initialized')
			return

		try:
			try:
				query = parse_qs(urlsplit(self.path).query)
				unlist_arguments(query)
			except Exception as ex:
				self.log_error(f'Error during request parsing: {ex}')
				raise
		except:
			self.send_error(HTTPStatus.BAD_REQUEST, 'Could not parse the request')
			return

		if HTTP_REQUEST_TYPE_ID not in query:
			self.send_error(HTTPStatus.BAD_REQUEST, f'Expected "{HTTP_REQUEST_TYPE_ID}" field')
			return

		method_name = query[HTTP_REQUEST_TYPE_ID]
		if method_name.startswith('_'):
			self.send_error(HTTPStatus.BAD_REQUEST, f'Method named "{method_name}" does not exist')
			return

		try:
			method = getattr(self.server.handler_obj, method_name)
		except:
			self.send_error(HTTPStatus.BAD_REQUEST, f'Method named "{method_name}" does not exist')
			return

		try:
			try:
				copy = query.copy()
				del copy[HTTP_REQUEST_TYPE_ID]
				result = method(**copy)
			except Exception as ex:
				self.log_error(f'Method "{method_name}" failed with {ex}')
				raise
		except:
			self.send_error(HTTPStatus.INTERNAL_SERVER_ERROR, 'Execution failed')
			return

		try:
			try:
				text = json.dumps(result)
			except Exception as ex:
				self.log_error(f'json serialization failed: {ex}')
				raise
		except:
			self.send_error(HTTPStatus.INTERNAL_SERVER_ERROR,
							f'Method "{method_name}" did not return proper json')
			return

		encoded = text.encode(encoding='utf-8')

		self.send_response(HTTPStatus.OK)
		self.send_header("Content-type", "application/json")
		self.send_header("Content-Length", str(len(encoded)))
		self.end_headers()

		self.wfile.write(encoded)


def run(handler_obj, address='', port=8000):
	httpd = HTTPServer((address, port), BaseHandler)
	httpd.handler_obj = handler_obj
	httpd.serve_forever()
