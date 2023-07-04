class Node:
    """Класс для узла очереди"""

    def __init__(self, data):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = None


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None


    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node



    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None

        return data


    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.head is None:
            return ''
        current_value = self.head
        queue_str = ''
        while current_value is not None:
            queue_str += str(current_value.data) + '\n'
            current_value = current_value.next_node
        return queue_str.strip()
