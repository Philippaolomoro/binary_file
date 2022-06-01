import sys


def create_dictionary():
  try:

    dictionary_length = int(input("Enter the dictionary length: "))
    dictionary = {}

    for i in range(dictionary_length):
      key =input("Enter a key: ") 
      value = input("Enter a value: ")
      dictionary[key] = value

    return(dictionary)  
  except ValueError:
    print("You are expected to input a number")
    sys.exit(1)
  except Exception as err:
    print("Something went wrong", repr(err))
    sys.exit(1)