def main():
    # Escribe el código adecuado para completar el programa
    l1 = int(input("Ingresa la medida del lado 1: "))
    l2 = int(input("Ingresa la medida del lado 2: "))
    l3 = int(input("Ingresa la medida del lado 3: "))

    if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
        if l1==l2 and l2==l3:
            print("ES UN TRIANGULO EQUILATERO")
        elif l1==l2 or l1==l3 or l2==l3:
            print("ES UN TRIANGULO ISOSCELES")
        else:
            print("ES UN TRIANGULO ESCALENO")
    else:
        print("NO ES TRIANGULO")


if __name__ == '__main__':
    main()