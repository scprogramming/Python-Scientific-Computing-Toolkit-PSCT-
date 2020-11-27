from DataStructures.Stack import Stack


def precedence(c):
    if c == "+" or c == "-":
        return 1
    elif c == "*" or c == "/":
        return 2
    elif c == "^":
        return 3
    else:
        return -1


def isOperator(c):
    return c == "+" or c == "-" or c == "/" or c == "*" or c == "^"


def performOperation(numbers, operations):
    first = numbers.pop()
    if not numbers.isEmpty():
        second = numbers.pop()
    else:
        raise OverflowError
    operation = operations.pop()

    if operation == "+":
        return first + second
    elif operation == "-":
        return second - first
    elif operation == "*":
        return first * second
    elif operation == "/":
        if first == 0:
            raise ZeroDivisionError
        else:
            return second / first
    elif operation == "^":
        return second ** first

def evaluate(expression):
    numbers = Stack()
    operations = Stack()
    i = 0

    while i < len(expression):
        c = expression[i]

        if str.isdigit(c):
            num = 0
            while str.isdigit(c):
                num = num * 10 + int(c)
                i += 1
                if i < len(expression):
                    c = expression[i]
                else:
                    c = ''
            i -= 1
            numbers.push(num)
        elif c == "(":
            operations.push(c)
        elif c == ")":
            while operations.peek() != "(":
                output = performOperation(numbers, operations)
                numbers.push(output)

                if operations.isEmpty():
                    raise OverflowError

            operations.pop()
        elif isOperator(c):
            while not operations.isEmpty() and precedence(c) <= precedence(operations.peek()):
                output = performOperation(numbers, operations)
                numbers.push(output)
            operations.push(c)
        i += 1

    while not operations.isEmpty():
        output = performOperation(numbers,operations)
        numbers.push(output)

    return numbers.pop()

def fixMissingOperation(expression,variable):
    i = 0
    newExpression = ""

    while i < len(expression):
        c = expression[i]

        if i+1 < len(expression):
            next = expression[i+1]

            if next == variable and not isOperator(c):
                newExpression += c + "*"
            elif (not str.isdigit(next) and not isOperator(next) and next != "(" and next != ")") and not isOperator(c):
                newExpression += c + '*'
            else:
                newExpression += c
        else:
            newExpression += c

        i += 1

    return newExpression

def evaluateAt(expression,variable,value):
    expression = fixMissingOperation(expression,variable)
    expression = str.replace(expression,variable,str(value))
    return evaluate(expression)

