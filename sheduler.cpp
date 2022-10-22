#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int m,n;
    cin >> n >> m;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    int max=arr[0];
    for(int i=1;i<n;i++){
        if(arr[i]>max){
            max=arr[i];
        }
        
    }
    if(m==1){
        int total=0;
        for(int i=0;i<n;i++){
            total=total+pow(2,arr[i]);
        } 
        cout<<total<<endl;
    
        }
    else
    {
        int total2;
        total2=pow(2,max);
        cout<<total2<<endl;
    }    
    return 0;
}
