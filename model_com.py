x = complex(0,0)
y = complex(0,0)

def init(a,b,c,d):
    global x
    global y
    x = complex(a,b)
    y = complex(c,d)

def do_mult():
    return x*y

def do_sum():
    return x+y

def do_sub():
    return x-y

def do_dev():
    return x/y