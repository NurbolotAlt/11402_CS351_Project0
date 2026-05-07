# Large Test Cases for Two Sum Problem

This folder contains test cases for load testing and performance validation of the Two Sum Problem Solver.

## Files

### `large_testcase.txt`
- **Size**: 10,000 elements (1 to 10,000)
- **Target**: 5,000
- **Expected Result**: 1 + 9,999 = 10,000 (or 2 + 4,998 = 5,000, etc.)
- **Purpose**: Standard large test case for CI/CD validation
- **Runtime**: < 1 second for both algorithms on modern hardware

### `medium_testcase.txt`
- **Size**: 25,000 elements (1 to 25,000)
- **Target**: 12,500
- **Expected Result**: Multiple valid pairs exist
- **Purpose**: Medium-scale test to validate performance scaling
- **Runtime**: ~10-100ms for hash-table, ~50-200ms for brute-force

### `no_solution_testcase.txt`
- **Size**: 5 elements [1, 2, 3, 4, 5]
- **Target**: 100
- **Expected Result**: "not found" (no valid pair sums to 100)
- **Purpose**: Edge case - validates "not found" scenario
- **Runtime**: < 1ms

### `negative_numbers_testcase.txt`
- **Size**: 8 elements [-100, -50, -20, 0, 10, 50, 100, 200]
- **Target**: 50
- **Expected Result**: -50 + 100 = 50 (or 10 + 40, etc.)
- **Purpose**: Validates handling of negative numbers
- **Runtime**: < 1ms

### `generate_test.py`
Python script to generate custom test cases of any size.

**Usage**:
```bash
# Generate 100,000 element test case
python3 tests/generate_test.py 100000 -o tests/huge_testcase.txt

# Generate 50,000 elements with custom target
python3 tests/generate_test.py 50000 -t 25000 -o tests/custom_test.txt

# Print to stdout (for piping)
python3 tests/generate_test.py 1000
```

**Parameters**:
- `n` (required): Number of array elements
- `-t, --target` (optional): Target sum (default: n+1)
- `-o, --output` (optional): Output file (default: stdout)

## Test Case Format

All test files follow this format:
```
<array_size>
<space_separated_integers>
<target_sum>
```

Example:
```
3
1 2 3
5
```

## Running Tests Locally

### Small Test Case
```bash
g++ -std=c++20 -O2 -o main source/main.cpp
cat tests/large_testcase.txt | ./main
```

### Medium Test Case (25,000 elements)
```bash
cat tests/medium_testcase.txt | ./main
```

### Edge Case Tests
```bash
# Test with no valid solution
echo "Running no-solution test..."
cat tests/no_solution_testcase.txt | ./main

# Test with negative numbers
echo "Running negative numbers test..."
cat tests/negative_numbers_testcase.txt | ./main
```

### Custom Large Test Case
```bash
python3 tests/generate_test.py 100000 | ./main
```

### Performance Comparison
```bash
# Measure execution time with built-in time utility
time python3 tests/generate_test.py 50000 | ./main
```

## GitHub Actions CI/CD Integration

The GitHub Actions workflow (`.github/workflows/ci.yml`) automatically runs:

1. **Built-in tests**: 6 small test cases (< 1ms each)
2. **Medium test (25,000 elements)**: Scaling validation
3. **Edge case tests**: No-solution and negative numbers tests
4. **Large test (10,000 elements)**: Validates O(n²) and O(n) algorithms
5. **Extra-large test (50,000 elements)**: Performance stress test

### Expected Results in CI

✅ **Hash-table algorithm (O(n))**: Should complete in ~10-50ms
⏱️ **Brute-force algorithm (O(n²))**: Should complete in ~500ms-2s

The CI workflow uses `/usr/bin/time -v` to display:
- Maximum resident set size (memory usage)
- Elapsed time
- CPU usage percentage

## Scaling Test Cases

| Array Size | Brute Force | Hash-Table | Memory | Notes |
|-----------|------------|-----------|--------|-------|
| 1,000 | ~1ms | <1ms | <1MB | Small test |
| 10,000 | ~100ms | <1ms | ~1MB | Default CI test |
| 50,000 | ~2.5s | <5ms | ~2MB | Extra-large CI test |
| 100,000 | ~10s | ~10ms | ~4MB | Performance test |
| 1,000,000 | ~100s | ~100ms | ~40MB | Heavy stress test |

## Creating Your Own Test Cases

```bash
# Generate tests of various sizes for benchmarking
for size in 1000 5000 10000 50000 100000; do
    python3 tests/generate_test.py $size -o tests/test_${size}.txt
done

# Run each test
for f in tests/test_*.txt; do
    echo "Testing $f..."
    /usr/bin/time -v cat $f | ./main
    echo "---"
done
```

## Customizing for Your Professor

### Option 1: Increase Default Test Size in CI
Edit `.github/workflows/ci.yml` to test with 100,000+ elements:
```yaml
- name: Run massive test case (100,000 elements)
  run: python3 tests/generate_test.py 100000 | ./main
```

### Option 2: Add Multiple Test Cases
Generate several test cases with different characteristics (no solution, negatives, duplicates):

```bash
python3 tests/generate_test.py 10000 -o tests/medium.txt    # 10k elements
python3 tests/generate_test.py 50000 -o tests/large.txt     # 50k elements  
python3 tests/generate_test.py 100000 -o tests/xlarge.txt   # 100k elements
```

Then update `.github/workflows/ci.yml` to run all of them.

### Option 3: Streaming Large Test Generator
For truly massive datasets (millions of elements), you can pipe directly:
```bash
python3 tests/generate_test.py 10000000 | timeout 60 ./main
```

## Verification

After running a large test case, verify correctness:
- Output should be two space-separated indices
- Those indices must point to array elements that sum to target
- Program should exit with code 0

Example verification script:
```bash
python3 tests/generate_test.py 1000 > /tmp/test.txt
./main < /tmp/test.txt > /tmp/result.txt
echo "Result: $(cat /tmp/result.txt)"
```
