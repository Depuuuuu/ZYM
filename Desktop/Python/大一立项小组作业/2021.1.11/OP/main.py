if __name__ == '__main__':
    from classs import *

    stack = ArrayStack()
    a = input()
    for i in a:
        if i == '+' or i == '-' or i == '*' or i == '/':
            number1 = stack.pop()
            number2 = stack.pop()
            if i == '+':
                stack.push(number1 + number2)
            elif i == '-':
                stack.push(number2 - number1)
            elif i == '*':
                stack.push(number1 * number2)
            elif i == '/':
                stack.push(number2 / number1)
        else:
            stack.push(int(i))
    print(stack)
