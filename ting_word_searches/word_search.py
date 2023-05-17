from ting_file_management.queue import Queue


def aux_format(word: str, file_line: str, search_content: bool):
    result = []

    for i, line in enumerate(file_line):
        if word.lower() in line.lower():
            content = {"linha": i + 1}
            if search_content:
                content["conteudo"] = line
            result.append(content)
    return result


def aux_find_words(word: str, instance: Queue, search_content=False):
    result = []

    for word_index in range(0, len(instance)):
        words = instance.search(word_index)
        obj_pattern = {
            "palavra": word,
            "arquivo": words['nome_do_arquivo'],
            "ocorrencias": []
        }
        lines_array = aux_format(
            word, words["linhas_do_arquivo"], search_content
            )
        if len(lines_array):
            obj_pattern["ocorrencias"] = lines_array
            result.append(obj_pattern)

    return result


def exists_word(word: str, instance: Queue):
    return aux_find_words(word, instance)


def search_by_word(word: str, instance: Queue):
    return aux_find_words(word, instance, True)
