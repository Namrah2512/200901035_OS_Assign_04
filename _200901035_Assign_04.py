import threading
import time
userInput_string = ""

def funcInput():
    global userInput_string
    try:
        userInput_string = input("Enter your desired string: ")
    except ValueError:
        userInput_string = ""
        print("Can't process on an empty string.")
        userInput_string = input("Enter a valied string: ")

def funcReverse():
    global userInput_string
    reverse_output = userInput_string[::-1]
    print("\nReversed output: ", reverse_output)

def funcCapitalize():
    global userInput_string
    capital = userInput_string.upper()
    print("\nCapitalized output: ", capital)

def funcShift():
    global userInput_string
    shifted_string = ""
    for character in userInput_string:
        if character == " ":
            shifted_string += " "
        else:
            shifted_string += chr(ord(character) + 2)
    print("\nString after shifts: ", shifted_string)

if __name__ == "__main__":
    Input_Thread = threading.Thread(target=funcInput)
    Input_Thread.start()
    Input_Thread.join()
    Reverse_Thread = threading.Thread(target=funcReverse)
    Capital_Thread = threading.Thread(target=funcCapitalize)
    Shift_Thread = threading.Thread(target=funcShift)
    Reverse_Thread.start()
    Reverse_Thread.join()
    Capital_Thread.start()
    Capital_Thread.join()
    Shift_Thread.start()
    Shift_Thread.join()