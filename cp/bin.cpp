#include<iostream>
using namespace std;
int movesb1(int );
int a[3][3];
int m,mmin=0;
int main()
{
	while(cin>>a[0][0]>>a[0][1]>>a[0][2])
	{
		cin>>a[1][0]>>a[1][1]>>a[1][2]);
		cin>>a[2][0]>>a[2][1]>>a[2][2]);
		for(int i=0;i<3;i++){m=movesb1(i);if(m<mmin)mmin=m;}
		cout<<mmin<<endl;
	}
	return 0;
}
int movesb1(int i)
{
	m=a[1][i]+a[2][i];
	for()
		
		
