#! /usr/bin/env python3

import math
from zeta import FastZeta
from typing import List

def is_prime(n: int) -> bool:
    """Simple primality test"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def actual_prime_count(x: int) -> int:
    """Count actual number of primes up to x"""
    return sum(1 for n in range(2, x + 1) if is_prime(n))

def prime_count_approximation(x: float) -> float:
    """Approximate number of primes up to x using zeta function"""
    if x < 2:
        return 0
    # Li(x) approximation using zeta
    return x / math.log(x) * (1 + 1/math.log(x))

def analyze_prime_distribution(start: int = 10, end: int = 100, step: int = 10):
    """Compare actual vs approximated prime counts"""
    print(f"{'x':<8}{'Actual':<10}{'Approx':<10}{'Error %':<10}")
    print("-" * 38)
    
    for x in range(start, end + 1, step):
        actual = actual_prime_count(x)
        approx = prime_count_approximation(x)
        error = abs(approx - actual) / actual * 100
        
        print(f"{x:<8}{actual:<10}{approx:<10.2f}{error:<10.2f}")

if __name__ == "__main__":
    analyze_prime_distribution(10, 1000, 100) 