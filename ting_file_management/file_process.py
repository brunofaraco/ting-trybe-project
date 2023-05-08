import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    file = txt_importer(path_file)
    files_read = []

    for i in range(instance.__len__()):
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


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
