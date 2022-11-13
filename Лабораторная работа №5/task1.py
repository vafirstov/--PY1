from pprint import pprint
keys = ['bin', 'dec', 'oct', 'hex']
dicts = [{'bin': bin(i), 'dec': int(i), 'oct': oct(i), 'hex': hex(i)} for i in range(16)]
pprint(dicts)