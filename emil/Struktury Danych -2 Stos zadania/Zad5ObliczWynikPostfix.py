class Conversion():
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        # tablica uzywana jako stos
        self.array = []
        # precedence setting - ustawienie pierwszenstwa

        self.output = []
        self.precedence = {'+':1, '-':1,'*':2, '/':2, '^':3}
        self.operators = set(['-', '+', '*', '/', '(', ')', '^'])


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
    # 1 sposob
    def PostFix_Eval(self, exp):
        for i in exp.split(' '):
            print(i)
            if i not in self.operators:
                self.push(i)
            else :
                var1 = self.pop()
                var2 = self.pop()

                self.push(str(eval(var2 + i + var1)))
            print(self.array)

        return int(self.pop())

    #2 sposob

    def PostFix_Eval_second(self, ab):
        for i in ab:

            # sprawdzamy czy to liczba
            try:
                self.push(int(i))
            # jesli nie jest to liczba to wykonujemy operację
            except ValueError:
                val1 = self.pop()
                val2 = self.pop()

            # wykonanie operacji
                switcher = {'+': val2 + val1, '-': val2 - val1, '*': val2 * val1, '/': val2 / val1, '^': val2 ** val1}
                self.push(switcher.get(i))
        return int(self.pop())

# 1 sposob
cal1 = '2 4 + 6 * 8 -'
cal2 = '20 10 + 75 45 - *'
cal3 = '2 4 + 3 / 14 3 - * 4 + 2 /'
obj2 = Conversion(len(cal2))
print(obj2.PostFix_Eval(cal2))

# do innego sposobu
cutting1 = cal1.split(' ')
cutting2 = cal2.split(' ')
cutting3 = cal3.split(' ')
obj = Conversion(len(cal3))
print(obj.PostFix_Eval_second(cutting1))





