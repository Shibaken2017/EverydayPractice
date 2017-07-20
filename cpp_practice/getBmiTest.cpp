#include "getBmi.h"
#include <iostream>
using namespace std;

int main(){
	double height,weight,bmi;
	
	cout<<"身長cm=";
	cin>>height;
		
	cout<<"体重kg=";
	cin>>weight;
	
	bmi=getBmi(height,weight);
	cout<<"あなたのBMIは"<<bmi<<"です\n";	

	return 0;

}
