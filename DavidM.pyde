intVar = 3
floatVar = 9.5
comlexVar = (3+5j)
stringVar = "Allah"
booleanVar = True
nonevar = None

if intVar < 3:
    print("warunek jest spelniony")
elif intVar >= 3:
    print("cos innego")
else:
    print("ŻEPA")

def setup():
    pass
def draw():
    rect(20, 50, 10, 80)
    print(mousePressed)
