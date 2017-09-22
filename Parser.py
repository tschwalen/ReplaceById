# This program takes a text, parses thorugh it, and replaces every
# instance of '{{m.id}}' with whatever is stored for that id in the 
# map. Additional ids can be nested in an id's value, and these are
# recursively parsed. 
#
# TODO:
# Infinite recursion should be terminated at 8 levels

MAX_RECURSION = 8

def __main__():
	inputText = 'For there are many {{m.9781}} to {{m.f912}}'
	
	keyMap = {'9781' : '{{m.1776}} hills', 'f912' : 'climb', '1776' : 'tall'}

	resultText = processText(inputText, keyMap)
	print(resultText)

def processText(input, map):
	output = ""
	pos = 0
	while pos < len(input):

		# if the { is encountered, begin to parse the syntax for 
		# a dict statement
		if input[pos] == "{":
			if input[pos : pos + 4] == '{{m.':
				pos += 4
				key = ""
				while input[pos : pos + 2] != '}}' and pos < len(input):
					key = key + input[pos]
					pos += 1
				if key in map:
					pos += 2
					newString = processText(map[key], map)
					output = output + newString
				else:
					output = output + '{{m.' + key
		else:
			output = output + input[pos]
			pos += 1
	return output

__main__()


