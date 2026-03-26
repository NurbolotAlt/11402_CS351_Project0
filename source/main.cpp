// C++20 implementation for Two Sum problem
// Provides two implementations:
// - TwoSumArray: brute-force O(n^2)
// - TwoSumHashTable: hash-table O(n)

#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <sstream>
#include <iomanip>
#if defined(_WIN32)
#include <io.h>
#include <stdio.h>
#define ISATTY _isatty
#define FILENO _fileno
#else
#include <unistd.h>
#define ISATTY isatty
#define FILENO fileno
#endif

using namespace std;

vector<int> TwoSumArray(const vector<int>& nums, int target) {
    int n = static_cast<int>(nums.size());
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (nums[i] + nums[j] == target) return {i, j};
        }
    }
    return {};
}

vector<int> TwoSumHashTable(const vector<int>& nums, int target) {
    unordered_map<int, int> m;
    for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
        int complement = target - nums[i];
        auto it = m.find(complement);
        if (it != m.end()) return {it->second, i};
        m[nums[i]] = i;
    }
    return {};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Input format:
    // n
    // a0 a1 ... a{n-1}
    // target

    auto valid_pair = [&](const vector<int>& nums, const vector<int>& p, int target) {
        if (p.size() != 2) return false;
        int a = p[0], b = p[1];
        if (a < 0 || b < 0 || a >= (int)nums.size() || b >= (int)nums.size() || a == b) return false;
        return nums[a] + nums[b] == target;
    };

    // If stdin is a terminal (no pipe) then run built-in tests for convenience.
    bool stdin_is_tty = ISATTY(FILENO(stdin));
    if (stdin_is_tty) {
        // Built-in test cases
        struct Test { vector<int> nums; int target; bool expect; };
        vector<Test> tests = {
            {{2,7,11,15}, 9, true},
            {{3,2,4}, 6, true},
            {{3,3}, 6, true},
            {{1,2,3}, 7, false},
            {{}, 0, false},
            {{-3,4,3,90}, 0, true}
        };

        cout << "Running built-in tests (no stdin detected)\n";
        for (size_t i = 0; i < tests.size(); ++i) {
            const auto& t = tests[i];
            auto r1 = TwoSumArray(t.nums, t.target);
            auto r2 = TwoSumHashTable(t.nums, t.target);
            bool ok1 = valid_pair(t.nums, r1, t.target);
            bool ok2 = valid_pair(t.nums, r2, t.target);
            cout << "Test " << (i+1) << ": ";
            cout << "nums=[";
            for (size_t j=0;j<t.nums.size();++j) { if (j) cout << ","; cout << t.nums[j]; }
            cout << "] target=" << t.target << " -> ";
            cout << "TwoSumArray(" << (ok1?"OK":"FAIL") << ") ";
            if (ok1) cout << "indices=" << r1[0] << "," << r1[1] << " ";
            cout << "TwoSumHashTable(" << (ok2?"OK":"FAIL") << ") ";
            if (ok2) cout << "indices=" << r2[0] << "," << r2[1] << " ";
            cout << "\n";
        }
        return 0;
    }

    // Otherwise behave as stdin-driven runner.
    int n;
    if (!(cin >> n)) {
        cerr << "Expected number of elements (n) on stdin.\n";
        return 1;
    }

    vector<int> nums;
    nums.reserve(n);
    for (int i = 0; i < n; ++i) {
        int x; cin >> x;
        nums.push_back(x);
    }

    int target; cin >> target;

    auto res1 = TwoSumArray(nums, target);
    auto res2 = TwoSumHashTable(nums, target);

    if (!res1.empty()) cout << "TwoSumArray: " << res1[0] << ' ' << res1[1] << '\n';
    else cout << "TwoSumArray: not found\n";

    if (!res2.empty()) cout << "TwoSumHashTable: " << res2[0] << ' ' << res2[1] << '\n';
    else cout << "TwoSumHashTable: not found\n";

    return 0;
}
