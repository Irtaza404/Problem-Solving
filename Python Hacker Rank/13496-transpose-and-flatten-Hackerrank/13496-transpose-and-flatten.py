import numpy

arr=[]
n,m=list(map(int,input().split()))
for i in range(n):
    arr.append(list(map(int,input().split())))

np=numpy.array(arr)
print(numpy.transpose(np))
print(np.flatten())


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna