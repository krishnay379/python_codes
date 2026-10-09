import random
friends = [ "Krishna", "Ram","Swapnil","Surywansh","Lakshya","Samarth","Arpit"]
# 1st method
print(random.choice(friends))

# 2nd method
random_index=(random.randint(0,4))
print(friends[random_index])