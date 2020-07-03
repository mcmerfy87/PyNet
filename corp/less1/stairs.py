
import sys

digital_string = sys.argv[1]

n = int(digital_string)
for i in range(1,n+1):
    print(f"{'#'*i:>{n}}")

    


print(type(digital_string))
