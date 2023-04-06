// Hashing
// 도대체 두 코드 차이가 무엇인지 물어보기.. 백준


#include <iostream>
#include <string>
using namespace std;


int r = 1;
int M = 1234567891;
int main(){
    int L;
    string s;

    cin >> L;
    cin >> s;

    long long sum = 0;
    for (int i=0; i < s.length(); i++)
    {
        sum = (sum + (s[i] - 'a' + 1) * r) % M;
        r = r * 31 % M;
    }

    cout << sum;

    return 0;
}