#include <iostream>
using namespace std;
int main(){
	double height,weight,bmi;
	cout<<"身長=";
	cin>>height;

	cout<<"体重=";
	cin>>weight;

	bmi=weight/(height*0.01*height*0.01);

	cout<<"あなたのBMIは"<<bmi<<"です\n";
		

	return 0;
}
