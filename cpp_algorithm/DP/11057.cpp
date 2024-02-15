#include <iostream>

#define MOD 10007

using namespace std;


int main() {
    int n, dp[10];
    int result = 0;

    cin >> n;

    for (int i=0; i<10; i++)    dp[i] = 1;

    for (int i=0; i<n-1; i++) {
        for (int j=0; j<10; j++) {
            for (int k=j+1; k<10; k++) {
                dp[j] += dp[k];
            }
            dp[j] %= MOD;
        }
    }

    for (int i=0; i<10; i++) {
        result += dp[i];
    }
    cout << result % MOD;

    return 0;
}