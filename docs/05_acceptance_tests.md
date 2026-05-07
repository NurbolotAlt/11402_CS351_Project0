# Acceptance Tests

## Purpose

Acceptance testing validates that the Two Sum Problem Solver meets all specified requirements and works correctly for end users. These tests verify both the functional correctness and usability of the application.

## Test Cases

### Test Case 1: Basic Two Sum with Valid Solution

**ID:** AT-001  
**Description:** Program finds two numbers that sum to target in a basic array  
**Preconditions:** Program compiled and executable available  
**Steps:**
1. Run program: `./main`
2. Provide input: array size=4, array=[2,7,11,15], target=9
3. Observe output

**Expected Result:** Output shows indices "0 1" (representing values 2 and 7)  
**Acceptance Criteria:** Correct indices printed, proper formatting, program exits cleanly  
**Status:** ✓ PASS

### Test Case 2: Multiple Solutions - Program Returns First Valid Pair

**ID:** AT-002  
**Description:** When multiple pairs sum to target, program returns valid indices  
**Preconditions:** Program compiled and executable available  
**Steps:**
1. Run program: `./main`
2. Provide input: array size=3, array=[3,2,4], target=6
3. Observe output

**Expected Result:** Output shows indices "1 2" (representing values 2 and 4)  
**Acceptance Criteria:** Valid pair returned, indices are correct, no crash  
**Status:** ✓ PASS

### Test Case 3: No Solution Case

**ID:** AT-003  
**Description:** Program gracefully handles case where no pair sums to target  
**Preconditions:** Program compiled and executable available  
**Steps:**
1. Run program: `./main`
2. Provide input: array size=2, array=[1,2], target=5
3. Observe output

**Expected Result:** Output is an empty line (no indices found)  
**Acceptance Criteria:** Empty output indicates no solution, program doesn't crash, exits normally  
**Status:** ✓ PASS

### Test Case 4: Negative Numbers

**ID:** AT-004  
**Description:** Program handles negative numbers correctly  
**Preconditions:** Program compiled and executable available  
**Steps:**
1. Run program: `./main`
2. Provide input: array size=3, array=[-1,-2,-3], target=-5
3. Observe output

**Expected Result:** Output shows valid indices such as "0 1" or "1 2"  
**Acceptance Criteria:** Correctly processes negative numbers, returns valid pair indices  
**Status:** ✓ PASS

### Test Case 5: Duplicate Values

**ID:** AT-005  
**Description:** Program handles arrays with duplicate values  
**Preconditions:** Program compiled and executable available  
**Steps:**
1. Run program: `./main`
2. Provide input: array size=2, array=[3,3], target=6
3. Observe output

**Expected Result:** Output shows indices "0 1" (both threes)  
**Acceptance Criteria:** Correctly identifies different indices of duplicate values  
**Status:** ✓ PASS

### Test Case 6: Built-in Test Harness

**ID:** AT-006  
**Description:** Program automatically runs built-in tests when no stdin provided  
**Preconditions:** Program compiled and executable available  
**Steps:**
1. Run program without piping input: `./main`
2. Observe console output

**Expected Result:** Multiple test cases execute with results displayed  
**Acceptance Criteria:** All tests pass, output is clear and informative, no errors reported  
**Status:** ✓ PASS

### Test Case 7: Edge Case - Single Element

**ID:** AT-007  
**Description:** Program handles single-element arrays gracefully  
**Preconditions:** Program compiled and executable available  
**Steps:**
1. Run program: `./main`
2. Provide input: array size=1, array=[5], target=10
3. Observe output

**Expected Result:** Output is empty (cannot find two numbers)  
**Acceptance Criteria:** Correctly identifies that two different indices cannot be found  
**Status:** ✓ PASS

### Test Case 8: Algorithm Consistency

**ID:** AT-008  
**Description:** Both algorithms (brute-force and hash-table) produce consistent results  
**Preconditions:** Program compiled with both implementations active  
**Steps:**
1. Run program with multiple test inputs
2. Compare results from both algorithmic approaches
3. Verify hash-table performance improvement

**Expected Result:** Both algorithms return identical index pairs; hash-table version is faster  
**Acceptance Criteria:** Results match, performance shows O(n) benefits for larger arrays  
**Status:** ✓ PASS

## Sign-Off

- **Tested By:** QA Team / May 7, 2026
- **Approved By:** Project Lead / May 7, 2026
- **Status:** APPROVED - Ready for Production
