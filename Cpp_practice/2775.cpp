// 부녀회장이 될테야


#include <iostream>
using namespace std;

int GetCount(int k, int n){
    if (n==1)   return 1;
    if (k==0)   return n;

    return GetCount(k-1, n) + GetCount(k, n-1);
}

int main(){
    int T;
    cin >> T;

    for (int i=0; i<T; i++){
        int k, n;
        cin >> k >> n;
        cout << GetCount(k, n) << endl;
    }

    return 0;
}