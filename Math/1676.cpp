#include <iostream>

using namespace std;

int main() {
	// 동기화를 위한 필요구문 - 찾아보자
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int n;
	int ans = 0;

	cin >> n;
	for (int i = 5; i <= n; i *= 5) {
		ans += n / i;
	}

	cout << ans;

	return 0;
}