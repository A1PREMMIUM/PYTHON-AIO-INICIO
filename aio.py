import os
import flet as ft

# Se establece la variable de entorno para el tamaño máximo de mensaje en el WebSocket
os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "10485760"


def main(page: ft.Page):
    # Corregido: se elimina la coma al final de la línea
    linea = ft.Row(wrap=True, scroll="always", expand=True)
    page.add(linea)

    for i in range(12):
        # Corregido: se crea un nuevo elemento en cada iteración del bucle
        elemento = ft.Column(
            width=250,
            height=250,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.AMBER_100,
            border=ft.border.all(1, ft.colors.BLACK),
            border_radius=ft.border_radius.all(8)
        )
        # Corregido: se agrega el elemento a la línea en cada iteración del bucle
        linea.add(elemento)

    page.update()


ft.app(target=main, view=ft.WEB_BROWSER)
