from lib.types import stack as _stack

def check(text):
    tmp      = ""
    stack    = _stack.Stack()
    balanced = tag = closing = False

    for symbol in text:
        if symbol is '<':
            tag = True
        elif tag:
            if symbol == '>':
                if tmp[0] == '/':
                    if stack.is_empty():
                        balanced = False
                    else:
                        balanced = tmp[1:] == stack.pop()
                else:
                    stack.push(tmp)
                tmp, tag = ("", False)
            else:
                tmp += symbol

    return balanced and stack.is_empty()