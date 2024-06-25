#write your answer here
number = int(input("Enter your number: "))
count = 0
while (number>0):
    number = number//10
    count = count+1
print('Number of digits:', count)

def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = int(input('Enter a number: '))
print(factorial(n))
    if n==str:
print('Not a valid input'.isalpha())


Computers ={
  "Laptop1" : {"brand" : "DELL","OS" : "Windows"},
  "Laptop2" : {"brand" : "HP", "OS" : "Linux"},
  "Desktop" : {"brand" : "Apple","OS" : "Mac-OS"}
}
brand=[Computers["Laptop1"]["brand"],Computers["Laptop2"]["brand"],Computers["Desktop"]["brand"]]
OS=[Computers["Laptop1"]["OS"],Computers["Laptop2"]["OS"],Computers["Desktop"]["OS"]]
print(brand)
print(OS)

class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            t = target - num
            if t in d:
                return [d[t], i]
            d[num] = i
        return [] 