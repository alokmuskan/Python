def chai_customer():
    print("welcome ! what chai would you like ?")
    order = yield    # waits for the order
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = chai_customer()
next(stall)  # start the generator 

stall.send("Masala chai")    # sends or passes the value/order to method
stall.send("Lemon chai")