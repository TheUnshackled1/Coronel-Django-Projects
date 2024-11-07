def calculator():
    print("WELCOME TO MY CALCULATOR👋🙋‍♂️")
    print("Enter 'exit' if you want to quit! 😊")
    while True:
        operator = ['add', 'subtract','multiply', 'divide']
        operation = input(f"Enter your operator{operator}:\t").lower()
        if operation == 'exit':
            print('Thank you for using my Calculator🥰🥰🥰')
            break
        if operation not in operator:
            print("Invalid Operator🚫🚫🚫⚠️⚠️⚠️ \n Try Again!!🥰🥰")
            continue
        try:
            num1 = int(input("Enter Your 1st Number:\t"))
            num2 = int(input("Enter Your 2nd Number:\t"))
        except ValueError:
            print("Error! pleas try again⚠️⚠️⚠️⚠️")
            continue
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                print("Cannot be divded by zero🚫🚫🚫")
                continue
            result = num1 / num2
        print(f"The result of {num1} {operation} by {num2} is", result , "🎉🎉🍾🍾🍾")
        
calculator() 


