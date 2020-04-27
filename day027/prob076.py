def lcd(num1, num2):    
    a, b = max(num1, num2), min(num1, num2)
    while b != 0:
        a, b = b, a%b
        
    return num1 * num2 // a

def solution(arr):    
    l = lcd(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        l = lcd(l, arr[i])
        
    return l
