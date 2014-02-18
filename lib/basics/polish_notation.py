from lib.types import stack

class _Expression(object):
    PRECEDENCE  = { '+': 1, '-': 1, '*': 2, '/': 2, '**': 2 }
    OPERATIONS  = PRECEDENCE.keys()

    class Operation(object):
        def __init__(self, symbol, precedence):
            self.symbol     = symbol
            self.precedence = precedence

        def __str__(self):
            return self.symbol

        def __eq__(self, other):
            if type(self) == type(other):
                return self.symbol == other.symbol
            elif type(other) == str:
                return self.symbol == other
            else:
                return False

        def __lt__(self, other):
            if type(self) == type(other):
                return self.precedence < other.precedence
            else:
                return False

        def __le__(self, other):
            if type(self) == type(other):
                return self.precedence <= other.precedence
            else:
                return False

        def __gt__(self, other):
            if type(self) == type(other):
                return self.precedence > other.precedence
            else:
                return False

        def __ge__(self, other):
            if type(self) == type(other):
                return self.precedence >= other.precedence
            else:
                return False

class _Evaluator(_Expression):
    def __init__(self, expression):
        self.expression = expression.split()
        self.stack      = stack.Stack()

    def calculate(self):
        raise NotImplemented

    def process_operation(self, left, right, operation):
        if operation == '*':
            return left * right
        elif operation == '+':
            return left + right
        elif operation == '-':
            return left - right
        elif operation == '/':
            return left / right
        elif operation == '**':
            return left ** right
        else:
            print ("Operation '{}' is not defined".format(operation))
            raise BaseException

class ExpressionConverter(_Expression):
    def __init__(self, expression):
        self.expression = expression.split()
        self.operations = stack.Stack()

    def convert(self):
        raise NotImplemented

class PostfixConverter(ExpressionConverter):
    parentheses = ('(', ')')

    def compare_operations(self, prev_operation, operation):
        return prev_operation and prev_operation >= operation

    def convert(self):
        result = []

        for token in self.expression:
            if token == self.__class__.parentheses[0]:
                self.operations.push(token)
            elif token == self.__class__.parentheses[1]:
                last_operand = self.operations.pop()                
                while last_operand != self.__class__.parentheses[0]:
                    result.append(last_operand.__str__())
                    last_operand = self.operations.pop()

            elif token in self.OPERATIONS:
                operation      = self.Operation(token, self.PRECEDENCE[token])
                prev_operation = self.operations.peek()
    
                if self.compare_operations(prev_operation, operation):
                    result.append(self.operations.pop().__str__())

                self.operations.push(operation)
            else:
                result.append(token)

        while not self.operations.is_empty():
            result.append(self.operations.pop().__str__())

        return ' '.join(result)

class PostfixEvaluator(_Evaluator):
    def calculate(self):
        for token in self.expression:
            if token in self.OPERATIONS:
                if self.stack.size() < 2:
                    print ('Error: not enough tokens in stack.')
                    raise BaseException

                right, left = map(int, self.stack.pop(2))
                calculation = self.process_operation(left, right, token)

                self.stack.push(calculation)
            else:
                self.stack.push(token)

        return int(self.stack.pop())

class PrefixConverter(PostfixConverter):
    parentheses = (')', '(')

    def compare_operations(self, prev_operation, operation):
        return prev_operation and prev_operation > operation

    def convert(self): 
        self.expression = self.expression[::-1]
        return super().convert()[::-1]

class PrefixEvaluator(PostfixEvaluator):
    def calculate(self):
        for token in self.expression[::-1]:
            if token in self.OPERATIONS:
                if self.stack.size() < 2:
                    print ('Error: not enough tokens in stack.')
                    raise BaseException

                left, right = map(int, self.stack.pop(2))
                calculation = self.process_operation(left, right, token)

                self.stack.push(calculation)
            else:
                self.stack.push(token)

        return int(self.stack.pop())
