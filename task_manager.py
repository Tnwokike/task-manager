

from dataclasses import dataclass
from typing import Optional



@dataclass
class Node:
    """A node holds one task and a pointer to the next node."""
    task: str
    priority: int                       
    next: Optional["Node"] = None



class TaskList:
    """Singly linked list of tasks. Tracks head and size manually."""

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.size: int = 0

    
    def add_to_front(self, task: str, priority: int) -> None:
        """O(1) insertion at the head."""
        self.head = Node(task, priority, self.head)
        self.size += 1

    def add_to_end(self, task: str, priority: int) -> None:
        """O(n) insertion at the tail — must walk to the last node."""
        new_node = Node(task, priority)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1

    
    def remove(self, task: str) -> bool:
        """Remove the first node matching `task`. Returns True on success."""
        if self.head is None:
            return False

        
        if self.head.task == task:
            self.head = self.head.next
            self.size -= 1
            return True

       
        prev, curr = self.head, self.head.next
        while curr is not None:
            if curr.task == task:
                prev.next = curr.next      
                self.size -= 1
                return True
            prev, curr = curr, curr.next
        return False

   
    def display(self) -> None:
        if self.head is None:
            print("  (no tasks)")
            return
        labels = {1: "HIGH ", 2: "MED  ", 3: "LOW  "}
        current, idx = self.head, 0
        while current is not None:
            tag = labels.get(current.priority, "?    ")
            print(f"  {idx:>2}. [{tag}] {current.task}")
            current = current.next
            idx += 1

    def search(self, task: str) -> int:
        """Linear search. Returns position (0-based) or -1 if not found."""
        current, idx = self.head, 0
        while current is not None:
            if current.task == task:
                return idx
            current = current.next
            idx += 1
        return -1

    
    def reverse(self) -> None:
        """Reverse the list in place by re-pointing each node's `next`."""
        prev, curr = None, self.head
        while curr is not None:
            nxt = curr.next      
            curr.next = prev     
            prev = curr          
            curr = nxt           
        self.head = prev


def prompt_int(message: str) -> int:
    while True:
        raw = input(message).strip()
        if raw.lstrip("-").isdigit():
            return int(raw)
        print("  Please enter a whole number.")


def prompt_priority() -> int:
    while True:
        p = prompt_int("Priority (1=High, 2=Medium, 3=Low): ")
        if p in (1, 2, 3):
            return p
        print("  Priority must be 1, 2, or 3.")


def main() -> None:
    tasks = TaskList()

    tasks.add_to_end("Write project README", 1)
    tasks.add_to_end("Refactor linked list module", 2)
    tasks.add_to_end("Reply to emails", 3)
    tasks.add_to_end("Plan weekend trip", 3)

    menu = (
        "\n----- Task Manager -----\n"
        "1. Show all tasks\n"
        "2. Add task to front\n"
        "3. Add task to end\n"
        "4. Remove task by name\n"
        "5. Search for a task\n"
        "6. Reverse task order\n"
        "7. Show task count\n"
        "0. Exit\n"
    )

    print("=========================================")
    print("   Task Manager (Python Linked List)     ")
    print("=========================================")

    while True:
        print(menu)
        choice = prompt_int("Choice: ")

        if choice == 1:
            print("Tasks:")
            tasks.display()

        elif choice == 2:
            name = input("Task name: ").strip()
            if not name:
                print("  Task name cannot be empty.")
                continue
            tasks.add_to_front(name, prompt_priority())
            print(f"  Added '{name}' to the front.")

        elif choice == 3:
            name = input("Task name: ").strip()
            if not name:
                print("  Task name cannot be empty.")
                continue
            tasks.add_to_end(name, prompt_priority())
            print(f"  Added '{name}' to the end.")

        elif choice == 4:
            name = input("Task to remove: ").strip()
            if tasks.remove(name):
                print(f"  Removed '{name}'.")
            else:
                print(f"  '{name}' not found.")

        elif choice == 5:
            name = input("Task to find: ").strip()
            pos = tasks.search(name)
            if pos == -1:
                print(f"  '{name}' is not in the list.")
            else:
                print(f"  Found '{name}' at position {pos}.")

        elif choice == 6:
            tasks.reverse()
            print("  List reversed.")
            tasks.display()

        elif choice == 7:
            print(f"  Total tasks: {tasks.size}")

        elif choice == 0:
            print("Goodbye!")
            return

        else:
            print("  Invalid choice. Please try again.")


if __name__ == "__main__":
    main()