import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            raise TypeError

        with open(path_file, "r") as file:
            content = file.read()
            lines = content.split("\n")
            return lines

    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

    except TypeError:
        sys.stderr.write("Formato inválido")
