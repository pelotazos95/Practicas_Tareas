import flet as ft
import os
import signal
from crontab import CronTab

def main(page: ft.Page):
    page.title = "Terminar Proceso"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def consulta_usu():
        page.clean()

        pedir_input = ft.TextField(label="Introduce el PID",width=400,keyboard_type=ft.KeyboardType.NUMBER,
            border_color="#4a6fa5",focused_border_color="#166084",
            bgcolor="#333333",color="#ffffff"
        )
        result_text = ft.Text(color="#ffffff")

        def kill_process(e):
            try:
                pid = int(pedir_input.value)
                result_text.value = f"Proceso {pid} finalizado con éxito."
                result_text.color = "green"
            except ValueError:
                result_text.value = "Introduce un número válido."
                result_text.color = "red"
            except ProcessLookupError:
                result_text.value = f"No se encontró el proceso con PID {pid}."
                result_text.color = "red"
            except PermissionError:
                result_text.value = "No tienes permisos para finalizar este proceso."
                result_text.color = "red"

            page.update()

        btn_kill = ft.ElevatedButton(
            "Finalizar Proceso",
            on_click=kill_process,
            color="white",
            bgcolor="#e74c3c",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                padding=20
            )
        )

        btn_volver = ft.ElevatedButton(
            "Volver",
            on_click=volver_main,
            color="white",
            bgcolor="#3498db",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                padding=20
            )
        )

        page.add(
            ft.Column(
                [
                    ft.Text("Control de Usuarios", size=20, weight="bold", color="#ffffff"),
                    pedir_input,
                    btn_kill,
                    result_text,
                    btn_volver
                ],
                alignment="center",
                horizontal_alignment="center",
                spacing=20
            )
        )

    def volver_main(e):
        page.go("selecion")
        page.update()

    page.update()
    consulta_usu()

#if __name__ == "__main__":
    #ft.app(target=main, view=ft.WEB_BROWSER)