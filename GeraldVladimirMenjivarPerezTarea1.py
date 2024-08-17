class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)
        print(f"Insertado: {item}")

    def desapilar(self):
        if self.esta_vacia():
            return "La pila esta vacia"
        return self.items.pop()

    def mostrar_pila(self):
        return self.items


def menu():
    pila = Pila()
    while True:
        print("\n--- Implementacion de una Pila ---")
        print("1. Insertar elemento en la pila")
        print("2. Eliminar todos los elementos modo pila(lifo)")
        print("3. Mostrar pila actual")
        print("4. Salir")

        opcion = input("Elige una opcion: ")

        if opcion == '1':
            item = input("Introduce el elemento  a insertar: ")
            pila.apilar(item)

        elif opcion == '2':
            print("\nEliminando elementos...😞")
            while not pila.esta_vacia():
                eliminado = pila.desapilar()
                print(f"Elemento eliminado: {eliminado}")
            print("Todos los elementos han sido eliminados. La pila esta vacia ✔️.")

        elif opcion == '3':
            print("Elementos en la pila:", pila.mostrar_pila())

        elif opcion == '4':
            print("Saliendo del programa.")
            break

        else:
            print(" ❌ Opcion no valida. Inténtalo de nuevo 🙃.")


if __name__ == "__main__":
    menu()
