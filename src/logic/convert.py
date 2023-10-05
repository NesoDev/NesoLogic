from queue import Queue, LifoQueue

# Crear una cola FIFO
cola = Queue()
 # Imprimirá 1

# La cola ahora contiene [2, 3]

# f = 2 * (3 + 2) =  2 3 2 + *

# q(cola) = []
# lq(pila) =[]

# q(cola) = [2]
# lq(pila) = [*]

# q(cola) = [2]
# lq(pila) = [*, (]

# q(cola) = [2, 3]
# lq(pila) = [*, (]

# q(cola) = [2, 3]
# lq(pila) = [*, (, +]

# q(cola) = [2, 3, 2]
# lq(pila) = [*, (, +]


# q(cola) = [2, 3, 2]
# lq(pila) = [*, (, +, )] = [*, +]

# q(cola) = [2, 3, 2, +, *]
# lq(pila) = []

# postfix = 2 3 2 + *

# ----------------------------------

# f = (3 + 2) * 2 

# q(cola) = []
# lq(pila) = []

# q(cola) = []
# lq(pila) =[(]

# q(cola) = [3]
# lq(pila) =[(]

# q(cola) = [3]
# lq(pila) =[(, +]

# q(cola) = [3, 2]
# lq(pila) =[(, +]

# q(cola) = [3, 2]
# lq(pila) =[(, +, )] = [+]

# q(cola) = [3, 2, +]
# lq(pila) =[*]

# q(cola) = [3, 2, +, 2]
# lq(pila) =[*]

# q(cola) = [3, 2, +, 2, *]
# lq(pila) =[]

# postfix = 3 2 + 2 *

# ----------------------------

# f = (1 * (2 + 3)) * 2

# q(cola) = []
# lq(pila) =[]

# q(cola) = []
# lq(pila) =[(]

# q(cola) = [1]
# lq(pila) =[(]

# q(cola) = [1]
# lq(pila) =[(, *]

# q(cola) = [1]
# lq(pila) =[(, *, (]

# q(cola) = [1, 2]
# lq(pila) =[(, *, (]

# q(cola) = [1, 2]
# lq(pila) =[(, *, (, +]

# q(cola) = [1, 2, 3]
# lq(pila) =[(, *, (, +]

# q(cola) = [1, 2, 3]
# lq(pila) =[(, *, (, +, )] = [(, *, +]

# q(cola) = [1, 2, 3]
# lq(pila) =[(, *, +, )] = [*, +]

# q(cola) = [1, 2, 3]
# lq(pila) =[(, *, +, )] = [*, +, *]

# q(cola) = [1, 2, 3]
# lq(pila) =[(, *, +, )] = [*, +]

# q(cola) = [1, 2, 3, +]
# lq(pila) =[*, *]

# q(cola) = [1, 2, 3, +, *]
# lq(pila) =[*]

# q(cola) = [1, 2, 3, +, *, 2]
# lq(pila) =[*]

# q(cola) = [1, 2, 3, +, *, 2, *]
# lq(pila) =[]

# postfix = 1 2 3 + * 2 *

def shunting_yard(f):
    precedens ={
        "(": 1,
        ")": 1,
        "and": 2,
        "or": 2,
        "xor": 2,
        "nor": 2,
        "xnor": 2,
        "nand": 2,
        "not": 3
    }

    def removeSpaces(f):
        return f.replace(" ", "")
    
    def actionParenthesis(stack):
        if "(" in stack and ")" in stack:
            size = len(stack)
            
            
    
    f = removeSpaces(f)

    # we create queae and stack
    queue = Queue()
    stack = LifoQueue()

    for char in f:
        if char.isupper():
            queue.put(char)
        match char:
            case "(":
                actionParenthesis()
 

help(cola)



