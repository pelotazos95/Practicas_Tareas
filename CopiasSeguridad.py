import flet as ft
import signal
from crontab import CronTab

def main(page: ft.Page):
    page.title = "Tareas Sistemas"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    minutos = [str(i).zfill(2) for i in range(60)]
    horas = [str(i).zfill(2) for i in range(24)]

    color_texto = ft.Text(color="#ffffff")

    def mensaje_alerta(title, message):
        color_texto.value = f"{title}: {message}"
        color_texto.color = "red" if title == "Error" else "green"
        page.update()

    def comprobar_datos(e):
        origen = direct_origen.value.strip()
        destino = direct_destino.value.strip()
        min = opcion_minutos.value
        hr = opcion_horas.value
        dia = dia_semana.value

        if not origen or not destino:
            mensaje_alerta("Error", "Debes introducir ambos directorios.")
            return

        cron = CronTab(user=True)
        job = cron.new(command=f"cp -r {origen} {destino}")

        valor_dias = {
            "Lunes": 1, "Martes": 2, "Miércoles": 3,
            "Jueves": 4, "Viernes": 5, "Sábado": 6, "Domingo": 7
        }

        cron_day = valor_dias.get(dia, "*")

        job.setall(f"{min} {hr} * * {cron_day}")
        cron.write()

        mensaje_alerta("Copia Programada", f"Copia de seguridad programada para {min}:{hr} del {dia}.")

    def volver_main(e):
        page.go("selecion")
        page.update()


    direct_origen = ft.TextField(label="Directorio de Origen", width=400,border_color="#4a6fa5", color="#ffffff")
    direct_destino = ft.TextField(label="Directorio de Destino", width=400,border_color="#4a6fa5", color="#ffffff")
    opcion_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    dia_semana = ft.Dropdown(label="Día de la Semana", width=400,options=[ft.DropdownOption(i) for i in opcion_semana],
                             border_color="#4a6fa5", filled=True, color="#ffffff")
    opcion_minutos = ft.Dropdown(label="Minuto", width=400,options=[ft.DropdownOption(i) for i in minutos],
                                 border_color="#4a6fa5", filled=True, color="#ffffff")
    opcion_horas = ft.Dropdown(label="Hora", width=400,options=[ft.DropdownOption(i) for i in horas],
                               border_color="#4a6fa5", filled=True, color="#ffffff")
    boton_aceptar = ft.ElevatedButton("Programar Copia", on_click=comprobar_datos,color="white", bgcolor="#2ecc71",
                                      style=ft.ButtonStyle(padding=20))
    boton_volver = ft.ElevatedButton("Volver", on_click=volver_main, color="white", bgcolor="#3498db",
                                     style=ft.ButtonStyle(padding=20))

    def columna():
        page.clean()
        page.add(
            ft.Column(alignment="center",horizontal_alignment="center",
                    controls = [ft.Text("Copia de Seguridad", size=20, weight="bold", color="#ffffff"),
                    direct_origen,
                    direct_destino,
                    opcion_minutos,
                    opcion_horas,
                    dia_semana,
                    boton_aceptar,
                    color_texto,
                    boton_volver
                ],
            )
        )

    page.update()
    columna()

#if __name__ == "__main__":
    #ft.app(target=main, view=ft.WEB_BROWSER)