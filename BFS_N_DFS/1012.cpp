// 숨바꼭질

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int graph[51][51];
int dx[4] = { 1, -1, 0, 0 };
int dy[4] = { 0, 0, 1, -1 };
int n, m, k;		// 가로, 세로, 배추
int x, y;
int cnt;
queue<pair<int, int>> q;

void bfs(int x, int y)
{
	graph[y][x] = 0;
	q.push(pair<int, int>(x, y));

	while (!q.empty())
	{
		int x = q.front().first;
		int y = q.front().second;

		q.pop();

		for (int i = 0; i < 4; i++)
		{
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (0 <= nx && nx < m && 0 <= ny && ny < n)
			{
				if (graph[ny][nx] == 1)
				{
					graph[ny][nx] = 0;
					q.push(pair<int, int>(nx, ny));
				}
			}
		}
	}
	cnt++;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int T;
	cin >> T;

	while (T--)
	{
		for (int j = 0; j < 50; j++)
			for (int i = 0; i < 50; i++)
				graph[j][i] = 0;

		cnt = 0;
		cin >> m >> n >> k;

		for (int i = 0; i < k; i++)
		{
			cin >> x >> y;
			graph[y][x] = 1;
		}

		for (int i = 0; i < 50; i++)
		{
			for (int j = 0; j < 50; j++)
			{
				if (graph[j][i] == 1)	bfs(i, j);
			}
		}

		cout << cnt << endl;
	}
}