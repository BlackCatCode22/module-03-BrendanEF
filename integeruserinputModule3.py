total = 0
count = 0
while True:
    user = input("Enter an integer or 'done' to finish: ")
    if user == 'done':
        break
    try:
        number = int(user)
        total = total + number
        count = count + 1
    except:
        print("Invalid input. Please enter an integer or 'done'.")
        continue
average = total / count
print(total)
print(count)
print(average)