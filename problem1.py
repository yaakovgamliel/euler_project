# https://projecteuler.net/problem=1

num = []

for i in range(1,1000):
    num.append(i)

def check_divisibles_sum(seq=[]):
    divs = []
    for i in seq:
        if(i % 3 == 0 or i % 5 ==0):
            divs.append(i)

    print(divs)
    return divs

def num_sum(nums=[]):
    sum = 0
    for n in nums:
        sum += n
    
    print(sum)
    return sum

# Or even simpler
def check_sum(nums=[]):
    sum = 0
    for i in nums:
        if(i % 3 == 0 or i % 5 ==0):
            sum += i

    return sum

num_sum(check_divisibles_sum(num))
print(check_sum(num))
