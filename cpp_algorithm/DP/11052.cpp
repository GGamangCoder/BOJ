#include <iostream>
#include <algorithm>

using namespace std;

const int MAX = 1001;
int dp[MAX];
int cards[MAX];

int main(){
    int n;
    cin >> n;

    for(int i=1; i<=n; i++) {
        cin >> cards[i];
    }

    for(int i=1; i<=n; i++) {
        for(int j=1; j<=i; j++) {
            dp[i] = max(dp[i], dp[i-j] + cards[j]);
        }
    }

    cout << dp[n] << endl;

    return 0;
}