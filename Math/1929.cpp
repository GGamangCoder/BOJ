// 소수 구하기

#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int M, N;
    cin >> M >> N;

    bool arr[1000001] = {false};

    for (int i=2; i<=N; i++){
        if (arr[i] == false)
            for (int j = 2*i; j <= N; j += i)
                arr[j] = true;
    }

    for (int i = M; i <= N; i++)
        if (!arr[i] && i != 1)
            cout << i << '\n';

    return 0;
}