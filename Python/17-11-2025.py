# write a function which can return sum of any no. of value
#using arbitary 
def sum(*args):
    s =0
    for num in args:
        s+=num
    return s

print(s)

    