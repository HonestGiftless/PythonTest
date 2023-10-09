def is_ip(lst):
    result = list()
    for i in lst:
        if i.isdigit() and 0 <= int(i) <= 255:
            result.append(True)
        else:
            result.append(False)

    return result

def is_interesting(lst):
    result = list()
    for i in lst:
        if '0' in str(i):
            continue
        else:
            counter = 0
            for j in str(i):
                if i % int(j) == 0:
                    counter += 1
            if counter == len(str(i)):
                result.append(i)

    return result

def pretty_print(data, side='-', delimiter='|'):
    text = ''
    for i in range(len(data)):
        if i != len(data) - 1:
            text += f'{delimiter} {data[i]} '
        else:
            text += f'{delimiter} {data[i]} {delimiter}'
    
    border_text = ' ' + side*(len(text)-2) + ' '

    print(border_text)
    print(text)
    print(border_text)

def concat(*args, sep=' '):
    result = ''
    if len(args) > 1:
        for i in range(len(args)):
            if i == 0:
                result += str(args[i]) + sep
            elif i == len(args) - 1:
                result += str(args[i])
            else:
                result += str(args[i]) + sep
    else:
        result = args[0]
    
    return result

def arithmetic_operation(action):
     return {'+': lambda x, y: x+y, '-': lambda x, y: x-y, '*': lambda x, y: x*y, '/': lambda x, y: x/y}[action]