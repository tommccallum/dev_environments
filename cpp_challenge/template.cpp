#include <bits/stdc++.h>
#include <cassert>

using namespace std;

int solution(vector<int> &A)
{
    return 0;
}

int solution(std::string& S)
{
	return 0;
}

int main()
{
	{
	    auto P = vector<int>({1,2,3});
		auto res = 1;
	    auto soln = solution(P);
		cout << soln << endl;
	    assert(soln==res);
	}
	{
		auto S = std::string("");
		auto res = 1;
		auto soln = solution(S);
		cout << soln << endl;
		assert(soln==res);
	}
    return
}
