#include <iostream>
using namespace std;
int main()

{
	int student[4];
	int sum;
	double average;
	int i;

	student[0]=63;
	student[1]=95;
	student[2]=47;
	student[3]=100;
	

	sum=0;
	for(i=0;i<4;i++){
		sum+=student[i];
	}
	average=sum/4.0;
	cout<<"heikintiha"<<average<<"点です\n";
	return 0;
	


}
