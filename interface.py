from tkinter import *
from tkcalendar import Calendar
from main import gerar_documento

def abrir_gerados():
    import os, sys
    base = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
    os.startfile(os.path.join(base, "gerados"))

def ao_clicar_botao():
    from datetime import datetime

    data_str = data.get()

    data_str_seis = data_seis.get()

    data_str_dois = data_dois_dias.get()

    data_str_um = data_um_dia.get()

    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    
    try:
        d_um = datetime.strptime(data_um_dia.get(), "%d/%m/%Y")
        data_extenso_um_auto = f"{d_um.day} de {meses[d_um.month - 1]} de {d_um.year}"
    except ValueError:
        data_extenso_um_auto = data_str_um

    try:
        d_dois = datetime.strptime(data_dois_dias.get(), "%d/%m/%Y")
        data_extenso_dois_auto = f"{d_dois.day} de {meses[d_dois.month -1]} de {d_dois.year}"
    except ValueError:
        data_extenso_dois_auto = data_str_dois

    try:
        d_seis = datetime.strptime(data_str_seis, "%d/%m/%Y")
        data_extenso_seis_auto = f"{d_seis.day} de {meses[d_seis.month - 1]} de {d_seis.year}"
    except ValueError:
        data_extenso_seis_auto = data_str_seis

    try:
        d = datetime.strptime(data_str, "%d/%m/%Y")
        data_extenso_auto = f"{d.day} de {meses[d.month - 1]} de {d.year}"
    except ValueError:
        data_extenso_auto = data_str

    dados_para_envio = {
        'nome': nome.get(),
        'cpf': cpf.get(),
        'data': data_str,
        'data_extenso': data_extenso_auto,
        'data_extenso_dois_dias': data_extenso_dois_auto,
        'data_extenso_um_dia': data_extenso_um_auto,
        'data_extenso_seis': data_extenso_seis_auto,
        'data_seis': data_str_seis,
        'empresa': empresa_var.get(),
        'funcao': funcao_var.get()
    }
    gerar_documento(dados_para_envio)

empresas_funcoes = {
    "CELTA": ["AZULEJISTA", "ENCARREGADO", "MEIO OFICIAL", "PEDREIRO", "SERVENTE"],
    "DLM": ["ARMADOR", "AZULEJISTA", "CARPINTEIRO", "ENCARREGADO", "PEDREIRO", "PINTOR DE OBRAS", "SERVENTE"],
    "ENGPRO": ["APONTADOR", "CARPINTEIRO", "ENCARREGADO", "OPERADOR DE CREMALHEIRA", "PEDREIRO", "PINTOR DE OBRAS", "SERVENTE"],
    "LDR": ["AZULEJISTA", "PEDREIRO", "SERVENTE"],
    "VLV": ["ARMADOR", "CARPINTEIRO", "PEDREIRO", "SERVENTE"],
    "WC": ["APONTADOR", "ARMADOR", "CARPINTEIRO", "ENCARREGADO", "MARTELETEIRO", "MESTRE DE OBRAS", "OPERADOR DE MINI GRUA", "PEDREIRO", "SERVENTE"]
}

janela = Tk()
janela.title("ASA - Sistema de Automação TRT")
janela.iconbitmap("asa.ico")
janela.configure(background="#004AAD")
janela.state("zoomed")
image = PhotoImage(file="asa.png")
image = image.subsample(2, 2)
label_imagem = Label(janela, image=image, bg="#004AAD")
label_imagem.place(x="1cm", y="1cm")

def atualizar_funcoes(*args):
    empresa_selecionada = empresa_var.get()
    funcoes = empresas_funcoes.get(empresa_selecionada, [])
    funcao["menu"].delete(0, "end")
    for x in funcoes:
        funcao["menu"].add_command(label=x, command=lambda v=x: funcao_var.set(v))

def abrir_calendario(campo):
    top = Toplevel(janela)
    top.title("Selecionar Data")
    top.grab_set()
    top.iconbitmap("asa.ico")

    x = janela.winfo_x() + janela.winfo_width() // 2 - 150
    y = janela.winfo_y() + janela.winfo_height() // 2 - 125
    top.geometry(f"300x250+{x}+{y}")

    cal = Calendar(top, selectmode='day', date_pattern='dd/mm/yyyy')
    cal.pack(padx=10, pady=10)

    def confirmar():
        campo.delete(0, END)
        campo.insert(0, cal.get_date())
        campo.config(fg="black")
        top.destroy()

    Button(top, text="Confirmar", command=confirmar).pack(pady=5)


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

def formatar_cpf(event):
    texto = cpf.get().replace(".", "").replace("-", "").replace(" ", "")
    texto = texto[:11]  # limita a 11 dígitos
    if len(texto) >= 4:
        texto = texto[:3] + "." + texto[3:]
    if len(texto) >= 8:
        texto = texto[:7] + "." + texto[7:]
    if len(texto) >= 12:
        texto = texto[:11] + "-" + texto[11:]
    cpf.delete(0, END)
    cpf.insert(0, texto)
    cpf.config(fg="black")

sombra1 = "Digite o nome: "
nome = Entry(janela, fg="grey")
nome.place(x="22.5cm", y=380, width=250, height=30)
nome.insert(0, sombra1)

sombra2 = "Digite o CPF: "
cpf = Entry(janela, fg="grey")
cpf.place(x="22.5cm", y=450, width=250, height=30)
cpf.insert(0, sombra2)

sombra3 = "Digite a data: "
data = Entry(janela, fg="grey")
data.place(x="22.5cm", y=520, width=220, height=30)
data.insert(0,sombra3)

sombra4 = "Digite a data da NR6: "
data_dois_dias = Entry(janela, fg="grey")
data_dois_dias.place(x="22.5cm", y=590, width=220, height=30)
data_dois_dias.insert(0, sombra4)

sombra5 = "Digite a data da NR35: "
data_um_dia = Entry(janela, fg="grey")
data_um_dia.place(x="22.5cm", y=660, width=220, height=30)
data_um_dia.insert(0, sombra5)

sombra6 = "Digite a data da EPI de seis meses: "
data_seis = Entry(janela, fg="grey")
data_seis.place(x="22.5cm", y=730, width=220, height=30)
data_seis.insert(0, sombra6)

nome.bind("<FocusIn>", lambda e: focus_in(e, nome, sombra1))
nome.bind("<FocusOut>", lambda e: focus_out(e, nome, sombra1))
nome.bind("<Return>", lambda e: pular(e, cpf))

cpf.bind("<FocusIn>", lambda e: focus_in(e, cpf, sombra2))
cpf.bind("FocusOut>", lambda e: focus_out(e, cpf, sombra2))
cpf.bind("<Return>", lambda e: pular(e, data))
cpf.bind("<KeyRelease>", formatar_cpf)

data.bind("<FocusIn>", lambda e: focus_in(e, data, sombra3))
data.bind("<FocusOut>", lambda e: focus_out(e, data, sombra3))
data.bind("<Return>", lambda e: pular(e, data_dois_dias))

empresa_var = StringVar()
empresa_var.set("SELECIONE A EMPRESA")
empresa = OptionMenu(janela, empresa_var, "CELTA", "DLM", "ENGPRO", "LDR", "VLV", "WC")
empresa.place(x="22.5cm", y=240, width=250, height=30)

funcao_var = StringVar()
funcao_var.set("SELECIONE A FUNÇÃO")
funcao = OptionMenu(janela, funcao_var, "SELECIONE A FUNÇÃO")
funcao.place(x="22.5cm", y=310, width=250, height=30)
empresa_var.trace("w", atualizar_funcoes)

btn_data = Button(janela, text="📅", command=lambda: abrir_calendario(data))
btn_data.place(x="28.4cm", y=520, width=30, height=30)

data_dois_dias.bind("<FocusIn>", lambda e: focus_in(e, data_dois_dias, sombra4))
data_dois_dias.bind("<FocusOut>", lambda e: focus_out(e, data_dois_dias, sombra4))
data_dois_dias.bind("<Return>", lambda e: pular(e, data_um_dia))

btn_data_dois = Button(janela, text="📅", command=lambda: abrir_calendario(data_dois_dias))
btn_data_dois.place(x="28.4cm", y=590, width=30, height=30)

data_um_dia.bind("<FocusIn>", lambda e: focus_in(e, data_um_dia, sombra5))
data_um_dia.bind("<FocusOut>", lambda e: focus_out(e, data_um_dia, sombra5))
data_um_dia.bind("<Return>", lambda e: pular(e, data_seis))

btn_data_um = Button(janela, text="📅", command=lambda: abrir_calendario(data_um_dia))
btn_data_um.place(x="28.4cm", y=660, width=30, height=30)

data_seis.bind("<FocusIn>", lambda e: focus_in(e, data_seis, sombra6))
data_seis.bind("<FocusOut>", lambda e: focus_out(e, data_seis, sombra6))
data_seis.bind("<Return>", lambda e: print(f"Dados: {nome.get()}, {cpf.get()}, {data.get()}, {data_dois_dias.get()}, {data_um_dia.get()}, {data_seis.get()}"))

btn_data_seis = Button(janela, text="📅", command=lambda: abrir_calendario(data_seis))
btn_data_seis.place(x="28.4cm", y=730, width=30, height=30)

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
    background="yellow"
    )

gerados = Button(
    janela,
    text="GERADOS",
    command=abrir_gerados,
    background="yellow"
)

botao.place(x="22.5cm", y=860, width=250, height=30)
gerados.place(x="22.5cm", y=920, width=250, height=30)

janela.mainloop()