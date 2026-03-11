# Contact Manager using Array and Linked List
#Implement a Contact Manager using Array and Linked List with operations Add, Search, and Delete contacts, generate Search and Delete methods, 
# and compare both approaches based on insertion and deletion efficiency.
'''class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def __repr__(self):
        return f"Contact({self.name}, {self.phone}, {self.email})"


# Array-based Contact Manager
class ArrayContactManager:
    def __init__(self):
        self.contacts = []
    
    def add(self, name, phone, email):
        """Add contact - O(1) average"""
        self.contacts.append(Contact(name, phone, email))
    
    def search(self, name):
        """Search contact - O(n)"""
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None
    
    def delete(self, name):
        """Delete contact - O(n)"""
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                self.contacts.pop(i)
                return True
        return False


# Linked List Node
class Node:
    def __init__(self, contact):
        self.contact = contact
        self.next = None


# Linked List-based Contact Manager
class LinkedListContactManager:
    def __init__(self):
        self.head = None
    
    def add(self, name, phone, email):
        """Add contact - O(1)"""
        new_node = Node(Contact(name, phone, email))
        new_node.next = self.head
        self.head = new_node
    
    def search(self, name):
        """Search contact - O(n)"""
        current = self.head
        while current:
            if current.contact.name == name:
                return current.contact
            current = current.next
        return None
    
    def delete(self, name):
        """Delete contact - O(n)"""
        if not self.head:
            return False
        
        if self.head.contact.name == name:
            self.head = self.head.next
            return True
        
        current = self.head
        while current.next:
            if current.next.contact.name == name:
                current.next = current.next.next
                return True
            current = current.next
        return False


# Comparison and Testing
if __name__ == "__main__":
    # Test Array Manager
    print("=== Array-based Contact Manager ===")
    array_mgr = ArrayContactManager()
    array_mgr.add("Alice", "111-1111", "alice@email.com")
    array_mgr.add("Bob", "222-2222", "bob@email.com")
    array_mgr.add("Charlie", "333-3333", "charlie@email.com")
    
    print("Search Bob:", array_mgr.search("Bob"))
    array_mgr.delete("Bob")
    print("Search Bob after delete:", array_mgr.search("Bob"))
    
    # Test Linked List Manager
    print("\n=== Linked List-based Contact Manager ===")
    ll_mgr = LinkedListContactManager()
    ll_mgr.add("Alice", "111-1111", "alice@email.com")
    ll_mgr.add("Bob", "222-2222", "bob@email.com")
    ll_mgr.add("Charlie", "333-3333", "charlie@email.com")
    
    print("Search Bob:", ll_mgr.search("Bob"))
    ll_mgr.delete("Bob")
    print("Search Bob after delete:", ll_mgr.search("Bob"))
    
    # Efficiency Comparison
    print("\n=== Efficiency Comparison ===")
    print("Array:\n  Add: O(1) | Search: O(n) | Delete: O(n)")
    print("Linked List:\n  Add: O(1) | Search: O(n) | Delete: O(n)")
    print("\nNote: Linked List is better for frequent insertions at the beginning.")'''



#2.Implement a **Library Book Request System** using a **Queue (FIFO)** and **Priority Queue** where **faculty requests have higher priority than student requests**, generate **enqueue() and dequeue() methods using GitHub Copilot**, 
# and **test with mixed student and faculty requests to verify correct prioritization.
from queue import Queue, PriorityQueue
class BookRequest:
    def __init__(self, requester_type, book_title):
        self.requester_type = requester_type  # 'faculty' or 'student'
        self.book_title = book_title
    
    def __repr__(self):
        return f"BookRequest({self.requester_type}, {self.book_title})"
# Queue-based Book Request System
class QueueBookRequestSystem:
    def __init__(self):
        self.requests = Queue()
    
    def enqueue(self, requester_type, book_title):
        """Add a book request to the queue."""
        self.requests.put(BookRequest(requester_type, book_title))
    
    def dequeue(self):
        """Remove and return the next book request from the queue."""
        if not self.requests.empty():
            return self.requests.get()
        return None
# Priority Queue-based Book Request System
class PriorityQueueBookRequestSystem:
    def __init__(self):
        self.requests = PriorityQueue()
    
    def enqueue(self, requester_type, book_title):
        """Add a book request to the priority queue with faculty having higher priority."""
        priority = 0 if requester_type == 'faculty' else 1
        self.requests.put((priority, BookRequest(requester_type, book_title)))
    
    def dequeue(self):
        """Remove and return the next book request from the priority queue."""
        if not self.requests.empty():
            return self.requests.get()[1]  # Return the BookRequest object
        return None
# Testing the Book Request Systems
if __name__ == "__main__":
    # Test Queue-based System
    print("=== Queue-based Book Request System ===")
    queue_system = QueueBookRequestSystem()
    queue_system.enqueue('student', 'Book A')
    queue_system.enqueue('faculty', 'Book B')
    queue_system.enqueue('student', 'Book C')
    
    print(queue_system.dequeue())  # Output: BookRequest(student, Book A)
    print(queue_system.dequeue())  # Output: BookRequest(faculty, Book B)
    print(queue_system.dequeue())  # Output: BookRequest(student, Book C)
    
    # Test Priority Queue-based System
    print("\n=== Priority Queue-based Book Request System ===")
    priority_queue_system = PriorityQueueBookRequestSystem()
    priority_queue_system.enqueue('student', 'Book A')
    priority_queue_system.enqueue('faculty', 'Book B')
    priority_queue_system.enqueue('student', 'Book C')
    
    print(priority_queue_system.dequeue())  # Output: BookRequest(faculty, Book B)
    print(priority_queue_system.dequeue())  # Output: BookRequest(student, Book A)
    print(priority_queue_system.dequeue())  # Output: BookRequest(student, Book C)
    # The Queue-based system processes requests in the order they were received, regardless of requester type, while the Priority Queue-based system prioritizes faculty requests over student requests, ensuring that faculty requests are processed first.    


