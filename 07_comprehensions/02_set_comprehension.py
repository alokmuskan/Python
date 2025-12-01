# favourite_chais = [
#     "masala chai", "green tea", "masala chai",
#     "lemon tea", "green tea", "elaichi chai"
# ]

# unique_chai = {chai for chai in favourite_chais}
# print(unique_chai)


recipes = {
    "masala chai": ["ginger", "cardamom", "clove"],
    "elaichi chai": ["cardamom", "milk"],
    "spicy chai": ["ginger", "black pepper", "clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)