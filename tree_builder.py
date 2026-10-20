
class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Each employee has a name and can have up to two direct reports.
    '''

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    The root represents the team lead.
    '''

    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        # Check whether the directory is empty
        if self.root is None:
            print("❌ Error: Add a team lead first.")
            return False

        # Validate the side
        side = side.lower()

        if side not in ("left", "right"):
            print("❌ Error: Side must be left or right.")
            return False

        # Start searching from the root
        if current_node is None:
            current_node = self.root

        # Recursive helper to find the manager
        def find_manager(node):
            if node is None:
                return None

            # Base case: manager found
            if node.name == manager_name:
                return node

            # Search the left subtree
            result = find_manager(node.left)

            if result is not None:
                return result

            # Search the right subtree
            return find_manager(node.right)

        # Find the manager recursively
        manager = find_manager(current_node)

        if manager is None:
            print(f"❌ Error: Manager '{manager_name}' not found.")
            return False

        # Add employee to the requested position
        if side == "left":
            if manager.left is None:
                manager.left = EmployeeNode(employee_name)
                print(f"✅ {employee_name} added to the LEFT of {manager_name}")
                return True
            else:
                print(f"❌ Error: LEFT side of {manager_name} is occupied.")
                return False

        elif side == "right":
            if manager.right is None:
                manager.right = EmployeeNode(employee_name)
                print(f"✅ {employee_name} added to the RIGHT of {manager_name}")
                return True
            else:
                print(f"❌ Error: RIGHT side of {manager_name} is occupied.")
                return False

    def print_tree(self, node=None, level=0):
        # Start at root during first call
        if node is None:
            if level == 0:
                node = self.root
            else:
                return

        # Check for an empty tree
        if node is None:
            print("The company directory is empty.")
            return

        # Display employee with indentation
        print("    " * level + "- " + node.name)

        # Recursively print left and right subtrees
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")

        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input(
                "Should this employee be on the LEFT or RIGHT of the manager? "
            )
            side = side.lower()

            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳 Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break

        else:
            print("❌ Invalid option. Try again.")


# Test your code here
def run_tests():
    print("\n========== TESTING COMPANY DIRECTORY ==========")

    test_tree = TeamTree()

    # Test 1: Create the team lead
    test_tree.root = EmployeeNode("Jordan")

    # Test 2: Add employees
    test_tree.insert("Jordan", "Riley", "left")
    test_tree.insert("Jordan", "Taylor", "right")
    test_tree.insert("Riley", "Morgan", "left")
    test_tree.insert("Riley", "Dana", "right")

    # Test 3: Print the tree
    print("\nTest Company Structure:")
    test_tree.print_tree()

    # Test 4: Check an occupied position
    print("\nTesting occupied position:")
    test_tree.insert("Jordan", "Alex", "left")

    # Test 5: Check nonexistent manager
    print("\nTesting nonexistent manager:")
    test_tree.insert("Unknown", "Sam", "right")

    # Test 6: Check invalid side
    print("\nTesting invalid side:")
    test_tree.insert("Jordan", "Chris", "middle")

    # Test 7: Verify structure
    assert test_tree.root.name == "Jordan"
    assert test_tree.root.left.name == "Riley"
    assert test_tree.root.right.name == "Taylor"
    assert test_tree.root.left.left.name == "Morgan"
    assert test_tree.root.left.right.name == "Dana"

    print("\n✅ All structure tests passed!")


# Run the tests and CLI
if __name__ == "__main__":
    run_tests()
    company_directory()
