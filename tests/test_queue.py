"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest

from src.queue import Queue, Node


class QueueTestCase(unittest.TestCase):

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(str(queue), '1')
        queue.enqueue(2)
        self.assertEqual(str(queue), '1\n2')
        queue.enqueue(3)
        self.assertEqual(str(queue), '1\n2\n3')

