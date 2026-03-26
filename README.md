# Two Sum Problem Solver (C++20)

This project provides two C++ implementations for the classic Two Sum problem and a small built-in test harness.

## Features

- **Brute Force Approach**: `TwoSumArray` - nested loops, O(n²) time complexity.
- **Optimized Approach**: `TwoSumsHashTable` - uses a hash table, O(n) time complexity.
- **Built-in Tests**: Run the executable without stdin to execute sample testcases.
- **CI**: GitHub Actions builds and runs the compiled binary.

## Build / Installation

Requirements: a C++20-capable compiler (g++ >= 10 or MSVC with C++20).

Build locally (Linux/macOS):
```sh
g++ -std=c++20 -O2 -o main source/main.cpp
```

On Windows with MSVC, use the Visual Studio Developer Command Prompt and compile with `/std:c++20`.

## Usage

Run built-in tests (no stdin):
```sh
./main
```

Run with stdin input (first line `n`, second line `n` integers, third line `target`):
```sh
printf "4\n2 7 11 15\n9\n" | ./main
```

## Project Structure

- `source/main.cpp`: C++ implementation and test runner.
- `source/requirements.txt`: Build/tooling notes for C++.
- `.github/workflows/ci.yml`: CI workflow updated to build and run the C++ binary.

## Contributing

Feel free to submit issues or pull requests for improvements.

*This is the latest test branch.*