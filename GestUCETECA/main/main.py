# main.py - Sistema de Gesti�n de Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def _init_(self):
           self.items = {}  # Cambia lista por diccionario
    
    def agregar_libro(self, titulo, autor):
        libro = {"titulo": titulo, "autor": autor, "disponible": True}
        self.libros.append(libro)
        print(f"Libro '{titulo}' agregado exitosamente")
    
    def listar_libros(self):
        print("\n=== LIBROS DISPONIBLES ===")
        for libro in self.libros:
            estado = "Disponible" if libro["disponible"] else "Prestado"
            print(f"- {libro['titulo']} por {libro['autor']} [{estado}]")

    def prestar_libro(self, titulo, id_usuario):
        for libro in self.libros:
            if libro["titulo"] == titulo and libro["disponible"]:
                libro["disponible"] = False
                print(f"Libro '{titulo}' prestado al usuario {id_usuario}")
                return True

        print("Libro no disponible")
        return False



if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.agregar_libro("Cien A�os de Soledad", "Gabriel Garc�a M�rquez")
    biblioteca.agregar_libro("Don Quijote", "Miguel de Cervantes")
    biblioteca.listar_libros()
