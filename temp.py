import textwrap

def list2string(data):
	return ''.join(map(str, data))

# https://en.wikipedia.org/wiki/Hamming(7,4)
zero = '0'

TABLE = {
	"0000": "0000000",
	"1000": "1110000",
	"0100": "1001100", #0011001
	"1100": "0111100", #0011110
	"0010": "0101010", #0101010
	"1010": "1011010", #0101101
	"0110": "1100110", #0110011
	"1110": "0010110", #0110100
	"0001": "1101001", #1001011
	"1001": "0011001", #1001100
	"0101": "0100101", #1010010
	"1101": "1010101", #1010101
	"0011": "1000011", #1100001
	"1011": "0110011", #1100110
	"0111": "0001111", #1111000
	"1111": "1111111" 
}

def Hammingencoder(s, span=4):

	en = []

	if len(s) % span == 0:
		
		data = tuple(textwrap.wrap(s, span))

		for datum in data:
			for origin, code in TABLE.items():
				if origin == datum:
					en.extend(code)	

	else:
		remainder = len(s) % span
		main = s[:-remainder]
		sub = s[-remainder:]
		data = tuple(textwrap.wrap(main, span))
		
		for datum in data:
			for origin, code in TABLE.items():
				if origin == datum:
					#print datum, code
					en.extend(code)

		en.extend(sub)

	return list2string(en)


def Hammingdecoder(s, span=7):

	de = []

	try:
		index_zero = s.index(zero*7)
		amount_zero = s.count(zero*7)
		string = s[index_zero:len(s)]
		strings = tuple(textwrap.wrap(string, span))
		for i in strings:
			if len(i) == span:
				for origin, code in TABLE.items():
	
					if code == i:
						de.extend(origin)
	
			else:
				de.extend(i)
	except ValueError:
		print('Value Error')
		pass 

	return list2string(de)


def Hammingcorrector(s, num=7):

	rst = []
	#p = (0,1,3)
	#d = (2,4,5,6)
	p1 = (0,2,4,6)
	p2 = (1,2,5,6)
	p4 = (3,4,5,6)

	if zero*8 in s:

		begin = s.index(zero*8)+1
		string = s[begin:len(s)]
		strings = tuple(textwrap.wrap(string, num))
		for i in strings:

			if len(i) == num:

				t4 = parity(i, p4)
				t2 = parity(i, p2)
				t1 = parity(i, p1)

			if t4+t2+t1 != zero*3:

				index = (int(t4+t2+t1, 2)) - 1
				sub = [e for e in i]
				if sub[index] == zero:
					sub[index] = 1
				else:
					sub[index] = 0
				rst.extend(sub)

			else:
				rst.extend(i)
	elif zero*num in s:

		begin = s.index(zero*7)
		string = s[begin:len(s)]
		strings = tuple(textwrap.wrap(string, num))

		for i in strings:

			if len(i) == num:

				t4 = parity(i, p4)
				t2 = parity(i, p2)
				t1 = parity(i, p1)

			if t4+t2+t1 != zero*3:
				index = (int(t4+t2+t1, 2)) - 1
				sub = [e for e in i]
				if sub[index] == zero:
					sub[index] = 1
				else:
					sub[index] = 0
				rst.extend(sub)

			else:
				rst.extend(i)
	return list2string(rst)
	#return decodeBaudot(rst)

def parity(s, indicies):
    alist = [s[i] for i in indicies]
    sub = ''.join(alist)
    return str(str.count(sub, '1') % 2) 

def main():
	
	en = Hammingencoder(input())	
	print(en)
	wrong = input()
	crct = Hammingcorrector(wrong)
	de = Hammingdecoder(crct)
	print(de)

if __name__ == '__main__':
	main()