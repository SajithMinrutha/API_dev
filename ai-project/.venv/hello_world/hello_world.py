def greet(name):
    return f"Hello {name} Welcome"


if __name__ == "__main__":
    user_name = input("Please enter your name:")
    message = greet(user_name)
    print(message)

    print("counting to 3")
    for i in range (1,4):
        print(i)

    number = 5
    if number > 0:
        print(f"\n{number} is a positive number.")
    else:
        print(f"\n{number} is not a positive number.")