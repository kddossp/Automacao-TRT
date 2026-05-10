from tkinter import *

janela = Tk()
janela.title("ASA - Sistema de Automação TRT")
janela.iconbitmap("TRT/asa.ico")
janela.configure(background="#2916f3")
janela.state("zoomed")

sistema = Label(janela, 
                text="ASA", 
                bg="#2916f3", 
                fg="white",
                font=("Arial", 30)).place(relx=0.5, rely=0.5, anchor="center")

janela.mainloop()