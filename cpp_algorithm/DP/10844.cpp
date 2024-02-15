#include <iostream>
#include <vector>

#define MOD 1000000000

using namespace std;

int main() {
    int N;          // 100 이하의 수, 최대 길이 100
    int dp[101][10] = { 0, };
    int result = 0;

    cin >> N;

    for (int i=1; i<10; i++) {
        dp[1][i] = 1;
    }

    for (int i=2; i<=N; i++) {
        for (int j=0; j<10; j++) {
            if (j == 0)
                dp[i][0] = dp[i-1][1];
            else if (j == 9)
                dp[i][9] = dp[i-1][8];
            else        // 업, 다운 가능
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1];
            
            dp[i][j] %= MOD;
        }
    }

    for (int i=0; i<10; i++) {
        result = (result + dp[N][i]) % MOD;
    }

    cout << result << endl;

    return 0;
}