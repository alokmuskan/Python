def pure(cups):
    return cups*10

total_chai = 0

def impure(cups):     # not recommended 
    global total_chai
    total_chai += cups