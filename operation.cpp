#include <bits/stdc++.h>
using namespace std;
string input;
vector<int> arrayData;
int q, l, r;
int main()
{
	cin >> input;
	arrayData.resize(input.size() + 1);
	for (int i = 0; i < input.size(); i++)
	{
		int temp = 0;
		if (input[i] == 'C')
		{
			temp = 1;
		}
		else if (input[i] == 'O')
		{
			temp = 2;
		}
		else if (input[i] == 'W')
		{
			temp = 3;
		}
		arrayData[i + 1] = arrayData[i] ^ temp;
	}
	cin >> q;
	for (int i = 0; i < q; i++)
	{
		cin >> l >> r;
		cout << ((arrayData[r] ^ arrayData[l - 1]) == 1 ? 'Y' : 'N');
	}
	return 0;
}