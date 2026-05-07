#!/usr/bin/env python3
"""
Test case generator for Two Sum problem solver
Generates large test cases for performance testing and GitHub Actions CI
Usage: python3 generate_test.py <num_elements> <target_sum> <output_file>
"""

import sys
import argparse

def generate_test_case(num_elements, target_sum=None, output_file=None):
    """
    Generate a test case with sequential integers 1..n
    This allows easy verification: indices i and j should have i+j = target if arranged properly
    """
    
    # Generate array: 1, 2, 3, ..., num_elements
    array = list(range(1, num_elements + 1))
    
    # If target not specified, use num_elements + 1 (will be found at indices 0 and num_elements-1)
    if target_sum is None:
        target_sum = num_elements + 1  # 1 + num_elements = num_elements + 1
    
    # Create output
    lines = [
        str(num_elements),  # array size
        ' '.join(map(str, array)),  # array elements
        str(target_sum)  # target sum
    ]
    
    output = '\n'.join(lines)
    
    if output_file:
        with open(output_file, 'w') as f:
            f.write(output)
        print(f"✓ Generated test case: {num_elements} elements, target={target_sum}")
        print(f"✓ Written to: {output_file}")
        print(f"✓ Expected result: indices 0 and {num_elements-1} (values 1 and {num_elements})")
    else:
        print(output)
    
    return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Generate test cases for Two Sum problem solver'
    )
    parser.add_argument('n', type=int, help='Number of array elements')
    parser.add_argument('-t', '--target', type=int, help='Target sum (default: n+1)')
    parser.add_argument('-o', '--output', help='Output file (default: stdout)')
    
    args = parser.parse_args()
    
    if args.n <= 0:
        print("Error: n must be positive", file=sys.stderr)
        sys.exit(1)
    
    generate_test_case(args.n, args.target, args.output)
