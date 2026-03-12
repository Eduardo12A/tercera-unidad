class Pila:
    def __init__(self, nombre):
        self.items = []
        self.nombre = nombre

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

    def __str__(self):
        return f"{self.nombre}: {self.items}"

def mover_discos(n, origen, destino, auxiliar):
    if n > 0:

        mover_discos(n - 1, origen, auxiliar, destino)
   
        disco = origen.desapilar()
        destino.apilar(disco)
        print(f"Mover disco {disco} de {origen.nombre} a {destino.nombre}")
        print(f"{torre_a} | {torre_b} | {torre_c}\n")
        
        mover_discos(n - 1, auxiliar, destino, origen)
print("--- Simulador de Torres de Hanoi ---")
cantidad = int(input("¿Con cuántos discos quieres jugar? "))

torre_a = Pila("Torre A")
torre_b = Pila("Torre B")
torre_c = Pila("Torre C")
for i in range(cantidad, 0, -1):
    torre_a.apilar(i)

print("\nEstado Inicial:")
print(f"{torre_a} | {torre_b} | {torre_c}\n")

mover_discos(cantidad, torre_a, torre_c, torre_b)

print("¡Juego completado!")