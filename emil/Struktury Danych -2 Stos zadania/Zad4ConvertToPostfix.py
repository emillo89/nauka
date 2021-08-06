class Conversion():
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        # tablica uzywana jako stos
        self.array = []
        # precedence setting - ustawienie pierwszenstwa

        self.output = []
        self.precedence = {'+':1, '-':1,'*':2, '/':2, '^':3}
        self.operators = set(['+', '-', '*', '/', '(', ')', '^'])


    def isEmpty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return '$'
    def push(self, op):
        self.top += 1
        self.array.append(op)


    # sprawdzenie znaku
    def isOperand(self,ch):
        return ch.isalpha()

    # sprawdzamy czy znak jest mniejszy niz znak na stosie
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <=b else False
        except KeyError:
            return False

    # glowna funkcja konwertujaca
    def infixToPostfix(self, exp):
        for i in exp:
            # jesli znak jest operand dodaj do outputu
            if i not in self.operators:
                self.output.append(i)
            # jesli znak jest '(' dodaj do stosu
            elif i == '(':
                self.push(i)
            #     jesli ktorys znak jest ) po znalezieniu ( usun ze stosu do outputu
            elif i == ')':
                while((not self.isEmpty()) and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
            # napotkano operator
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
        # wszystkie operatory sa na stosie
        while not self.isEmpty():
            self.output.append(self.pop())

        print(''.join(self.output))
        # print((self.output))


exp = '(2+4)*6-8'
obj = Conversion(len(exp))
a = obj.infixToPostfix(exp)

exp2 = '((2+4)/3+(14−3)*4)/2'
obj = Conversion(len(exp2))
b = obj.infixToPostfix(exp2)

cal1 = '24+6*8-'
cal2 = '24+3/143−*4+2/'
obj = Conversion(len(cal1))
# print(obj.expression_postFix(cal1))
# 27+3/14−34*+2/
obj2 = Conversion(len(cal2))
# print(obj.expression_postFix(cal2))





