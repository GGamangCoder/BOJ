// 오큰수

#include <iostream>
#include <stack>
using namespace std;

int A[1000001];
int NGE[1000001];
stack<int> s;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;
    for(int i=0; i<n; i++)  cin >> A[i];

    for(int i=0; i<n; i++)
    {
        while (!s.empty() && A[s.top()] < A[i]) {
            NGE[s.top()] = A[i];
            s.pop();
        }
        
        s.push(i);
    }

    // 스택에 남은, 오큰수 없는 것들에 대해 처리
    while (!s.empty())
    {
        NGE[s.top()] = -1;
        s.pop();
    }

    for(int i=0; i<n; i++)  cout<<NGE[i]<<" ";

    return 0;
}
