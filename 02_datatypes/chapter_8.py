# List are same as array but we call them list in python

ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")  # append adds at the very beginning
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")


# commom way to combine two strings
spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"Chai : {chai_ingredients}")
chai_ingredients.insert(2, "black tea")
print(f"Chai : {chai_ingredients}")


# operator overloading  -> when an operator is used to perform more than one work

base_liquid = ["watre" , "milk"]
extra_flavour = ["ginger"]

full_liquid_mix = base_liquid + extra_flavour
print(f"Liquid mix : {full_liquid_mix}")  # works same as string concatination

strong_brew = ["black tea", "milk"] * 3   # maintains the order and prints three times
print(f"Strong brew : {strong_brew}")