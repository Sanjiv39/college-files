# Define facts (predicates)
male = {"John", "Bob", "Charlie", "Tom", "Alex"}
female = {"Mary", "Alice", "Diana", "Sara", "Emily"}

# Define parent-child relationships
# (parent, child) tuples
parent = {
("John", "Charlie"),
("Mary", "Charlie"),
("John", "Diana"),
("Mary", "Diana"),
("Bob", "Tom"),
("Alice", "Tom"),
("Charlie", "Alex"),
("Sara", "Alex"),
}

# Define rules for family relations
def father(f, c):
    return (f, c) in parent and f in male

def mother(m, c):
    return (m, c) in parent and m in female

def grandfather(gf, c):
    for p in male:
        if (gf, p) in parent and (p, c) in parent:
            return True
    return False

def grandmother(gm, c):
    for p in female:
        if (gm, p) in parent and (p, c) in parent:
            return True
    return False

def brother(b, s):
    if b in male and s != b:
        for p in parent:
            if p[1] == b and (p[0], s) in parent:
                return True
    return False

def sister(sis, s):
    if sis in female and sis != s:
        for p in parent:
            if p[1] == sis and (p[0], s) in parent:
                return True
    return False

def uncle(u, n):
    for p in parent:
        if brother(u, p[1]) and (p[1], n) in parent:
            return True
    return False

def aunt(a, n):
    for p in parent:
        if sister(a, p[1]) and (p[1], n) in parent:
            return True
    return False

def nephew(n, p):
    return (brother(p, n) or sister(p, n)) and n in male

def niece(n, p):
    return (brother(p, n) or sister(p, n)) and n in female

def cousin(c1, c2):
    for p1 in parent:
        for p2 in parent:
            if p1[1] != p2[1] and brother(p1[0], p2[0]):
                if (p1[1], c1) in parent and (p2[1], c2) in parent:
                    return True
    return False

# Test the rules
print(f"Is John the father of Charlie? {father('John', 'Charlie')}")
print(f"Is Mary the mother of Diana? {mother('Mary', 'Diana')}")
print(f"Is John the grandfather of Alex? {grandfather('John', 'Alex')}")
print(f"Is Alice the grandmother of Tom? {grandmother('Alice', 'Tom')}")
print(f"Is Charlie the brother of Diana? {brother('Charlie', 'Diana')}")
print(f"Is Diana the sister of Charlie? {sister('Diana', 'Charlie')}")
print(f"Is Bob the uncle of Alex? {uncle('Bob', 'Alex')}")
print(f"Is Alice the aunt of Alex? {aunt('Alice', 'Alex')}")
print(f"Is Alex the nephew of Diana? {nephew('Alex', 'Diana')}")
print(f"Is Diana the niece of Bob? {niece('Diana', 'Bob')}")
print(f"Are Charlie and Tom cousins? {cousin('Charlie', 'Tom')}")