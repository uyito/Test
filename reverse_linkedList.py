class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    prev_node = None
    current = head


    while current is not None:
        next_node = current.next
        current.next = prev_node
        prev_node = current
        current = next_node

    return prev_node

def print_list(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next

if __name__ == '__main__':
    A = Node("A")
    A.next = Node("B")
    A.next.next = Node("C")
    A.next.next.next = None
    print_list(A)
    print('--------------------')
    rev = reverse(A)

    print_list(rev)


