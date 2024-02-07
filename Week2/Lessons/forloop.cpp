#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
#define rep(i, a, b) for (int i = a; i < b; i++)

int main()
{

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int answer = 0;
    for(int i=0; i<10000; i++){
        answer += i;
        cout<<"first "<<i<<" number gives "<<answer<<"\n";
    }
    return 0;
}
