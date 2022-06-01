import base64
import re
import sys

from create_dictionary import create_dictionary


dictionary = create_dictionary()

def serialize():
  try:
    file_name = input("Enter a filename with a dat/bin/txt extension: ")
    extension_regex = "(?i)([^\\s]+(\\.(dat|txt|bin))$)"

    if not file_name:
      raise ValueError

    compiled_regex = re.compile(extension_regex)
    
    if not (re.search(compiled_regex, file_name)):
      file_name = ('{}.dat'.format(file_name))
      file = open(file_name, "wb")
    else:
      file = open(file_name, "wb")

    encoded_dictionary = str(dictionary).encode("ascii")
    binary_form = base64.b64encode(encoded_dictionary)

    file.write(binary_form)
    
    file.close()

  except ValueError:
    print("The file name was empty")
    sys.exit(1)
  except Exception as err:
    print("Something went wrong", repr(err))
    sys.exit(1)


serialize()