cup = input("Choose your cup size : \n1. Small\n2. Medium\n3. Large\n").lower()

if cup == "small":
    print(f"Price is 10 rupees")
elif cup == "medium":
    print(f"Price is 15 rupees")
elif cup == "large":
    print(f"Price is 20 rupees")
else:
    print(f"Invalid cup size")