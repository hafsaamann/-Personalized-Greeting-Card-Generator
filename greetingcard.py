

import datetime

def create_greeting(name, occasion, message):
    # Construct the greeting message
    greeting = f"Dear {name},\n\nHappy {occasion}!\n\n{message}\n\nBest wishes,\nYour Friend"
    return greeting

def save_greeting(name, greeting):
    # Save the greeting to a text file
    filename = f"{name}_{datetime.datetime.now().strftime('%Y%m%d')}_greeting.txt"
    with open(filename, "w") as file:
        file.write(greeting)
    print(f"Greeting saved to {filename}")

def main():
    print("Welcome to the Personalized Greeting Card Generator!")
    name = input("Enter the recipient's name: ")
    occasion = input("Enter the occasion (e.g., Birthday, Graduation): ")
    message = input("Enter your message: ")

    greeting = create_greeting(name, occasion, message)
    print("\nYour Greeting Card:\n")
    print(greeting)
    
    save_greeting(name, greeting)

if __name__ == "__main__":
    main()
