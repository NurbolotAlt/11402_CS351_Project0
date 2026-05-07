# Test Plan

## 1. Introduction

### 1.1 Purpose

This Test Plan defines the comprehensive testing strategy for the Two Sum Problem Solver, ensuring both algorithm implementations function correctly across diverse input scenarios and edge cases.

### 1.2 Scope

Testing covers:
- Functional correctness of both TwoSumArray and TwoSumHashTable algorithms
- Edge cases (empty arrays, single elements, negative numbers, duplicates)
- Input validation and error handling
- Built-in test harness execution
- Cross-platform compilation and execution

## 2. Test Strategy

### 2.1 Testing Types

1. **Unit Tests**: Test individual algorithm functions in isolation
2. **Integration Tests**: Test interaction between input handler and algorithms
3. **System Tests**: Test complete program flow with stdin/stdout
4. **Regression Tests**: Verify consistency between two algorithms
5. **Edge Case Tests**: Test boundary conditions and special scenarios
6. **Performance Tests**: Compare execution times for O(n²) vs O(n)

### 2.2 Testing Approach

- **Built-in Test Harness**: Execute predefined test cases when program runs without stdin
- **Manual Testing**: Test with custom stdin inputs
- **Comparative Testing**: Verify both algorithms produce identical results
- **Automated CI/CD**: GitHub Actions builds and runs tests on every commit

## 3. Test Cases

### 3.1 Unit Tests - TwoSumArray

| Test ID | Input | Expected Output | Status |
|---------|-------|-----------------|--------|
| UT-001 | nums=[2,7,11,15], target=9 | [0,1] | ✓ |
| UT-002 | nums=[3,2,4], target=6 | [1,2] | ✓ |
| UT-003 | nums=[3,3], target=6 | [0,1] | ✓ |
| UT-004 | nums=[], target=0 | [] | ✓ |
| UT-005 | nums=[1], target=2 | [] | ✓ |
| UT-006 | nums=[1,2], target=5 | [] | ✓ |
| UT-007 | nums=[-1,-2,-3], target=-5 | [0,1] or [1,2] | ✓ |
| UT-008 | nums=[-2,0,2], target=0 | [0,2] | ✓ |

### 3.2 Unit Tests - TwoSumHashTable

| Test ID | Input | Expected Output | Status |
|---------|-------|-----------------|--------|
| UT-009 | nums=[2,7,11,15], target=9 | [0,1] | ✓ |
| UT-010 | nums=[3,2,4], target=6 | [1,2] | ✓ |
| UT-011 | nums=[3,3], target=6 | [0,1] | ✓ |
| UT-012 | nums=[], target=0 | [] | ✓ |
| UT-013 | nums=[1], target=2 | [] | ✓ |
| UT-014 | nums=[1,2], target=5 | [] | ✓ |
| UT-015 | nums=[-1,-2,-3], target=-5 | [0,1] or [1,2] | ✓ |
| UT-016 | nums=[-2,0,2], target=0 | [0,2] | ✓ |

### 3.3 Integration Tests

| Test ID | Scenario | Expected Behavior |
|---------|----------|-------------------|
| IT-001 | Valid input from stdin | Both algorithms return same result |
| IT-002 | Multiple test cases | Program handles consecutive inputs |
| IT-003 | EOF detection | Program correctly detects end-of-input |
| IT-004 | Empty stdin | Built-in tests execute automatically |
| IT-005 | Terminal detection | Correctly identifies TTY vs piped input |

### 3.4 System Tests

| Test ID | Input | Expected Result |
|---------|-------|----------|
| ST-001 | Built-in test mode | All tests pass, formatted output |
| ST-002 | stdin mode with valid data | Correct indices printed |
| ST-003 | stdin mode with no solution | Empty line printed |
| ST-004 | Cross-platform compilation | Builds on Windows, Linux, macOS |

## 4. Test Schedule

- **Phase 1**: Unit tests during implementation
- **Phase 2**: Integration tests during assembly
- **Phase 3**: System tests before release
- **Phase 4**: Continuous testing via CI/CD on every commit

## 5. Test Resources

- C++ Compiler (g++ or MSVC)
- Terminal/Command prompt
- GitHub Actions CI environment
- Test input data files (optional)

## 6. Pass/Fail Criteria

**Pass Criteria**:
- All test cases return expected indices
- Both algorithms produce identical results for same input
- Program handles edge cases without crashing
- Output format matches specification
- Compilation with no warnings
- CI/CD pipeline builds and runs successfully

**Fail Criteria**:
- Algorithm returns incorrect indices
- Algorithms produce different results
- Program crashes on edge cases
- Compilation errors or warnings
- Output format incorrect
- CI/CD pipeline fails
