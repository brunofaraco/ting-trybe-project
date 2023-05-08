import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    file = txt_importer(path_file)
    files_read = []

    for i in range(len(instance)):
        file_name = instance.search(i)["nome_do_arquivo"]
        files_read.append(file_name)

    if path_file not in files_read:
        data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file,
        }

        instance.enqueue(data)
        sys.stdout.write(str(data))


def remove(instance: Queue):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")

    else:
        path_file = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance: Queue, position: int):
    try:
        data = instance.search(position)
        sys.stdout.write(str(data))
    except IndexError:
        sys.stderr.write("Posição inválida")
