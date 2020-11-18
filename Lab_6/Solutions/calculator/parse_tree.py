import math



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


operators = ['+', '-', '/', '*', '^', '!', 'sqrt', 'log', 'mod', '||']
priority = {'+': 0, '-': 0, '/': 1, '*': 1, '^': 2, 'mod': 3, '!': 3, 'sqrt': 3, 'log': 3, '(': -1, '|': -1}


def pretty_print(root: Node, lvl, path, is_right):
    if root is not None:
        for i in range(len(path) - 1):
            if path[i] == "l":
                print("|   ", end='')
            elif path[i] == "r":
                print("    ", end='')

        if lvl != 0:
            if is_right:
                print("└---", end='')
            else:
                print("|---", end='')

        print('[' + str(root.value) + ']')
        pretty_print(root.left, lvl + 1, path + "l", False)
        pretty_print(root.right, lvl + 1, path + "r", True)


def print_tree(root):
    pretty_print(root, 0, "", False)

def construct_node(elem, postfix):
    if elem in operators:
        tmp = Node(elem)
        tmp.right = postfix.pop()
        if elem != '!' and elem != 'sqrt' and elem != 'log' and elem != '||':
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

        elif ch == '|':
            stack.append(ch)
        elif ch == '||':
            while stack[-1] != '|':
                construct_node(stack.pop(), postfix)

            construct_node('||', postfix)
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

        token = root.value
        if token in operators:
            if token == "+":
                stack.append(float(stack.pop()) + float(stack.pop()))
            elif token == "-":
                stack.append(-float(stack.pop()) + float(stack.pop()))
            elif token == "*":
                stack.append(float(stack.pop()) * float(stack.pop()))
            elif token == "/":
                e1 = float(stack.pop())
                e2 = float(stack.pop())
                stack.append(e2/e1)
            elif token == "mod":
                e1 = float(stack.pop())
                e2 = float(stack.pop())
                stack.append(e2 % e1)
            elif token == "^":
                e1 = float(stack.pop())
                e2 = float(stack.pop())
                stack.append(pow(e2, e1))
            elif token == "!":
                stack.append(math.factorial(float(stack.pop())))
            elif token == "sqrt":
                stack.append(math.sqrt(float(stack.pop())))
            elif token == "log":
                stack.append(math.log(float(stack.pop()), 10))
            elif token == '||':
                stack.append(math.fabs(float(stack.pop())))
        else:
            stack.append(token)


def calculate_equation(root):
    result = []
    post_order_traveller(root, result)
    return result[0]


def main():
    equation = "( 6 mod 4 ) ^ 2"
    tree = infix_to_tree(equation)
    print(print_tree_return_string(tree))
    print(calculate_equation(tree))


if __name__ == "__main__":
   main()
