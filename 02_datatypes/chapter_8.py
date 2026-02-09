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