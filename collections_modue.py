import collections 

def show_functions(module):
	result = [ fn for fn in dir(module) if not fn.startswith('__')]
	print(len(result))
	with open('log.txt','w') as f:
		try:
			f.writelines('\t\t' .join(result))
		except Exception as e:
			print(repr(e))



show_functions(collections)




