def Q(n):
    try:
        if n>0 and n<3:
           return 1
        elif n<0:
           return 'Invalid'
        else:
           return Q ( n - Q ( n - 1 ) ) + Q ( n - Q ( n - 2 ) )
    except:return "Enter an INTEGER value!"
print(Q(int(input())))
