from tkinter import *
from main import gerar_documento

def ao_clicar_botao():
    dados_para_envio = {
        'nome': nome.get(),
        'cpf': cpf.get(),
        'data': data.get(),
        'data_extenso': data_extenso.get(),
        'data_extenso_dois_dias': data_extenso_dois_dias.get(),
        'data_extenso_um_dia': data_extenso_um_dia.get(),
        'data_extenso_seis': data_extenso_seis.get(),
        'data_seis': data_seis.get()
    }
    gerar_documento(dados_para_envio)

janela = Tk()
janela.title("ASA - Sistema de Automação TRT")
janela.iconbitmap("asa.ico")
janela.configure(background="#004AAD")
janela.state("zoomed")
image = PhotoImage(file="asa.png")
image = image.subsample(2, 2)
label_imagem = Label(janela, image=image, bg="#004AAD")
label_imagem.place(x="1cm", y="1cm")

def focus_in(event, campo, texto_sombra):
    if campo.get() == texto_sombra:
        campo.delete(0, END)
        campo.config(fg="black")

def focus_out(event, campo, texto_sombra):
    if campo.get() == "":
        campo.insert(0, texto_sombra)
        campo.config(fg="grey")

def pular(event, proximo_campo):
    proximo_campo.focus_set()

sombra1 = "Digite o nome: "
nome = Entry(janela, fg="grey")
nome.place(x="22.5cm", y=300, width=250, height=30)
nome.insert(0, sombra1)

sombra2 = "Digite o CPF: "
cpf = Entry(janela, fg="grey")
cpf.place(x="22.5cm", y=370, width=250, height=30)
cpf.insert(0, sombra2)

sombra3 = "Digite a data: "
data = Entry(janela, fg="grey")
data.place(x="22.5cm", y=440, width=250, height=30)
data.insert(0,sombra3)

sombra4 = "Digite a data por extenso: "
data_extenso = Entry(janela, fg="grey")
data_extenso.place(x="22.5cm", y=510, width=250, height=30)
data_extenso.insert(0, sombra4)

sombra5 = "Digite a data da NR6 por extenso: "
data_extenso_dois_dias = Entry(janela, fg="grey")
data_extenso_dois_dias.place(x="22.5cm", y=580, width=250, height=30)
data_extenso_dois_dias.insert(0, sombra5)

sombra6 = "Digite a data da NR35 por extenso: "
data_extenso_um_dia = Entry(janela, fg="grey")
data_extenso_um_dia.place(x="22.5cm", y=650, width=250, height=30)
data_extenso_um_dia.insert(0, sombra6)

sombra7 = "Digite a data da EPI de seis meses por extenso: "
data_extenso_seis = Entry(janela, fg="grey")
data_extenso_seis.place(x="22.5cm", y=720, width=250, height=30)
data_extenso_seis.insert(0, sombra7)

sombra8 = "Digite a data da EPI de seis meses: "
data_seis = Entry(janela, fg="grey")
data_seis.place(x="22.5cm", y=790, width=250, height=30)
data_seis.insert(0, sombra8)

nome.bind("<FocusIn>", lambda e: focus_in(e, nome, sombra1))
nome.bind("<FocusOut>", lambda e: focus_out(e, nome, sombra1))
nome.bind("<Return>", lambda e: pular(e, cpf))

cpf.bind("<FocusIn>", lambda e: focus_in(e, cpf, sombra2))
cpf.bind("FocusOut>", lambda e: focus_out(e, cpf, sombra2))
cpf.bind("<Return>", lambda e: pular(e, data))

data.bind("<FocusIn>", lambda e: focus_in(e, data, sombra3))
data.bind("<FocusOut>", lambda e: focus_out(e, data, sombra3))
data.bind("<Return>", lambda e: pular(e, data_extenso))

data_extenso.bind("<FocusIn>", lambda e: focus_in(e, data_extenso, sombra4))
data_extenso.bind("<FocusOut>", lambda e: focus_out(e, data_extenso, sombra4))
data_extenso.bind("<Return>", lambda e: pular(e, data_extenso_dois_dias))

data_extenso_dois_dias.bind("<FocusIn>", lambda e: focus_in(e, data_extenso_dois_dias, sombra5))
data_extenso_dois_dias.bind("<FocusOut>", lambda e: focus_out(e, data_extenso_dois_dias, sombra5))
data_extenso_dois_dias.bind("<Return>", lambda e: pular(e, data_extenso_um_dia))

data_extenso_um_dia.bind("<FocusIn>", lambda e: focus_in(e, data_extenso_um_dia, sombra6))
data_extenso_um_dia.bind("<FocusOut>", lambda e: focus_out(e, data_extenso_um_dia, sombra6))
data_extenso_um_dia.bind("<Return>", lambda e: pular(e, data_extenso_seis))

data_extenso_seis.bind("<FocusIn>", lambda e: focus_in(e, data_extenso_seis, sombra7))
data_extenso_seis.bind("<FocusOut>", lambda e: focus_out(e, data_extenso_seis, sombra7))
data_extenso_seis.bind("<Return>", lambda e: pular(e, data_seis))

data_seis.bind("<FocusIn>", lambda e: focus_in(e, data_seis, sombra8))
data_seis.bind("<FocusOut>", lambda e: focus_out(e, data_seis, sombra8))
data_seis.bind("<Return>", lambda e: print(f"Dados: {nome.get()}, {cpf.get()}, {data.get()}, {data_extenso.get()}, {data_extenso_dois_dias.get()}, {data_extenso_um_dia.get()}, {data_extenso_seis.get()}, {data_seis.get()}"))

janela.focus()

sistema = Label(janela, 
                text="AUTOMATIZE SEU TRT", 
                bg="#004AAD", 
                fg="white",
                font=("Arial", 30)).place(x="20cm", y="3cm")

botao = Button(
    janela,
    text="GERAR DOCUMENTO",
    command=ao_clicar_botao,
    )

botao.place(x="22.5cm", y=860, width=250, height=30)

janela.mainloop()