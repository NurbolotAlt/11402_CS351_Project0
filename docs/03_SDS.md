# Software Design Specification (SDS)

## 1. Introduction

### 1.1 Purpose

This Software Design Specification details the architectural and implementation design for the Two Sum Problem Solver, including component architecture, algorithms, data structures, and design patterns used in the C++20 implementation.

### 1.2 Scope

This document covers the design of both algorithmic implementations, the I/O system, testing framework, and the main program flow. It excludes UI design and deployment infrastructure.

## 2. System Architecture

### 2.1 Overview

The system follows a modular, function-based architecture with clear separation between:
- Algorithm implementations (TwoSumArray, TwoSumHashTable)
- I/O handling (input parsing, output formatting)
- Test harness (built-in test cases and validation)
- Main program flow

### 2.2 Components

| Component | Purpose | Responsibility |
|-----------|---------|----------------|
| TwoSumArray | Brute-force solver | O(n²) solution using nested loops |
| TwoSumHashTable | Optimized solver | O(n) solution using unordered_map |
| Input Handler | Parse stdin | Read array size, elements, target |
| Output Handler | Format results | Display indices or test results |
| Test Harness | Validate solutions | Execute and verify predefined test cases |
| Main Program | Orchestrate flow | Coordinate components, handle modes |

### 2.3 Interfaces

**Algorithm Interface**:
```cpp
vector<int> TwoSum(const vector<int>& nums, int target);
// Input: vector of integers, target sum
// Output: vector with two indices [i, j] or empty vector if no solution
```

**Program Modes**:
- Built-in test mode: Detect terminal input, auto-execute test cases
- Interactive mode: Read from stdin when available

## 3. Detailed Design

### 3.1 Data Structures

**Primary Data Structures**:
- `vector<int>`: Dynamic array for input numbers and index pairs
- `unordered_map<int, int>`: Hash table mapping value to index for O(n) solution
- `pair<vector<int>, int>`: Test case structure (array, target)

### 3.2 Module Specifications

**Module: TwoSumArray**
```
Function: TwoSumArray(const vector<int>& nums, int target)
Time Complexity: O(n²)
Space Complexity: O(1)
Algorithm: Nested loop comparing all pairs
Constraints: Works with all integer values, including negatives
```

**Module: TwoSumHashTable**
```
Function: TwoSumHashTable(const vector<int>& nums, int target)
Time Complexity: O(n)
Space Complexity: O(n)
Algorithm: Single pass with hash table lookup
Constraints: Hash table size limited by available memory
```

**Module: Input Processing**
```
Reads three lines from stdin:
  Line 1: Array size (int)
  Line 2: Space-separated integers
  Line 3: Target sum (int)
Error handling: Validates size, detects EOF
```

### 3.3 Algorithms

**Brute-Force Algorithm (O(n²))**:
```
1. For each element i from 0 to n-1:
   2. For each element j from i+1 to n-1:
      3. If nums[i] + nums[j] == target:
         4. Return {i, j}
5. Return empty vector
```

**Hash-Table Algorithm (O(n))**:
```
1. Create empty hash map
2. For each element i from 0 to n-1:
   3. Calculate complement = target - nums[i]
   4. If complement exists in map:
      5. Return {map[complement], i}
   6. Add nums[i] -> i to map
7. Return empty vector
```

## 4. Design Patterns

- **Function-based Design**: Clear, testable algorithm functions
- **Strategy Pattern**: Two different algorithm implementations selectable at runtime
- **Standard Library Usage**: Leverage C++ STL (vector, unordered_map) for reliability
- **RAII Principles**: Automatic resource management through standard containers

## 5. Database Design

No database required. All data is in-memory with test cases hardcoded in the application.
