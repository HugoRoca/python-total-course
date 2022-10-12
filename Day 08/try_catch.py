def suma():
    n1 = int(input("Enter number 1: "))
    n2 = int(input("Enter number 2: "))
    print(n1 + n2)
    print("thanks")

try:
    suma()
except:
    print("algo no ha salido bien")
else:
    print("Hiciste todo bien")
finally:
    print("eso fue todo")

def pedir_numero():
    while True:
        try:
            numero = int(input("Dame un numero"))
        except:
            print("este no es numero")
        else:
            print(f"ingresaste el numero {numero}")
            break

    print("thanks")

pedir_numero()