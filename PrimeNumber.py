number = int(input("Enter the number to check"))
count = 1
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            count += 1
if count == 1:
    print(number, "Is Prime")
else:
    print(number, "Is Not Prime")
