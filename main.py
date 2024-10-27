try:
    a=int(input('Enter your age: '))
    if a%2==0:
        print('It is even')
    else:
        print('It is odd')
except:
    print('An error occured')