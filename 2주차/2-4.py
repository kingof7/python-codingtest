# 링크드 리스트 구현 - 1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(3)

# [5] -> [12] -> None

first_node = Node(5)
second_node = Node(12)
first_node.next = second_node

third_node = Node(7)
second_node.next = third_node

# ...

# 번거롭다, class 내에 메소드를 만든다

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

linked_list = LinkedList(5)
print(linked_list.head.data)  # [5]

