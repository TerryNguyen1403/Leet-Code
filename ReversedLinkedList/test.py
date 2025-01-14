import ReversedLinkedList
from typing import Optional

def main():
    ListNode = ReversedLinkedList.ListNode
    # Tạo linked list từ mảng [1, 2, 3, 4, 5]
    nodes = [ListNode(i) for i in range(1, 6)]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    head = nodes[0]  # Head của linked list

    # In linked list ban đầu
    print("Original Linked List:")
    print_linked_list(head)

    solution = ReversedLinkedList.Solution()
    result = solution.reversedList(head)

    print("Reversed Linked List:")
    print_linked_list(result)


def print_linked_list(head: Optional[ReversedLinkedList.ListNode]):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "-> None \n")
        current = current.next

if __name__ == '__main__':
    main()