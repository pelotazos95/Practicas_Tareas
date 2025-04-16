import flet as ft

def main(page: ft.Page):
    page.title = "SELECCIONAR OPCIÓN"
    page.window_width = 400
    page.window_height = 600
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "#000000"

    def elegir_opcion(e):
        if opcion_drop.value == "Control Usuarios":
            page.go("/ConsultasUsuarios")
            page.update()
        elif opcion_drop.value == "Copia Seguridad":
            page.go("/CopiasSeguridad")
            page.update()

    def volver_consulta(e):
        page.go("/ConsultasUsuarios")
        page.update()

    def volver_copias(e):
        page.go("/CopiasSeguridad")
        page.update()

    opcion_drop = ft.Dropdown(
        label="Selecciona opción",
        width=400,
        options=[ft.DropdownOption("Control Usuarios"), ft.DropdownOption("Copia Seguridad")],
        on_change=elegir_opcion,
        border_color="#4a6fa5",
        focused_border_color="#166084",
        filled=True,
        bgcolor="#333333",
        color="#ffffff"
    )

    def vista_principal():
        page.add(
            ft.Column(
                [
                    ft.Text("Selecciona una opción:", size=20, weight="bold", color="#ffffff"),
                    opcion_drop
                ],
                alignment="center",
                horizontal_alignment="center"
            )
        )

    page.update()
    vista_principal()

#if __name__ == "__main__":
    #ft.app(target=main, view=ft.WEB_BROWSER)