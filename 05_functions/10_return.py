# def make_chai():
#     #return "Here is your masala chai"
#     print("Here is your masala chai")

# return_value = make_chai()
# print(return_value)

# def idle_chaiwala():
#     pass
# print(idle_chaiwala())


# def sold_cups():
#     return 120
# total = sold_cups()
# print(total)


# def chai_status(cup_left):
#     if cup_left == 0:
#         return "Sorry, chai over"
#     return "chai is ready"
#     print("chai")   # this is not printed anyhow -> which is called early from a function 
# print(chai_status(0))
# print(chai_status(5))


def chai_report():
    return 100, 20

sold, remaining = chai_report()
print("Sold:", sold)
print("remaining:", remaining)


def chai_report():
    return 100, 20 , 10

sold, remaining, _ = chai_report()   # we are probably never using third value 
print("Sold:", sold)
print("remaining:", remaining)