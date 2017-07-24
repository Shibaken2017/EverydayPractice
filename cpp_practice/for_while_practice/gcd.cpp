#include <iostream>
using namespace std;

int main(){
	int a,b;
	
	cout << "整数1=";
	cin >>  a;

	cout << "整数2=";
	cin>>b;
	

	while(a != b){
		if(a>b){
		a-=b;		
		}
		else{
		b-=a;
		}

	}
	cout<<"最大公約数は"<< a <<"です\n";
	return 0;
}
