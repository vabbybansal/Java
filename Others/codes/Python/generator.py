def squareNumbersGen(nums):
    print 'Inside Gen'
    for i in nums:
        print 'Inside Loop1'
        yield i*i

myNumsGen = squareNumbersGen([1,2,3,4,5])

print next(myNumsGen)
print next(myNumsGen)
print next(myNumsGen)
print next(myNumsGen)
print next(myNumsGen)

myNumsGen = squareNumbersGen([1,2,3,4,5])
for num in myNumsGen:
    print num