def get_name():
    while True:
        name = input("Enter your name: ")
        if any(char.isdigit() for char in name):
            print("Invalid input. Name cannot contain numbers.")
        elif name.strip() == "":
            print("Invalid input. Name cannot be blank.")
        else:
            return name

if __name__ == "__main__":
    user_name = get_name()
    print("Hello,", user_name)
  
get_name()

