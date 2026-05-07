# Requirements Traceability Matrix (RTM)

## Purpose

The Requirements Traceability Matrix provides a comprehensive mapping between project requirements, design elements, implementation, and test cases. This ensures that every requirement is designed, implemented, and tested, with full traceability throughout the development lifecycle.

## Traceability Table

| Requirement ID | Requirement Description | Design Element | Implementation | Test Case | Status |
|----------------|-------------------------|-----------------|-----------------|-----------|--------|
| FR-001 | Array-based Solution | TwoSumArray function | main.cpp:24-32 | UT-001 to UT-008 | ✓ VERIFIED |
| FR-002 | Hash-table Solution | TwoSumHashTable function | main.cpp:34-43 | UT-009 to UT-016 | ✓ VERIFIED |
| FR-003 | Input Processing | Input handler in main() | main.cpp:45-85 | IT-001, IT-002 | ✓ VERIFIED |
| FR-004 | Index Output | Output formatter in main() | main.cpp:90-105 | ST-002, AT-001 | ✓ VERIFIED |
| FR-005 | Empty Output | Empty vector handling | main.cpp:110-115 | AT-003, UT-006 | ✓ VERIFIED |
| FR-006 | Built-in Tests | Test harness in main() | main.cpp:50-75 | AT-006, ST-001 | ✓ VERIFIED |
| FR-007 | Multiple Solutions | Loop in main() | main.cpp:45-120 | IT-002, AT-002 | ✓ VERIFIED |
| FR-008 | Input Validation | Input error handling | main.cpp:75-85 | IT-003, IT-004 | ✓ VERIFIED |
| NFR-001 | C++20 Language | Code written in C++20 | main.cpp:1-6 | ST-004 | ✓ VERIFIED |
| NFR-002 | Array O(n²) Complexity | TwoSumArray algorithm | main.cpp:24-32 | UT-001 to UT-008 | ✓ VERIFIED |
| NFR-003 | Hash Table O(n) | TwoSumHashTable algorithm | main.cpp:34-43 | UT-009 to UT-016 | ✓ VERIFIED |
| NFR-004 | Cross-platform | Platform-specific IO handling | main.cpp:11-21 | ST-004 | ✓ VERIFIED |
| NFR-005 | Clean Compilation | Compiler flags | Makefile / requirements.txt | ST-004 | ✓ VERIFIED |
| NFR-006 | Code Quality | Documentation and style | main.cpp comments | Code review | ✓ VERIFIED |
| NFR-007 | CLI Accessibility | Clear input/output format | main.cpp I/O sections | AT-001 to AT-008 | ✓ VERIFIED |

## Verification Status

**Overall Status: 100% COMPLETE - ALL REQUIREMENTS VERIFIED**

### Functional Requirements Coverage
- ✓ All 8 functional requirements (FR-001 through FR-008) are implemented and tested
- ✓ Each requirement has corresponding design elements
- ✓ Each requirement has minimum 1-2 dedicated test cases
- ✓ No gaps identified

### Non-Functional Requirements Coverage
- ✓ All 7 non-functional requirements (NFR-001 through NFR-007) are addressed
- ✓ Performance characteristics validated through comparative testing
- ✓ Cross-platform compatibility verified
- ✓ Code quality standards maintained

### Test Coverage
- ✓ 16 unit tests (UT-001 through UT-016)
- ✓ 5 integration tests (IT-001 through IT-005)
- ✓ 4 system tests (ST-001 through ST-004)
- ✓ 8 acceptance tests (AT-001 through AT-008)
- **Total: 33 test cases covering all requirements**

## Notes

1. **Two Algorithm Implementation**: Both brute-force and optimized solutions are implemented, allowing educational comparison
2. **No External Dependencies**: Uses only C++ standard library (vector, unordered_map), simplifying deployment
3. **Automated Testing**: Built-in test harness eliminates need for external test framework
4. **CI/CD Integration**: GitHub Actions automatically verifies all requirements on every commit
5. **Documentation Coverage**: All 8 markdown documents comprehensively cover the complete software lifecycle
6. **Design Trade-offs**: Brute-force solution maintained despite O(n²) complexity for educational value and simplicity comparison
