"""LC 150 - Evaluate RPN"""
def eval_rpn(tokens):
    stack = []
    for t in tokens:
        if t in '+-*/':
            b,a=stack.pop(),stack.pop()
            if t=='+': stack.append(a+b)
            elif t=='-': stack.append(a-b)
            elif t=='*': stack.append(a*b)
            else: stack.append(int(a/b))
        else: stack.append(int(t))
    return stack[0]
if __name__=="__main__":
    cases=[["2","1","+","3","*"],["4","13","5","/","+"],["10","6","9","3","+","-11","*","/","*","17","+","5","+"]]
    for tokens in cases:
        print(f"{tokens} -> {eval_rpn(tokens)}")
