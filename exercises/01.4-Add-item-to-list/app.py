#Remember import random function here:
import random 

my_list = [4,5,734,43,45]

index = list(range(0,10))



for i in range(0,10):
    my_random_list = random.randint(0, 10)
    my_list.append(my_random_list)
print(my_list)