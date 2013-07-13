
def mergeArray(A , B):
	print "Hello world!" 
	C = []
	total = len(A) + len(B)
	aIdx = 0
	bIdx = 0
	for k in range(total):
		print k, aIdx, bIdx, C
		if aIdx == len(A):
			C.append(B[bIdx])
		elif bIdx == len(B):
			C.append(A[aIdx])
		else:
			if A[aIdx] < B[bIdx]:
				C.append(A[aIdx])
				aIdx += 1
			else:
				print B[bIdx]
				C.append(B[bIdx])
				bIdx += 1
	return C


listA = [2,4,6,7]
listB = [1,3,5,8]
listC = mergeArray(listA, listB)
print listC
