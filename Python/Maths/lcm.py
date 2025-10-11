import math
def isPrime(n:int) -> bool:
    # Trial division. Not the best one, but the easiest one
    if n <= 1:
        return False
	# 2 is the only even prime number
    if n == 2:
        return True
    if n % 2 == 0:
	    return False
    for num in range(3, int(math.sqrt(n)) + 1):
        if n % num == 0:
            return False
    return True

def primeFactor(n:int) -> list[int]:
    current_factor = 2
    factors = []
    while n != 1:
        if n % current_factor == 0:
            factors.append(current_factor)
            n = n // current_factor
        else:
            current_factor += 1
            while not isPrime(current_factor):
                current_factor += 1
    return factors

def lcm(arr:list[int]) -> list[int]:
    lcm = 1
    prime_factors = dict()
    for n in arr:
        prime_factors[n] = primeFactor(n)

    for c in {b for a in prime_factors.values() for b in a}:
        lcm *= c ** max([e.count(c) for e in prime_factors.values()])
    return lcm

def main() -> None:
    user_numbers = input("Insert numbers for which you want to find the least common multiple: ").split()
    try:
        user_numbers = list(map(int, user_numbers))
    except:
        print("Only integers allowed. You need to insert integers space separated.")
        exit(1)
    for n in user_numbers:
        if n < 1:
            print("Values should be equal or greater than 1")
            exit(1)
    return lcm(user_numbers)

if __name__ == "__main__":
    print(main())
