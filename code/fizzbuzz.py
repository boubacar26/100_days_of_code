#Write your code below this row 👇

#total = 0

for number in range(1, 101):
    if number % 3 == 0:
        if number % 5 != 0:
            print("Fizz")
        else:
            print("FizzBuzz")
    elif number % 5 == 0:
        if number % 3 != 0:
            print("Buzz")
        else:
            print("FizzBuzz")
    else:
        print(number)
