import argparse
from pathlib import Path


def process_includes(path):
    base = Path(path).parent
    with open(path, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    resultado = []
    for linha in linhas:
        if linha.strip().startswith("<!-- include:"):
            file_name = linha.strip().split(":", 1)[1].strip(" -->\n")
            file_path = base / file_name

            # Impede recursão
            with open(file_path, "r", encoding="utf-8") as inc:
                content = inc.read()

            titulo = Path(file_name).stem  # Nome do arquivo sem extensão
            resultado.append(f"---\n### {titulo}\n")
            resultado.append(content)
        else:
            resultado.append(linha)

    return resultado


def generate_doc(doc_base_path, doc_output_path):
    output = process_includes(doc_base_path)
    with open(doc_output_path, "w", encoding="utf-8") as f:
        f.writelines(output)
