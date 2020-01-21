
from inspect import (
	getmembers,
	getfullargspec,
	)

import json
import requests
import constant

class InterfaceRequestError(Exception):
	def __init__(self, m, base_exception, request):
		message = f'{m} (base_exception: {base_exception}) (request: {request})'
		super().__init__(message)
		self.request = request
		self.base_exception = base_exception

def get_new_method(url, name, spec):
	def new_method(*args, **kwargs):
		arg_count = len(args) + len(kwargs)
		if arg_count != len(spec):
			raise TypeError(f'{name} takes {len(spec)} positional arugments, but {arg_count} was given')

		adict = {}
		for (key, value) in kwargs.items():
			if key in adict:
				raise SyntaxError('keyword argument repeated')
			adict[key] = value

		arglist = list(args)
		for arg in spec:
			if arg not in adict:
				adict[arg] = arglist.pop()

		adict[constant.HTTP_REQUEST_TYPE_ID] = name

		try:
			req = requests.get(url, params=adict)
		except Exception as ex:
			raise InterfaceRequestError('Error during reuqests.get', ex, None)
		try:
			result = json.loads(req.text)
		except Exception as ex:
			raise InterfaceRequestError('Error during json.loads', ex, req)

		return result
	return new_method

def decorator(url):
	'''
	Decorator for classes representing server API
	Rewrites all methods to be just senders
	They return json object that represents server response
	Methods must not have default values or varargs (*args, **kwargs)
	Argument name 'method' is reserved
	'''
	def for_class(self):
		for (name, value) in getmembers(self):
			# skip private methods
			if name.startswith('_'):
				continue
			# get argument list
			spec = getfullargspec(value).args
			# set class function to new one
			setattr(self, name, get_new_method(url, name, spec))
		return self

	return for_class
