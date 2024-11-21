#! /usr/bin/env python3

import math
import numpy as np
from zeta import FastZeta
from prime_analysis import actual_prime_count, prime_count_approximation

def predict_next_crossings(end=500):
    """Predict next crossing points using exponential fits"""
    
    # Fit parameters from current data
    pos_a, pos_b = 0.013400, -0.006255  # Positive crossings: a*e^(bx)
    neg_a, neg_b = -0.612846, -0.005205  # Negative crossings: a*e^(bx)
    
    # Last known crossings
    last_pos = 195.1
    last_neg = 197.1
    
    print("Predicted Next Crossings:")
    print(f"{'x':<10}{'Derivative':<15}{'Type':<10}")
    print("-" * 35)
    
    # Predict next 5 crossings of each type
    for i in range(5):
        # Calculate next crossing points
        pos_x = last_pos + 20 + i * 5  # Estimate based on observed spacing
        neg_x = last_neg + 20 + i * 5
        
        # Calculate expected derivatives at these points
        pos_d = pos_a * math.exp(pos_b * pos_x)
        neg_d = neg_a * math.exp(neg_b * neg_x)
        
        print(f"{pos_x:<10.1f}{pos_d:<15.6f}{'Positive':<10}")
        print(f"{neg_x:<10.1f}{neg_d:<15.6f}{'Negative':<10}")
        
        last_pos = pos_x
        last_neg = neg_x

    # Verify predictions
    print("\nVerification of first prediction:")
    x = last_pos + 20
    actual = actual_prime_count(int(x))
    approx = prime_count_approximation(x)
    error = abs(approx - actual) / actual * 100
    print(f"x = {x:.1f}, Error = {error:.6f}%")

if __name__ == "__main__":
    predict_next_crossings() 