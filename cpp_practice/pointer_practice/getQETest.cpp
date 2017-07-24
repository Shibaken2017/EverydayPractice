#include "getQE.h"
#include <iostream>
using namespace std;

int main()
{
	double a,b,c,x1,x2;
	
	cout<<"定数a=";
	cin >> a ;
	cout<<"定数b=";
	cin >>b;
	cout<<"定数c=";
	cin>>c;
	
	if(getQE(a,b,c,&x1,&x2)==true){
		cout<<"1つ目の解"<<x1<<"\n";
		cout<<"2つ目の解"<<x2<<"\n";
	}else{
		cout<<"解がありません\n";
	
	}
	return 0;
}
