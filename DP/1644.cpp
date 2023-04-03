#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
vector<int> prime;

void get_prime(int n) {
	vector<bool> isCheck(n + 1, false);
	for (int i = 2; i * i <= n; i++)
	{
		if (isCheck[i] == false)
		{
			for (int j = 2 * i; j <= n; j += i)
			{
				isCheck[j] = true;
			}
		}
	}
	for (int i = 2; i <= n; i++) {
		if (isCheck[i] == false)
		{
			prime.push_back(i);
		}
	}

}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;

	if (N == 1)
	{
		cout << 0;
		return 0;
	}

	get_prime(N);

	int ans = 0;
	int s = 0, e = 0;
	int sum = 0;

	while (s <= e)
	{
		if (e == prime.size() - 1)	break;

		if (sum < N) {
			sum += prime[e++];
		}
		else if (sum > N) {
			sum -= prime[s++];
		}
		else {
			ans++;
			sum -= prime[s++];
		}
	}

	cout << ans;

	return 0;
}