

# import random

# print(dir(random))

# print(f"random number :{}")


#================================

# from random import randint

# print(f"random number :{randint(100,1000)}")


#+===============================

import random 
from  collections import Counter

options=["blue","white","black"]
results= random.choices(options,k=10)
print(f"random color : {Counter(results)}")
