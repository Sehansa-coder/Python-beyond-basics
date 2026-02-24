# This program shows how to filter prime numbers from a list

numbers=[2,3,4,5,6,7,8,9,10,11]

# a prime number is divisible only by 1 and itself
# we check if there are no divisors between 2 and num-1

primes=[]

for num in numbers:
    if num>1:   # skip 0 and 1
        is_prime=True
        for i in range(2,num):   # check divisibility
            if num%i==0:
                is_prime=False
                break      # no need to check further
        if is_prime:
            primes.append(num)

print(primes)

# sample output:
# [2, 3, 5, 7, 11]