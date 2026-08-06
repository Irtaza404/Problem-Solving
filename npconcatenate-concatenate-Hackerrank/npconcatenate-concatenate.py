if __name__ == '__main__':
    student=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
    _,score=zip(*student)
    second=sorted(set(score))[1]
    student.sort(key=lambda x:x[0])
    for name,score in student:
        if score==second:
            print(name) 


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna