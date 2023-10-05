def question1():
    n = int(input("Ingrese un numero natural-> "))

    suma1 = 0
    for x in range(n + 1):
        suma1 += x ** 5

    suma2 = 0
    for x in range(n + 1):
        suma2 += x ** 7

    p3 = 2 * ((0.5 * n * (n + 1)) ** 4)

    if suma1 + suma2 == p3:
        print("Se cumple la ecuacion")
    else:
        print("No se cumple la ecuacion")

def question2():
    a = -1
    while a < 0:
        a = int(input("Ingrese a -> "))
        if a < 0:
            print("'a' no debe ser negativo")

    b = -1
    while b < 0 or b < a:
        b = int(input("Ingrese b -> "))
        if b < 0:
            print("'b' no debe ser negativo")
        if b < a:
            print("Error: 'b' debe ser mayor que 'a'")

    print(f"Multiplos de 5 entre {a} y {b}: ", end='')
    multiplos_5 = []
    for i in range(a, b + 1):
        if i % 5 == 0:
            multiplos_5.append(i)

    for i in multiplos_5:
        print(i, end=', ')

    print("\nNumeros entre a y b incluyendo ambos y sus multiplos de 5 con '*': ")
    for i in range(a, b + 1):
        print(i, end=' ')
        if i in multiplos_5:
            print("*", end=' ')
        print()

question1()
question2()



    
    
    

        


