import flet as ft


def main(page):

    def login(e):
        if not entrada_nombre.value:
            # Si no se ingresa un nombre, se muestra un mensaje de error
            entrada_nombre.error_text = "Por favor, digite su nombre."

            page.update()
        if not entrada_contraseña.value:
            # Si no se ingresa una contraseña, se muestra un mensaje de error
            entrada_contraseña.error_text = "Campo de Contraseña es obligatorio."
            page.update()
        else:
            nombre = entrada_nombre.value  # Se obtiene el valor del campo de entrada de nombre
            # Se obtiene el valor del campo de entrada de contraseña
            contraseña = entrada_contraseña.value
            # Se imprime en la consola el nombre y la contraseña ingresados
            print(f"Nombre: {nombre}\nContraseña: {contraseña}")

            page.clean()  # FuncionSe limpia la página
            page.add(
                ft.Text(f"Bienvenido {
                        nombre}.\nSea bienvenido a nuestra aplicacion.")
            )  # Se agrega un texto de bienvenida a la página

    # Se crea un campo de entrada de texto para el nombre
    entrada_nombre = ft.TextField(label="Digite su Nombre")
    # Se crea un campo de entrada de texto para la contraseña
    entrada_contraseña = ft.TextField(label="Digite su Apellido")

    page.add(
        entrada_nombre,
        entrada_contraseña,
        # Se agrega un botón con texto "Clique em mim" que ejecuta la función login al hacer clic
        ft.ElevatedButton("Clique em mim", on_click=login)
    )


ft.app(target=main)  # Se inicia la aplicación con la función main como objetivo
