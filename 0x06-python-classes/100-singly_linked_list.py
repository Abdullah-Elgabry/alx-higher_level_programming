#!/usr/bin/python3
"""Defining the module."""


class Node:
    """Defining the Node Class."""

    def __init__(self, data, next_node=None):
        """Node INIT.
        Args:
            data (int): new Node data.
            next_node (Node): new Node nxt node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Node data setter."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next_node setter."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """defining singly-linked list class."""

    def __init__(self):
        """SinglyLinkedList INIT."""
        self.__head = None

    def sorted_insert(self, value):
        """function to insert a new node.
        Args:
            value (Node): new Node will be inserted.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Singly Linked List defining."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
