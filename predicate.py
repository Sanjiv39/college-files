class Person:
    def __init__(self, name):
        self.name = name

def is_batsman(person):
    # Predicate: Checks if the person is a batsman
    return person.name == "Sachin"

def is_cricketer(person):
    # Predicate: All batsmen are cricketers
    if is_batsman(person):
        return True
    return False
    
# Creating an instance for Sachin
sachin = Person("Sachin")

# Check if Sachin is a cricketer
if is_cricketer(sachin):
    print(f"{sachin.name} is a Cricketer.")
else:
    print(f"{sachin.name} is not a Cricketer.")