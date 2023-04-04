// 숨바꼭질

#include <iostream>
#include <vector>
#include <queue>
// #include <algorithm>
using namespace std;
int N, K;
int x;
int cnt = 0;
bool flag = false;

bool isCheck[100001];

int main() {
	cin >> N >> K;
	queue<int> q;
	// 새로운 개념!! emplace
	q.push(N);

	while (true)
	{
		int l = sizeof(q);
		cnt++;

		for (int n = 0; n < l; n++)
		{
			int current = q.front();
			q.pop();

			if (current == K)
			{
				flag = true;
				break;
			}

			int x1 = current - 1;
			int x2 = current + 1;
			int x3 = current * 2;

			if (0 <= x1 && !isCheck[x1]) {
				isCheck[x1] = true;
				q.push(x1);
			}
			if (0 <= x2 && !isCheck[x2]) {
				isCheck[x2] = true;
				q.push(x2);
			}
			if (0 <= x3 && !isCheck[x3]) {
				isCheck[x3] = true;
				q.push(x3);
			}
		}
		if (flag == true)	break;
	}

	cout << cnt << endl;
	return 0;
}