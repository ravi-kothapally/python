try:
    a=10
    print(a)
    raise ValueError('pora')
except ValueError as e:
    print(e)
else:
    print(a*a)
    raise
finally:
    print('erbu')
    
