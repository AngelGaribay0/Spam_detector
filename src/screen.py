import tkinter as tk
import spam_detector # importar nuestro modulo

def analizar_email():
    # funcion que se ejecuta al presionar el boton
    texto = entrada_email.get()
    if texto == "":
        etiqueta_resultado.config(text = "porfavor escribe un email")
        return
    Resultado = spam_detector.predecir_spam(texto, modelo, vectorizer)

    if Resultado == "SPAM":
        etiqueta_resultado.config(text= " SPAM",fg="red")
    else:
        etiqueta_resultado.config(text= "NO SPAM", fg= "green")
    
def main():
    global modelo, vectorizer, entrada_email, etiqueta_resultado
    #entrenar el modelo usando la funcion del modulo
    print("entrenando modelo...")

    modelo, vectorizer = spam_detector.entrenar_modelo()
    #mostrar precision
    accuracy = spam_detector.evaluar_modelo(modelo, vectorizer)
    print(f"precision del modelo: {accuracy:.2f}")
    # crear ventana
    ventana = tk.Tk()
    ventana.title("Detector de spam")
    ventana.geometry("500x300")

    #titulo
    titulo = tk.Label(ventana, text="Detector de spam", font=("Arial", 16, "bold"))
    titulo.pack(pady=20)

    #intstruccion
    instruccion = tk.Label(ventana, text= "Escribe un email para analizar:")
    instruccion.pack()

    #entrada de texto
    entrada_email = tk.Entry(ventana, width=50)
    entrada_email.pack(pady=10)

    #boton
    boton = tk.Button(ventana, text="Analizar", command=analizar_email, bg="#4CAF50",fg="white", padx=20,pady=5)
    boton.pack(pady=10)

    #resultado
    etiqueta_resultado = tk.Label(ventana, text="", font= ("Arial", 14))
    etiqueta_resultado.pack(pady=20)
    ventana.mainloop()
if __name__ == "__main__":
    main()