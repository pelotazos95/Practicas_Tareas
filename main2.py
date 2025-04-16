import flet as ft
import ConsultasUsuarios
import CopiasSeguridad
import selecion

def main(page: ft.Page):
    page.title = "APP TAREAS"

    def route_change(e):
        page.views.clear()

        if page.route == "ConsultasUsuarios" and page.route is not None:
            print("Consultas")
            page.views.append(
                ft.View(
                    route="ConsultasUsuarios",
                    controls=[ConsultasUsuarios.main(page)]
                )
            )
        elif page.route == "CopiasSeguridad" and page.route is not None:
            print("Seguridad")
            page.views.append(
                ft.View(
                    route="CopiasSeguridad",
                    controls=[CopiasSeguridad.main(page)]
                )
            )
        elif page.route == "selecion" and page.route is not None:
            print("selecion")
            page.views.append(
                ft.View(
                    route="selecion",
                    controls=[selecion.main(page)]
                )
            )

        page.update()


    page.on_route_change = route_change
    page.go("selecion")

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER, port=30019)