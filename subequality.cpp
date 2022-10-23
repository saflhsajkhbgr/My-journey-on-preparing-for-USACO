#include <bits/stdc++.h>
using namespace std;
const int m = 18;
string s, t, o;
string aArray[1 << m];
string bArray[1 << m];
int c[1 << m];
int q;
int solve(int x, int y)
{
	if (x > y)
	{
		swap(x, y);
	}
	return y * (y + 1) / 2 + x;
}
int main()
{
	cin >> s >> t;
	for (int i = 0; i < s.size(); i++)
	{
		for (int j = 0; j < m; j++)
		{
			aArray[solve(s[i] - 'a', j)] += s[i];
		}
	}
	for (int i = 0; i < t.size(); i++)
	{
		for (int j = 0; j < m; j++)
		{
			bArray[solve(t[i] - 'a', j)] += t[i];
		}
	}
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < m; j++)
		{
			c[solve(i, j)] = (aArray[solve(i, j)] == bArray[solve(i, j)]);
		}
	}	
	cin >> q;
	for (int i = 0; i < q; i++)
	{
		cin >> o;
		bool f = false;
		for (int j = 0; j < o.size(); j++)
		{
			for (int k = 0; k < o.size(); k++)
			{
				if (!c[solve(o[j] - 'a', o[k] - 'a')])
				{
					f = true;
				}
			}
		}
		cout << (f ? 'N' : 'Y');
	}
	return 0;
}