def chai_flavour(flavour="masala"):
    """Return the flavour of chai."""   # this must be at the very first line 
    chai="ginger"
    return flavour


print(chai_flavour.__doc__)
print(chai_flavour.__name__)

help(len)  # another builtin function to which we can pass anything 


def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa 
    :param chai: Number of chai cups (10 rupees each)
    :param samosa: Number of samosa (15 repees each)
    : return: (total amount, thank you message as a string )
    """

    total = chai*10 + samosa*15
    return total, "Thank you for visiting chaicode.com"