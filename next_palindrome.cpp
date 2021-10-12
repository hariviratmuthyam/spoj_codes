#include <iostream>
#include<string>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	  string s;cin>>s;
	   int n=s.size();
	   string rev=s;
	   for(int i=0;i<n/2;i++){
	       rev[n-1-i]=rev[i];
	   }
	   if(rev>s) cout<<rev<<endl;
	   else {
	       int mid=(n-1)/2;
	       for(int i=mid;i>=0;i--){
	           if(rev[i]!='9'){
	           rev[i]=rev[i]+1;
	           break;
	       }
	       else
	       rev[i]='0';    
	       }
	   
	   
	   for(int i=0;i<n/2;i++){
	       rev[n-1-i]=rev[i];
	   }
	   if(rev[0]=='0'){
	       rev[0]='1';
	       rev=rev+'1';
	   }
	   cout<<rev<<endl;
	   }
	    
	}
	
	return 0;
}
