from random import choice

symbols = "aAbBcCdDeEfFgGhHiIkKlLmMnNoOpPrRsStTuUwjJqQvVWxXyYzZ123456789"

while True:
    user_input = input("Enter password length: ")

    if user_input.isdigit():
        passlength = int(user_input)
        
        # Проверяем, чтобы длина была больше нуля
        if passlength <= 0:
            print("The password length must be greater than 0!\n")
            continue

        print("Your Password:  ", end="")
        for i in range(passlength):
            print(choice(symbols), end="")
        print()  # Перенос строки в конце
    else:
        print("Please use only numbers.\n")
    
    ques = input("Continue? (y/n) :")
    if "y" in ques:
        continue
    elif ques == "n":
        break