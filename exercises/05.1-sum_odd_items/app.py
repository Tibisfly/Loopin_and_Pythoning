arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
new_arr = []

def sumOdds(num):
    new_arr = sum([num for num in arr if num % 2 != 0])
    return new_arr
  
print(sumOdds(arr))
