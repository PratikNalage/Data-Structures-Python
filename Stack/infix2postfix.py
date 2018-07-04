def prior(i):

    if i=='*' or i=='/' or i=='%':
        return 1
    elif i=='+' or i=='-':
        return 2
    elif i=='(':
        return 3

from stacks import Stack
exp = input("Enter an infix expression: ") + ')'
op = Stack()
postfix = []
op.push('(')
for i in exp:
    if i.isalpha():
        postfix.append(i)
    elif i=='(':
        op.push(i)
    elif i=='*' or i=='/' or i=='%' or i=='+' or i=='-':
        if prior(op.peek()) < prior(i):
            postfix.append(op.pop())
        op.push(i)
    elif i==')':
        while(op.peek() != '('):
            postfix.append(op.pop())
        temp = op.pop()


print("The postfix expression is: {}".format("".join(postfix)))
