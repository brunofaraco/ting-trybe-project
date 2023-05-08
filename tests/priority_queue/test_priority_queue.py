import pytest
from ting_file_management.priority_queue import PriorityQueue

non_priority_1 = {"qtd_linhas": 10}
non_priority_2 = {"qtd_linhas": 6}

priority = {"qtd_linhas": 3}


def test_basic_priority_queueing():
    instance = PriorityQueue()

    instance.enqueue(non_priority_1)
    instance.enqueue(non_priority_2)

    assert len(instance) == 2
    assert instance.dequeue() == non_priority_1

    instance.enqueue(priority)

    assert instance.search(0) == priority

    assert instance.dequeue() == priority

    with pytest.raises(IndexError):
        instance.search(10)
