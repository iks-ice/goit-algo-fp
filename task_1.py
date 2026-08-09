class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Список порожній")

    def reverse(self):
        prev = None
        cur = self.head
        
        while cur:
            next_node = cur.next  
            cur.next = prev       
            prev = cur            
            cur = next_node       
            
        self.head = prev          

    def insertion_sort(self):
        sorted_head = None        
        cur = self.head           
        
        while cur:
            next_node = cur.next  
            
            if sorted_head is None or sorted_head.data >= cur.data:
                cur.next = sorted_head
                sorted_head = cur
            else:
                search = sorted_head
                while search.next and search.next.data < cur.data:
                    search = search.next
                
                cur.next = search.next
                search.next = cur
                
            cur = next_node
            
        self.head = sorted_head

    @staticmethod
    def merge_sorted(list1, list2):
        dummy = Node()
        tail = dummy
        
        cur1 = list1.head
        cur2 = list2.head
        
        while cur1 and cur2:
            if cur1.data <= cur2.data:
                tail.next = cur1
                cur1 = cur1.next
            else:
                tail.next = cur2
                cur2 = cur2.next
            tail = tail.next 
            
        if cur1:
            tail.next = cur1
        elif cur2:
            tail.next = cur2
            
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

print("--- 1. Тест реверсування та сортування ---")
list_a = LinkedList()
for val in [20, 5, 50, 15, 30]:
    list_a.insert_at_end(val)

print("Оригінальний список A:")
list_a.print_list()

list_a.reverse()
print("Після реверсування:")
list_a.print_list()

list_a.insertion_sort()
print("Після сортування вставками:")
list_a.print_list()


print("\n--- 2. Тест об'єднання двох відсортованих списків ---")
# Створимо два вже відсортованих списки
list1 = LinkedList()
for val in [1, 3, 7, 10]:
    list1.insert_at_end(val)

list2 = LinkedList()
for val in [2, 5, 8, 12, 15]:
    list2.insert_at_end(val)

print("Список 1:")
list1.print_list()
print("Список 2:")
list2.print_list()

merged = LinkedList.merge_sorted(list1, list2)
print("Результат об'єднання:")
merged.print_list()
