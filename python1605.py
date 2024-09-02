def eventOdd(x:int)->int:
    if(x%2 == 0):
        result = "even"
        return  result
    else:
        result = "Odd"
        return result

def callEventOdd():
    print("ใส่ตัวเลข : ",end="")
    x = int(input())
    ans = eventOdd(x)
    print(f"Number = {x} is {ans}")