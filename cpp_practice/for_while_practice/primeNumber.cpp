#include<cmath>
#include<string>
#include<iostream>
using namespace std;


int main(){
	int n,max,i;
	string judge;

	cout<<"素数かどうかを判定する整数";
	cin>>n;

	max=(int)sqrt((double)n);
	
	if(n>=2)
	{
		judge="素数です";
	}
	else{
		judge="素数ではありません";	
	}



	for (i=2;i<=max;i++){
		if(n % i==0){
			judge="素数ではありません";
			break;		
		}


	}
	
	cout<<n<<"は"<<judge<<"\n";
	return 0;



}
