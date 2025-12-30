# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")


value = 13

if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")



available_size = ["small", "medium", "large"]

if(requested_size := input("Entre your chai cup size: ")) in available_size:
    print(f"Serving {requested_size} chai")
else:
    print(f"Size is unavaiable - {requested_size}")