//Given a positive integer N, print count of set bits in it. 
//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    int setBits(int N) {
           if (N == 0)
        return 0;
    else
        return (N & 1) + setBits(N >> 1);
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin >> N;

        Solution ob;
        int cnt = ob.setBits(N);
        cout << cnt << endl;
    }
    return 0;
}

// } Driver Code Ends
