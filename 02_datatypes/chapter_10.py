chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai Order: {chai_order}")


# empty dictionary

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe["base"]}")
del chai_recipe["liquid"]
print(f"Recipe : {chai_recipe}")