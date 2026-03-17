# chai = "Ginger chai"

# def prepare_chai(order):
#     print("Preparing ", order)

# prepare_chai(chai)


# chai = [1,2,3]
# def edit_chai(cup):
#     cup[1] = 42

# edit_chai(chai)
# print(chai)


# def make_chai(tea, milk, sugar):
#     print(tea, milk, sugar)
# make_chai("darjeeling", "yes", "sugar") #positional
# make_chai(tea="green", sugar="no", milk="little") #keywords or kargs


# def special_chai(*ingredients, **extras):
#     print("Ingredients", ingredients)
#     print("Extras", extras)
# special_chai("cinnamon","cardmom", sweetener="Honey", foam="yes")

def chai_order(order=[]):
    order.append("Masala")
    print(order)

chai_order()
chai_order()