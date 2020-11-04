import sys

class Node:

    # Constructor to create a node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


operators = ['+', '-', '/', '*']
priority = {'+': 0, '-': 0, '/': 1, '*': 1, '^': 2, '(': -1}


def pretty_print(root: Node, lvl, path, isRight):
    if root is not None:
        for i in range(len(path)-1):
            if path[i] == "l":
                print("|   ", end = '')
            elif path[i] == "r":
                print("    ", end='')

        if (lvl != 0):
            if (isRight):
                print("└---", end='')
            else:
                print("|---", end='')

        print('['+str(root.value)+']')
        pretty_print(root.left, lvl + 1, path+"l", False)
        pretty_print(root.right, lvl + 1, path+"r", True)


def print_tree(root):
    pretty_print(root, 0, "", False)


def construct_node(elem, postfix):
    if elem in operators:
        tmp = Node(elem)
        tmp.right = postfix.pop()
        tmp.left = postfix.pop()
        postfix.append(tmp)


def infix_to_tree(infix):
    infix_array = infix.split()
    stack = []
    postfix = []

    infix_array.insert(0, '(')
    infix_array.append(')')

    for ch in infix_array:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack[-1] != '(':
                construct_node(stack.pop(), postfix)
            stack.pop()
        elif ch in operators:
            while priority[ch] <= priority[str(stack[-1])]:
                construct_node(stack.pop(), postfix)
            stack.append(ch)
        else:
            postfix.append(Node(ch))

    for e in stack:
        construct_node(e, postfix)

    return postfix[0]


def post_order_traveller(root, stack):
    if root is not None:
        post_order_traveller(root.left, stack)
        post_order_traveller(root.right, stack)
        if root.value in operators:
            if root.value == "+":
                stack.append(float(stack.pop()) + float(stack.pop()))
            if root.value == "-":
                stack.append(-float(stack.pop()) + float(stack.pop()))
            if root.value == "*":
                stack.append(float(stack.pop()) * float(stack.pop()))
            if root.value == "/":
                stack.append(1/float(stack.pop()) * float(stack.pop()))
        else:
            stack.append(root.value)


def calculate_equation(root):
    result = []
    post_order_traveller(root, result)
    return result[0]

def main(args):
    #equation = input("Enter the equation: ")
    tree = infix_to_tree(args[1])
    print(args[1]+"= "+str(calculate_equation(tree)))
    if '-t' in args:
        print('')
        print_tree(tree)
        print('')


if __name__ == "__main__":
    main(sys.argv)
