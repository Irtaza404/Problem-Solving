if __name__ == '__main__':
    N = int(input())
    data=[]
    for _ in range(N):
        temp=input().split()
        match temp[0]:
            case "insert":data.insert(int(temp[1]),int(temp[2]))
            case "print":print(data)
            case "remove":data.remove(int(temp[1]))
            case "append":data.append(int(temp[1]))
            case "sort":data.sort()
            case "pop":data.pop()
            case "reverse":data.reverse()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna