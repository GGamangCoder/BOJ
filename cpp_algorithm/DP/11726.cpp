#include <iostream>

using namespace std;

int main() {
    int n;
    int D[1001];

    cin >> n;

    D[1] = 1, D[2] = 2;

    for (int i=3; i<=n; i++) {
        D[i] = D[i-1] + D[i-2];
        D[i] %= 10007;
    }

    cout << D[n];
    return 0;
}