def pure(cups):
    return cups*10

total_chai = 0

def impure(cups):     # not recommended 
    global total_chai
    total_chai += cups


def pour_chai(n):     # recursive function 
    print(n)
    if n==0:
        return "All chai is poured"
    return pour_chai(n-1)
print(pour_chai(3))


chai_types = ["light", "kadak", "ginger", "kadak"]      #anonymous function (lambda)

strong_chai = list(filter(lambda chai: chai="kadak", chai_types))
print(strong_chai)