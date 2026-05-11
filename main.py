from docx import Document

def gerar_documento(dados):
    substituicoes = {
        "{nome}": dados['nome'],
        "{cpf}": dados['cpf'],
        "{data}": dados['data'],
        "{data_extenso}": dados['data_extenso'],
        "{data_extenso_dois_dias}": dados['data_extenso_dois_dias'],
        "{data_extenso_um_dia}": dados['data_extenso_um_dia'],
        "{data_extenso_seis}": dados['data_extenso_seis'],
        "{data_seis}": dados['data_seis']
    }

    arquivo = "modelos/servente_engpro/TRT_COMPLETO.docx"

    doc = Document(arquivo)

    for element in doc.element.iter():
        if element.tag.endswith('}t') and element.text:
            texto = element.text

            for chave, valor in substituicoes.items():
                if chave in texto:
                    texto = texto.replace(chave, valor)
        

            element.text = texto

    nome_arquivo = f"./gerados/{dados['nome']}.docx"

    doc.save(nome_arquivo)

    print("Arquivo gerado com sucesso!")