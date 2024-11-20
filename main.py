# def checkno(num1,num2):
#     if ((num1^num2)!=0):
#         print("numbers are not equal")
#     else:
#         print("numbers are equal")
    
# num1 = int(input("Enter num1:"))
# num2 = int(input("Enter num2:"))

# checkno(num1, num2)









# def oddoccur(arr):
#     res=0
#     for element in arr:
#         res=res^element
#     return res

# arr=[]
# n=int(input("Enter the size of arrays: "))

# while(n):
#     num=int(input("Enter the number of elements:"))
#     arr.append(num)
#     n-=1
# print("The number which appears an odd number is: ",oddoccur(arr))




def twoc(arr,size):
    xorof2=arr[0]
    x=0
    y=0
    setbit=0
    for i in range(1,size):
        xorof2=xorof2^arr[i]
        
    setbit=xorof2&~(xorof2-1)
    
    
    for i in range(size):
        if (arr[i]&setbit):
            x=x^arr[i]
            
        else:
            y=y^arr[i]
            
    print("two odd elements are:",x,"&",y)
    
arr=[]
arr_size=int(input("Enter the size of the array:"))

for i in range(0,arr_size):
    z=int(input("Enter element:"))
    arr.append(z)
    
print("Two odd elements are:")

twoc(arr,arr_size)