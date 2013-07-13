
def mergeArray(A , B):
	print "Hello world!" 
	C = []
	total = len(A) + len(B)
	aIdx = 0
	bIdx = 0
	for k in range(total):
		#print k, aIdx, bIdx, C
		if aIdx == len(A):
			C.append(B[bIdx])
		elif bIdx == len(B):
			C.append(A[aIdx])
		else:
			if A[aIdx] < B[bIdx]:
				C.append(A[aIdx])
				aIdx += 1
			else:
				C.append(B[bIdx])
				bIdx += 1
	return C

def readFile(filename, l):
	# f = open(filename, "r")
	with open(filename, "r") as f:
		for line in f:
			l.append(int(line))
			# print f.readline()

	if f.closed == False:
		f.close()

def main ():
	listA = [2,4,6,7]
	listB = [1,3,5,8]
	listC = mergeArray(listA, listB)
	print listC

# this is just a test
	testInts = []
	readFile("test.txt", testInts)
	print testInts
	print testInts[1:2]

# get the big one
	allInts = []
	readFile("IntegerArray.txt", allInts)
	print allInts[:15]
	print len(allInts)

	return 0

main()
