from tkinter import *
import requests

def get_quote():
    #==>Obtenemos el JSON de la api.kanye.rest<==
    response = requests.get(url="https://api.kanye.rest/")
    # Elevamos error el status code no es exitoso
    response.raise_for_status()
    # Pasamos el objeto a JSON
    data = response.json()
    # Obtenemos el quote
    quote = data["quote"]
    #==>FIN de Obtenemos el JSON de la api.kanye.rest<==

    # Trabajo con Tkinter
    canvas.itemconfig(quote_text, text = quote)  



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
# Uso del get_quote() en el botón de la aplicación
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()