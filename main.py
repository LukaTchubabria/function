def sums(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3


def myfun(*args):
    m = sum(args)/len(args)
    return m


def myfun2(*args):
    x = {args}
    return x

def myfun4(stri):
    for a in stri:
        if a == 'a' or a == 'e' or a == 'o' or a == 'u':
            print(f'{a} this is vowel')
        else:
            print(f'{a} this is Consonant')


def myfun5(x):
    if x % 2 == 0:
        return False
    else:
        return True



while True:
    x = input("num: ")
    x = float(x)
    myfun5(x)