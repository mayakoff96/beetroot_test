def is_balanced(sequence):
    stack = []
    opening = {'(', '[', '{'}
    closing = {')', ']', '}'}
    matching = {'(': ')', '[': ']', '{': '}'}

    for i, char in enumerate(sequence):
        if char in opening:
            stack.append((char, i))
        elif char in closing:
            if len(stack) == 0:
                return False, char, i
            top, top_index = stack.pop()
            if matching[top] != char:
                return False, char, i

    if len(stack) == 0:
        return True, None, None
    else:
        top, top_index = stack.pop()
        return False, top, top_index


# Test the program
sequence1 = "({[()]})"
sequence2 = "({[()]})"
sequence3 = "({[()]}))"
sequence4 = "({[()]})"
sequence5 = "({[()]}"
sequence6 = "({[()]})"
sequence7 = "({[()]})"

print(is_balanced(sequence1)) 
print(is_balanced(sequence2))
print(is_balanced(sequence3))
print(is_balanced(sequence4))
print(is_balanced(sequence5))
print(is_balanced(sequence6))
print(is_balanced(sequence7))
