import turtle

def tree(branchLen,t):
    if branchLen > 3:
        t.forward(branchLen)
        t.right(30)
        tree(branchLen-15,t)
        
        t.left(60)
        tree(branchLen-15,t)
        t.right(30)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(100,t)

main()
