The application I built is a taks manager which is a console-based to-do list completely in python. Every task is stored as a node in a
hand-written singly linked list. Every menu option in the program corresponds to a fundamental linked-list operation, so the project also works
as a refrence for how the data structure should behave at the pointer level. The problem that this project works to solve is how usually when people
use the python language they use "list" reflexivity but "list" is a dynamic array, which has very different preformance characteristics then that of a 
linked list. Therfore this project exist to demonstrate the difference between node-based structure and pythons built in containers. It also shows pointer 
manipulation in a concrete language that hides pointers. In addition the project demonstrates the cost of operations that look free in list but are actually
O(n) in a linked list and vive versa, finally the project provides a CLI to practice on. The technologies used in the application go as followed, Language: python
std library: dataclasses, typing. For the setup and installization the project simply requires python 3.9 or newer. In order to run the project you can use the command:
"python3 task_manager.py" from the project directory. Since the program is pre-loaded ther is nothing to install. Some of the key functionalities shown in this project
are the unique functions such as: Add to front, Add to end, Display, Linear search, In-place reversak, count, Input validation.
My role and contribution to this project was to design and impliment the entire functionality. This includes the Node datclass as well as TaskList class
with all six operations, the menu-driven CLI, the input validation helpers, and finally the README.
Here is a sample output:

=========================================
   Task Manager (Python Linked List)
=========================================

----- Task Manager -----
1. Show all tasks
2. Add task to front
3. Add task to end
4. Remove task by name
5. Search for a task
6. Reverse task order
7. Show task count
0. Exit

Choice: 1
Tasks:
   0. [HIGH ] Write project README
   1. [MED  ] Refactor linked list module
   2. [LOW  ] Reply to emails
   3. [LOW  ] Plan weekend trip

Choice: 2
Task name: Review pull request
Priority (1=High, 2=Medium, 3=Low): 1
  Added 'Review pull request' to the front.

Choice: 6
  List reversed.
   0. [LOW  ] Plan weekend trip
   1. [LOW  ] Reply to emails
   2. [MED  ] Refactor linked list module
   3. [HIGH ] Write project README
   4. [HIGH ] Review pull request

Choice: 5
Task to find: Reply to emails
  Found 'Reply to emails' at position 1.
  
Reflection: The most difficult part of this project to impliment was the in-place reversal. For this implimentation I was forced to keep three pointers
in the head simulatanously and to preform the four steps in the exactly right order. Another challenge I had was learning about the different preformance
tradeoffs when comparing linked list and the built in list. Insertion at the head is O(1) here but O(n) for list.

Choice: 0
Goodbye!
