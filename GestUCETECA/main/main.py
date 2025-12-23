# main.py - Sistema de Gestión de Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
    
    def agregar_libro(self, titulo, autor):
        libro = {"titulo": titulo, "autor": autor, "disponible": True}
        self.libros.append(libro)
        print(f"Libro '{titulo}' agregado exitosamente")
    
    def listar_libros(self):
        print("\n=== LIBROS DISPONIBLES ===")
        for libro in self.libros:
            estado = "Disponible" if libro["disponible"] else "Prestado"
            print(f"- {libro['titulo']} por {libro['autor']} [{estado}]")

if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.agregar_libro("Cien Años de Soledad", "Gabriel García Márquez")
    biblioteca.agregar_libro("Don Quijote", "Miguel de Cervantes")
    biblioteca.listar_libros()
