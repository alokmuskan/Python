snack = input("Enter your preferred snack : ").lower()  # adding this lower() method saves a lot of effort as if the user enters SamOSA then if helps in matching with the given constraints
# print(f"User said : {snack}")
if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! We'll serve you {snack}")
else:
    print(f"Sorry, we only serve cookies or samosa")    