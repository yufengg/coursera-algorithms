def sortAndCount(I):
	mid = len(I)//2	 # floor
	#print mid, I

	if len(I) == 1:
		return I,0
	#elif len(I) == 2:
		#A, leftInv = sortAndCount(I[0])
		#B, leftInv = sortAndCount(I[1])
	#else:
	A, leftInv = sortAndCount(I[:mid]) # will be bigger if odd size
	B, rightInv = sortAndCount(I[mid:])

	C, splitInv = mergeAndCountArray(A,B)
	#return A, B, C, leftInv, rightInv, splitInv
	return C, splitInv+leftInv+rightInv

def mergeAndCountArray(A , B):
	C = []
	total = len(A) + len(B)
	aIdx = 0
	bIdx = 0
	invCount = 0
	for k in range(total):
		#print k, aIdx, bIdx, C
		if aIdx == len(A):
			C.append(B[bIdx])
			bIdx += 1
		elif bIdx == len(B):
			C.append(A[aIdx])
			aIdx += 1
		else:
			if A[aIdx] < B[bIdx]:
				C.append(A[aIdx])
				aIdx += 1
			else:
# increment the count of inversions
				invCount += len(A[aIdx:])
				C.append(B[bIdx])
				bIdx += 1
	#print "Merged ",A," with ",B," into ",C
	return C, invCount

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
	listC , invCount = mergeAndCountArray(listA, listB)
	print listC, invCount

	listA = [7,6,5,4]
	listB = [8,5,3,1]
	listX = [8,7,6,5,4,3,2,1]
	C, splitInv = sortAndCount(listX) #listA + listB)
	print C, splitInv 

# this is just a test
	print "this is just a test"
	testInts = []
	readFile("test.txt", testInts)
	print testInts
	print testInts[1:2]

# get the big one
	allInts = []
	readFile("IntegerArray.txt", allInts)
	print allInts[:15]
	print len(allInts)

	print "Starting big sort..."
	C, allInv = sortAndCount(allInts)
	print allInv
	C, allInv = sortAndCount(C)

	return 0

main()
