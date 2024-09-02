def funAdd(num1:int, num2: int,) -> int:
    """Add two number"""
    num3 = num1 + num2
    return num3
def resultAdd():
    num1,num2=5,15
    title = "The addition of"
    ans = funAdd(num1,num2)
    print(f" {title} {num1} + {num2} = {ans}")