a=98
b=0
try:
    print(a/b)
except  ZeroDivisionError as e:
    print("zeroDivisionError is :",e)
finally:
    print("completed")
