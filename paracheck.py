def balance_check(s):
    stack = []
    dict = {'(':')', '[':']', '{':'}'}
    for c in s:
        if c in dict:
            stack.append(dict[c])
        elif c in stack[-1]:
            stack.pop()
        else:
            return False
    return len(stack) == 0

s = '[](){([[[]]])}'
# s = '()(){]}'
# s = '()'

print(balance_check(s))