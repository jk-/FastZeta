#! /usr/bin/env python3
import unittest
from zeta import FastZeta

class TestFastZeta(unittest.TestCase):
    def test_accuracy(self):
        """Test accuracy of fast approximation"""
        test_points = [5.0, 10.0, 15.0, 20.0]
        max_error = 0.1  # Allow up to 0.1% error
        
        for x in test_points:
            fast = FastZeta.zeta(x, 'fast')
            traditional = FastZeta.zeta(x, 'traditional')
            error = abs(fast - traditional) / traditional * 100
            
            self.assertLess(error, max_error, 
                f"Error at x={x} is {error}%, which exceeds {max_error}%")
    
    def test_convergence(self):
        """Test that values converge to 1"""
        x = 20.0
        result = FastZeta.zeta(x, 'fast')
        self.assertAlmostEqual(result, 1.0, places=5)
    
    def test_complex_values(self):
        """Test behavior with complex inputs"""
        s = complex(10, 1)
        fast = FastZeta.zeta(s, 'fast')
        traditional = FastZeta.zeta(s, 'traditional')
        error = abs(fast - traditional) / abs(traditional) * 100
        
        self.assertLess(error, 0.1)
    
    def test_error_estimates(self):
        """Test that error estimates are conservative"""
        test_points = [5.0, 10.0, 15.0]
        
        for x in test_points:
            fast = FastZeta.zeta(x, 'fast')
            traditional = FastZeta.zeta(x, 'traditional')
            actual_error = abs(fast - traditional) / traditional * 100
            estimated_error = FastZeta.error_estimate(x)
            
            self.assertGreater(estimated_error, actual_error,
                f"Error estimate at x={x} is not conservative")

if __name__ == '__main__':
    unittest.main()
   
