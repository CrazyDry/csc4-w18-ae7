#!/usr/bin/env python3

import operator
import logging
import math
import readline
from retrying import retry

logging.basicConfig(level=logging.DEBUG)


operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'%': operator.mod,	
	'<<': operator.lshift,
	'>>': operator.rshift,
	'&': operator.and_,
	'^^': operator.xor,
	'~': operator.invert,
	'|': operator.or_,
	'!': math.factorial,
}

def calculate(arg):
	stack = list()
	for token in arg.split():
		try:
			value = int(token)
			stack.append(value)
		except ValueError:
			function = operators[token]
			try:
				arg2 = stack.pop()
				arg1 = stack.pop()
				result = function(arg1, arg2)
				stack.append(result)
			except IndexError:
				#arg1 = stack.pop()
				result = function(arg2)
				stack.append(result)
		logging.debug(stack)

	if len(stack) != 1:
		raise TypeError

	return stack.pop()

@retry()
def main():
	while True:
		print(calculate(input('rpn calc> ')))


if __name__ == '__main__':
	main()
