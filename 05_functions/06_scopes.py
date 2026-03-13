# def serve_chai():
#     chai_type = "Masala"     # local scope -> means the validation of this variable is just inside this function
#     print(f"Chai type is {chai_type}")


# chai_type = "Lemon"
# serve_chai()
# print(f"Outside Function: {chai_type}")



def chai_counter():
    chai_order = "lemon"  #Enclosing scope

    def print_order():
        chai_order = "ginger"
        print("Inner:", chai_order)
    print_order()
    print("Outer:", chai_order)  # if i am at indentation level that means i am outside the function

chai_order = "Tulsi" # Global 
chai_counter()
print("Global:", chai_order)
     