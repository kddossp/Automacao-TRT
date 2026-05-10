from docx import Document

arquivo = "TRT/modelos/servente_engpro/TRT_COMPLETO.docx"

doc = Document(arquivo)

substituicoes = {
    "{nome}": "KEVYN DIAS CAMPOS",
    "{cpf}": "547.259.578-95",
    "{data}": "04/05/2026",
    "{data_extenso}": "04 de Maio de 2026",
    "{data_extenso_dois_dias}": "06 de Maio de 2026",
    "{data_extenso_um_dia}": "05 de Maio de 2026",
    "{data_extenso_seis}": "04 de Novembro de 2026",
    "{data_seis}": "04/11/2026"
}

for element in doc.element.iter():
    if element.tag.endswith('}t') and element.text:
        texto = element.text

        for chave, valor in substituicoes.items():
            if chave in texto:
                texto = texto.replace(chave, valor)
        

        element.text = texto

doc.save("resultado_teste.docx")

print("Arquivo gerado com sucesso!")