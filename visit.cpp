#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
int a[1000020], q[2000020], in[1000020], n, flag;
int c[1000020];
int v[1000020];
ll g[1000020][2];
ll f[1000020][2];
int w[1000020];
ll answer;

void dfs(int p)
{
	int i;
	flag++;
	for (i = p;; i = a[i])
	{
		if (v[i] == flag)
			break;
		if (v[i])
			return;
		v[i] = flag;
	}
	for (; !c[i]; i = a[i])
		c[i] = 1;
}

void solve(int p)
{
	int i, ss = 0;
	for (i = p; c[i]; i = a[i])
		q[++ss] = i, c[i] = 0;
	int temp = w[q[1]];
	for (i = 1; i <= ss; i++)
	{
		temp = min(temp, w[q[i]]);
	}
	answer -= temp;
}

int main()
{
	int i;
	scanf("%d", &n);
	for (i = 1; i <= n; i++)
	{
		scanf("%d%d", &a[i], &w[i]), in[a[i]]++;
		answer += w[i];
	}

	for (i = 1; i <= n; i++)
		if (!v[i])
			dfs(i);

	for (i = 1; i <= n; i++)
		if (c[i])
			solve(i);
			
	printf("%lld\n", answer);
	return 0;
}