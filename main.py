""" 
practice decorator:
It comes from the classic decorator pattern in OOP, python turns it into an @anotation (check abc package)
*Caution:  Don't over use decorators, that will impact readability of the codes
*Better use for : 1. wrap event handlers 2. wrap routes like Flask does 3. wrap lower level functions such as logging, error handling or benchmarking, currying(functools.partial)
It solve cross-cutting concerns, decoupling some behaviors (cache or sync e.g) from modeled object

NOTE: TODO we also can implement decorators using class with `__init__` and `__call__` method (`__init__` for parameterizing and `__call__` for applying deco to func of class)
And in addition we can decorate not only functions but classes as well

NOTE: Any relationship with context Manager
*Types: function, class or method decorators


"""
import math
import time
import functools
from abc import ABC, abstractmethod

def timer(func):

    @functools.wraps(func)
    def wrapper( *args, **kwargs ):
        now = time.time()
        value = func(*args, **kwargs)
        then = time.time()
        elapsed = then - now
        print(f'time used: {elapsed}')
        return value
    return wrapper

def is_prime(num: int) -> bool:
    if num < 2:
        return False    
    for x in range(2, int(math.sqrt(num)) +1):
        if num % x == 0 :
            return False
    return True

# a one line solution for is_prime
def is_prime_one_line(num: int) -> bool:
    return num >1  and all( num % i for i in range(2,  int(num ** 0.5) + 1 ) ) 


@timer
def count_prime(num: int) -> int:
    if num < 1 or num == 1:
        return 0
    count = 0
    for i in range(2, num+1):
        if is_prime_one_line(i):
            count += 1

    return count

# create cache decorator - not calling func(*args) if the result is cached
# use decorator factory to create the decorator dynamically with params. A decorator function shouldn't have params other than the func
def cached_factory(msg:list[str]):
    # decorator function
    def cached(func):
        cached_data = {}

        @functools.wraps(func)
        def cached_dec(*args):
            try:
                # print(msg[0])
                return cached_data[args] # args=(4,)
            except KeyError:
                print(msg)
                cached_data[args] = ret = func(*args) # ret = 16
                return ret
        return cached_dec
    return cached

@cached_factory("Welcome, newcommer!")
def do_something(x):
    print(f'calling {x}')
    return x*x


def main():
    # print(f'total is {count_prime(100000)}')
    value = do_something(4)
    value1 = do_something(4)
    # value2 = do_something(5)
    # value3 = do_something(6)

    print(value, value1)
    # print(value2, value3)

if __name__ == "__main__":
    main()
    
            
        

        
