def psp(brackets_string):
    open_brackets = 0
    close_brackets = 0

    for bracket in brackets_string:
        if bracket == '(':
            open_brackets += 1
        elif bracket == ')':
            if open_brackets == 0:
                close_brackets += 1
            else:
                open_brackets -= 1

    return open_brackets + close_brackets

def nearest_smaller(arr):
    n = len(arr)
    result = [-1] * n
    
    stack = []
    
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            result[stack.pop()] = i
        
        stack.append(i)
    
    return result