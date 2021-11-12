# simple script meant to allow to encode and decode URLs.

import urllib.parse as parser
import sys

def main(argv):
      if argv[0] == '-h':
          print("Encode: urlcoder.py -e <string_to_encode>")
          print("Decode: urlcoder.py -d <string_to_decode>")
      elif argv[0] == '-e':
          print("\n" + parser.quote(" ".join(argv[1:])))
      elif argv[0] == '-d':
          print("\n" + parser.unquote(" ".join(argv[1:])))
      else:
          print("Invalid input. Use -h for help.")

if __name__ == "__main__":
    main(sys.argv[1:])
