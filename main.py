"""
Punto de entrada de la aplicación.
Inicializa la base de datos y lanza la interfaz gráfica (ventana de login).
"""
import db
from gui import Login


def main():
    # Inicializar la base de datos (archivo ecotech.db en el mismo directorio)
    db.inicializar_bd()
    # Abrir la ventana de login; al autenticarse, la GUI principal se iniciará.
    login = Login()
    login.mainloop()


if __name__ == "__main__":
    main()
