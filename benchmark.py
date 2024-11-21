#! /usr/bin/env python3

import time
import cmath
import math
import numpy as np
from zeta import FastZeta

def safe_traditional_zeta(s, max_terms=100):
    """Safe version of traditional zeta to avoid overflow"""
    try:
        return FastZeta.zeta(s, 'traditional')
    except OverflowError:
        # Use fewer terms for large values
        total = 0
        for n in range(1, max_terms + 1):
            try:
                total += 1 / (n ** s)
            except OverflowError:
                break
        return abs(total)

def benchmark_extended_range(x_values=[25.0, 30.0, 35.0, 40.0], iterations=100):
    methods = {
        "FastZeta": lambda x: FastZeta.zeta(x, 'fast'),
        "Safe Traditional": safe_traditional_zeta,
        "Schönhage": lambda x: sum(1/(n**x) for n in range(1, 50))  # Limited terms
    }
    
    print(f"Extended Range Analysis ({iterations} iterations)")
    print(f"{'x':<8}{'Method':<15}{'Time (ms)':<12}{'Result':<15}{'Error %':<10}")
    print("-" * 60)
    
    for x in x_values:
        # Use FastZeta as reference for large values
        reference = FastZeta.zeta(x, 'fast')
        
        for method_name, method in methods.items():
            start = time.time()
            result = 0
            
            try:
                for _ in range(iterations):
                    result = abs(method(x))
                    
                exec_time = (time.time() - start) * 1000
                error = abs(result - reference)/reference * 100
                
                print(f"{x:<8}{method_name:<15}{exec_time:<12.3f}{result:<15.6f}{error:<10.6f}")
            except (OverflowError, ZeroDivisionError) as e:
                print(f"{x:<8}{method_name:<15}{'OVERFLOW':<12}{'N/A':<15}{'N/A':<10}")
        print()

def benchmark_stability(base_x=25.0, delta=0.0001, iterations=100):
    """Test numerical stability by looking at tiny changes in input"""
    methods = {
        "FastZeta": lambda x: FastZeta.zeta(x, 'fast'),
        "Safe Traditional": safe_traditional_zeta,
        "Schönhage": lambda x: sum(1/(n**x) for n in range(1, 50))
    }
    
    print(f"Numerical Stability Analysis ({iterations} iterations)")
    print(f"Testing x = {base_x} vs x = {base_x + delta}")
    print(f"{'Method':<15}{'Base':<15}{'Base+Δ':<15}{'Δ Result':<15}")
    print("-" * 60)
    
    for method_name, method in methods.items():
        try:
            result1 = abs(method(base_x))
            result2 = abs(method(base_x + delta))
            diff = abs(result2 - result1)
            
            print(f"{method_name:<15}{result1:<15.12f}{result2:<15.12f}{diff:<15.12f}")
        except (OverflowError, ZeroDivisionError):
            print(f"{method_name:<15}{'ERROR':<15}{'ERROR':<15}{'N/A':<15}")
    
def benchmark_precision(x_value=25.0, iterations=100):
    """Compare methods at different precision levels"""
    methods = {
        "FastZeta": lambda x: FastZeta.zeta(x, 'fast'),
        "Safe Traditional": safe_traditional_zeta,
        "Schönhage": lambda x: sum(1/(n**x) for n in range(1, 50))
    }
    
    print(f"Precision Analysis at x={x_value} ({iterations} iterations)")
    print(f"{'Method':<15}{'Result':<25}{'Digits':<10}{'Time (ms)':<12}")
    print("-" * 62)
    
    for method_name, method in methods.items():
        start = time.time()
        result = 0
        
        for _ in range(iterations):
            result = abs(method(x_value))
            
        exec_time = (time.time() - start) * 1000
        
        # Count significant digits
        str_result = f"{result:.16f}"
        significant = len(str_result.rstrip('0').split('.')[1])
        
        print(f"{method_name:<15}{str_result:<25}{significant:<10}{exec_time:<12.3f}")

if __name__ == "__main__":
    benchmark_extended_range()
    benchmark_stability()
    benchmark_precision() 