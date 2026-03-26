# Two Sum Problem Solver

This Python project implements two solutions to the classic Two Sum problem: finding two numbers in an array that add up to a target sum and returning their indices.

## Features

- **Brute Force Approach**: [`twoSumArray`](main.py) - Uses nested loops with O(n²) time complexity.
- **Optimized Approach**: [`twoSumHashTable`](main.py) - Uses a hash table for O(n) time complexity.
- **Comprehensive Testing**: Includes a [`run_tests`](main.py) function with various test cases, including edge cases like duplicates, negatives, and empty arrays.
- **CI/CD Pipeline**: Automated testing via GitHub Actions using pytest.

## Installation

1. Clone the repository.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the tests directly:
```sh
python main.py
```

Or use pytest for more detailed output:
```sh
python -m pytest main.py -v
```

## Project Structure

- [`main.py`](main.py): Contains the Two Sum implementations and test runner.
- [`requirements.txt`](requirements.txt): Lists project dependencies (pytest).
- [`.github/workflows/ci.yml`](.github/workflows/ci.yml): GitHub Actions workflow for continuous integration.
- [`tests/`](tests/): Directory for additional test files (currently empty).

## Contributing

Feel free to submit issues or pull requests for improvements.


Requirements: C++, Github actions, Docker, Design correct testcase 

This is branched edit.