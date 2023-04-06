// 직사각형에서 탈출

#include <iostream>
#include <algorithm>
using namespace std;

int x, y, w, h;
int main(){
    cin >> x >> y >> w >> h;
    int width = w - x;
    int height = h - y;
    width = width > x ? x : width;
    height = height > y ? y : height;
    cout << (width > height ? height : width);

    return 0;
}