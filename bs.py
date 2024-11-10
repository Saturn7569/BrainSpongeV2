import sys

from src.parser import parse_line

if len(sys.argv) != 2:
    print("Invalid run command!")
    sys.exit(1)

code = ""
try:
    with open(sys.argv[1], "r") as f:
        code = "".join(f.readlines())
except FileNotFoundError:
    print(f"'{sys.argv[1]}': no such file or directory")
    sys.exit(1)
except Exception as e:
    print(f"ERROR: '{e}'")
    sys.exit(1)

# print(code)

tok, err, _ = parse_line(code)
if err:
    print(f"{err[0]} ERROR: {err[1]}")
    sys.exit(1)

print(tok)
