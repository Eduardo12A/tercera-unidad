def evaluar_posfija(expresion):
    pila = []
    tokens = expresion.split()

    for token in tokens:
        if token.isdigit():
            pila.append(int(token))
        else:
            n2 = pila.pop()
            n1 = pila.pop()
            
            if token == '+':
                pila.append(n1 + n2)
            elif token == '-':
                pila.append(n1 - n2)
            elif token == '*':
                pila.append(n1 * n2)
            elif token == '/':
                pila.append(n1 / n2)
                
    return pila.pop()

print("--- Evaluador de Expresiones Posfijas ---")
print("Ingresa los elementos separados por espacios (Ejemplo: 5 3 + 2 *)")

entrada = input("Expresión: ")
resultado = evaluar_posfija(entrada)

print(f"\nEl resultado de la operación es: {resultado}")