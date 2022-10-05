from Tasks.a0_my_stack import Stack


def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    stack = Stack()
    for i in brackets_row:
        if i == "(":
            stack.push(i)
        elif i == ")" and stack.peek() == "(":
            stack.pop()
        elif i == ")" and len(stack.data) == 0:
            return False

    return not stack.data

