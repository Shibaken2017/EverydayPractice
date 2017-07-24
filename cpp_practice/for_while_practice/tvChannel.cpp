#include <iostream>
using namespace std;

int main(){
	int channel;

	cout<<"チャンネル番号";
	cin>>channel;

	switch(channel)
	{
		case 1:
		cout<<"nhk\n";
		break;
		
		case 3:
		cout<<"nhkedu\n";
		break;

		case 4:
		cout<<"nihonTv\n";
		break;

		case 6:
		cout <<"tbsTv\n";
		break;

		case 8:
		cout << "fujitv\n";
		break;

		case 10:
		cout<<"tvasahi\n";
		break;

		case 12:
		cout <<"tvtokyo\n";
		break;

		default:
		cout<<"割り当てられていません\n";
		break;

	}




}

