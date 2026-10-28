class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''
    
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        is_initial_call = current_node is None
        if current_node is None:
            current_node = self.root

        if current_node is None:
            print(f"Error: manager '{manager_name}' does not exist.")
            return False

        side = side.lower()
        if side not in ("left", "right"):
            print("Error: side must be 'left' or 'right'.")
            return False

        if current_node.name == manager_name:
            if getattr(current_node, side) is not None:
                print(f"Error: the {side} side of '{manager_name}' is already occupied.")
            else:
                setattr(current_node, side, EmployeeNode(employee_name))
                print(f"{employee_name} added to the {side.upper()} of {manager_name}")
            return True

        if current_node.left is not None:
            if self.insert(manager_name, employee_name, side, current_node.left):
                return True

        if current_node.right is not None:
            if self.insert(manager_name, employee_name, side, current_node.right):
                return True

        if is_initial_call:
            print(f"Error: manager '{manager_name}' does not exist.")
        return False

    def print_tree(self, node=None, level=0):
        if node is None:
            if level == 0:
                node = self.root
            else:
                return

        if node is None:
            return

        print(f"{'  ' * level}- {node.name}")
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)

# Test your code here









# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\nTeam Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"{name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\nCurrent Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("Invalid option. Try again.")


'''
Design Memo

Recursive insertion starts at the root and checks whether the current employee
is the requested manager. If it is, the new employee is attached to the chosen
left or right pointer, provided that position is open. Otherwise, insertion
searches the left subtree and then the right subtree. Each recursive call makes
the same decision at a smaller part of the tree, so the search continues until
it finds the manager or has no child nodes left to check.

The main challenge in finding the right spot is distinguishing a manager that
has not been reached yet from a manager that does not exist. The search must
continue through both subtrees without inserting under the wrong employee.
Insertion also needs to check whether the requested side is already occupied,
and report invalid side names rather than silently placing the employee in a
different position. Keeping these cases separate helps prevent changes to the
wrong part of the reporting structure.

Trees are useful when data has a natural hierarchy or branching relationship.
An organization chart is one example: each employee can be connected to
reports below them, making it straightforward to display or search a particular
branch. File systems, website navigation, and decision processes can also be
represented as trees. Compared with a flat list, a tree makes parent-child
relationships explicit and allows recursive operations to process a branch
without treating every item as unrelated. The binary tree used here limits
each employee to two reports, which is suitable for this exercise but may not
fit every real organization; a general tree could support any number of reports.
'''