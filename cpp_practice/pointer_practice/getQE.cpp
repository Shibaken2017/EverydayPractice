#include <cmath>
bool getQE(double a,double b,double c,double *x1,double *x2){
	double r;
	r=b*b-4*a*c;
	
	if(r<0)
	{
		return false;

	}
	else{
		*x1=(-b+sqrt(r))/(2*a);
		*x2=(-b-sqrt(r))/(2*a);
		return true;
	}
}
