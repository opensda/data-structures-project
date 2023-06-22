"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack

class TestArrs(unittest.TestCase):
    def test_Node(self):
        n1 = Node(1)
        self.assertEqual(n1.data, 1)
        self.assertEqual(n1.next_node, None)
        # self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)

    def test_Stack(self):
        stack = Stack()
        self.assertEqual(stack.top, None)



    # def test_push(self):
    #     stack1 = Stack()
    #     stack1.push('data1')
    #     stack1.push('data2')
    #     stack1.push('data3')
    #     self.assertEqual(stack1.top.data, 'data3')
    #     self.assertEqual(stack1.top.next_node.data, 'data2')
    #     self.assertEqual(stack1.top.next_node.next_node.data, 'data1')











