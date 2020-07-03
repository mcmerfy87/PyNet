
import sys

digital_string = sys.argv[1]

n = 0
for i in digital_string:
    n += int(i)
    print(i)


print(type(digital_string))
print(f"Sum string is {n}")