
import json
import traceback

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
				splited = urlsplit(self.path)
				method_name = splited.path
				if method_name.startswith('/'):
					method_name = method_name[1:]

				query = parse_qs(splited.query)
				unlist_arguments(query)
			except Exception as ex:
				self.log_error(f'Error during request parsing: {ex}')
				raise
		except:
			self.send_error(HTTPStatus.BAD_REQUEST, 'Could not parse the request')
			return

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
				result = method(**query)
			except Exception as ex:
				self.log_error(f'Method "{method_name}" failed with {ex}')
				tr = ''.join(traceback.format_exception(etype=type(ex), value=ex, tb=ex.__traceback__))
				self.send_error(HTTPStatus.INTERNAL_SERVER_ERROR, f'Execution failed with: {ex}; trace: {tr}')
				raise
		except:
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
