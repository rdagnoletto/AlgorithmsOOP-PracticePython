

def decompressString(compString, num = 1, decompString = ""):
	open = 0
	close = 0
	start = 0
	end = None
	newnum = None
	for i, c in enumerate(compString):
		if c.isalpha() and open == 0:
			decompString += num*c
		elif c.isdigit():
			if not newnum:
				newnum = int(c)
				start = i +1
		elif c == '[':
			open+=1
		elif c == ']':
			close +=1
			if open == close:
				end = i
				if open == 1:
					decompString += newnum*compString[start+1:end]
				else:
					decompString += newnum*decompressString(compString[start+1:end], num, decompString)
				close, open = 0, 0
				newnum = None

	return decompString










print(decompressString("3[abc]4[ab]c"))
print(decompressString("2[3[a]b]"))
