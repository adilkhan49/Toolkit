import random

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
special2 = '!#$%&()*+,-./:;<=>?@'
alpha_count = 9
num_count = 4
special_count = 2

mypw = ""

for i in range(alpha_count):
    next_index = random.randrange(len(alphabet))
    mypw = mypw + alphabet[next_index]
for i in range(num_count):
    next_index = random.randrange(len(numbers))
    mypw = mypw + numbers[next_index]
for i in range(special_count):
    next_index = random.randrange(len(special2))
    mypw = mypw + special2[next_index]

def shuffle(string):
    l = list(string)
    random.shuffle(l)
    return ''.join(l)

mypw = shuffle(mypw)
print(mypw)
