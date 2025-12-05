# import recipes.flavors

# print(recipes.flavors.ginger_chai())



# from recipes.flavors import elaichi_chai, ginger_chai  # named import   # press ctrl + space for suggestions

# print(ginger_chai())


from .recipes.flavors import ginger_chai  # .. the two dots take us to the root directory so can use one dot if they are on the same level 