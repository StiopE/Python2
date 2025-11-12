def triangle1(size):
    for i in range(1, size):
        print('* '*i)

def triangle2(size):
    for i in range(size,0,-1):
        print('* '*i)

def triangle3(size):
    for i in range(size,0,-1):
        print(' '*i + '*'*(size-i))


def tree1(size):
    for i in range(size,0,-1):
        print(' '*i + '* '*(size-i))

def tree2(size):
    print("        *")
    for i in range(1,size,1):
        print(' '*(size-i),'*'+ '  '*i+'*')
        if i == 5:
            print(' * * * * * * * *')

def sand_timer():
    sums = 0
    for i in range(10, 0, -1):
        print(' '*sums + '* '*i)
        sums+=1
    sums2 = 8
    for i in range(2,11, 1):
        print(' '*sums2 + '* '*i)
        sums2-=1

def portal():
    sums3 = 5
    for i in range(1,6, 1):
        print(' '*sums3 + '* '*i)
        sums3-=1
    sums4 = 4   
    for i in range(2,7,1):
        print(' '*i + '* '*sums4)
        sums4-=1


        

