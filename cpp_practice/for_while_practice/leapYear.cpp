#include <iostream>
using namespace std;

int main(){
	int year;
	cout<<"西暦=";
	cin >>year;
	
	if((year%4==0 && year%100!=0)||(year&400==0)){
		cout<<"うるう年です\n";
	}else{
		cout<<"うるどしではありませｎ\n";
	
	}

	return 0;


}
