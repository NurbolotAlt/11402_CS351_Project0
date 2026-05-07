# Deployment Guide

## 1. Introduction

The Two Sum Problem Solver is a standalone command-line executable requiring no installation beyond compilation. This guide covers building from source, deployment to various environments, and verification procedures.

## 2. Pre-Deployment Checklist

- [x] Source code reviewed and approved
- [x] All unit tests passing
- [x] All integration tests passing
- [x] CI/CD pipeline successful
- [x] Documentation complete and accurate
- [x] No compilation warnings
- [x] Performance benchmarks completed
- [x] Cross-platform testing completed

## 3. Installation Instructions

### 3.1 Prerequisites

**Required**:
- C++20 capable compiler:
  - GCC g++ (version 10 or higher)
  - Clang (version 11 or higher)
  - MSVC (Visual Studio 2019 or later with C++20)
- Standard development tools (make, git)
- Terminal/Command prompt access

**Optional**:
- CMake (for larger build systems)
- Git (for repository cloning)

### 3.2 Installation Steps

**Linux/macOS**:
```bash
# 1. Clone or download repository
git clone <repository-url>
cd 11402_CS351_Project0-1

# 2. Navigate to source directory
cd source

# 3. Compile with optimization
g++ -std=c++20 -O2 -o main main.cpp

# 4. Verify compilation succeeded
ls -la main

# 5. Run built-in tests
./main
```

**Windows (MSVC)**:
```cmd
REM 1. Open Developer Command Prompt for Visual Studio

REM 2. Navigate to source directory
cd source

REM 3. Compile
cl /std:c++latest /O2 main.cpp /link /OUT:main.exe

REM 4. Run built-in tests
main.exe
```

**Windows (MinGW)**:
```cmd
cd source
g++ -std=c++20 -O2 -o main.exe main.cpp
main.exe
```

### 3.3 Configuration

No configuration files required. The program operates with default settings:
- Input: Reads from stdin or executes built-in tests
- Output: Writes to stdout
- Error messages: May write to stderr

No environment variables or configuration files needed.

## 4. Deployment Environments

### 4.1 Development Environment

**Setup**:
1. Clone repository: `git clone <url>`
2. Navigate to source: `cd source/`
3. Compile with debug symbols: `g++ -std=c++20 -g -O0 -o main main.cpp`
4. Run tests: `./main`
5. Test with custom input: `echo "2\n3 4\n7" | ./main`

**Verification**:
- All built-in tests pass
- No compiler warnings
- Test output matches expected format

### 4.2 Testing Environment

**Setup**:
1. Obtain compiled binary from development environment
2. Copy to test machine: `scp /path/to/main testuser@testmachine:/opt/two-sum/`
3. Verify permissions: `chmod +x /opt/two-sum/main`
4. Execute test suite: `/opt/two-sum/main`

**Test Cases**:
- Basic Two Sum: [2,7,11,15] target=9 → [0,1] ✓
- No Solution: [1,2] target=5 → empty ✓
- Negative Numbers: [-1,-2,-3] target=-5 ✓
- Duplicates: [3,3] target=6 → [0,1] ✓

### 4.3 Production Environment

**Release Build**:
```bash
# Compile with full optimization
g++ -std=c++20 -O3 -DNDEBUG -o main main.cpp

# Strip symbols for smaller binary (optional)
strip main

# Verify binary
file main
./main  # Run built-in tests
```

**Distribution**:
1. Package binary: `tar czf two-sum-solver-v1.0.tar.gz main`
2. Generate checksums: `sha256sum two-sum-solver-v1.0.tar.gz > SHA256SUMS`
3. Create release on GitHub with binary attachments
4. Document in release notes

**Installation for End Users**:
```bash
# Extract
tar xzf two-sum-solver-v1.0.tar.gz

# Make executable
chmod +x main

# Verify
./main
```

## 5. Post-Deployment Verification

### Verification Checklist

✓ **Binary Execution**
```bash
./main  # Should run built-in tests and show results
```

✓ **Test Input Processing**
```bash
printf "4\n2 7 11 15\n9\n" | ./main  # Should output: 0 1
```

✓ **No Solution Handling**
```bash
printf "2\n1 2\n5\n" | ./main  # Should output empty line
```

✓ **Cross-Platform Compatibility**
- Test on Windows (MSVC and MinGW)
- Test on Linux (GCC and Clang)
- Test on macOS (Apple Clang)

✓ **Performance Verification**
- Large input (n=10000): Should complete in <5 seconds
- Hash-table version faster than array-based for large inputs

### Verification Output
Expected output from built-in tests:
```
Test 1: [2, 7, 11, 15], target=9 -> [0, 1] ✓
Test 2: [3, 2, 4], target=6 -> [1, 2] ✓
Test 3: [3, 3], target=6 -> [0, 1] ✓
[...more tests...]
All tests passed!
```

## 6. Rollback Procedures

Since this is a stateless command-line tool with no persistent state or database:

**Rollback Steps**:
1. If new version has issues, simply use previous binary: `cp main.v1.0 main`
2. No data migration or state synchronization needed
3. No database rollback required
4. No cleanup of temporary files needed

**Version Management**:
```bash
# Keep versioned binaries
cp main main.v1.0
cp main main.v1.1

# Switch versions as needed
ln -sf main.v1.0 main.current
```

**If Compilation Issues Arise**:
1. Verify compiler version: `g++ --version`
2. Check C++20 support: `g++ -std=c++20 -x c++ - <<< 'int main() {}'`
3. Fallback to previous source version if needed
4. Report issue to development team

## 7. Support and Maintenance

[Describe ongoing support and maintenance]
