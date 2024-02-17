number = []
while True:
    user = input("Enter a number or 'done' to finish: ")
    if user == 'done':
        break
    try:
        num = float(user)
        number.append(num)
    except:
        print("invalid input. Please enter a number or 'done'.")
        continue
print(max(number))
print(min(number))
