import base64
import ast
import sys


def deserialize():
  try:
    file_name = input("Please put in the file you want to read: ")
    file = open(file_name, "rb")
    binary_string = file.read()

    binary_decode = base64.b64decode(binary_string)
    decoded_string = binary_decode.decode("ascii")
    dictionary = ast.literal_eval(decoded_string)

    print(dictionary)

    file.close()
  except FileNotFoundError:
    print(f"This file with name-{file_name} cannot be found. Aborting!!!")
    sys.exit(1)
  except UnicodeDecodeError:
    print(f"The file with name-{file_name} contains a wrong format")
    sys.exit(1)
  except Exception as err:
    print(f"Something went wrong while trying to open {file_name}", repr(err))
    sys.exit(1)


deserialize()