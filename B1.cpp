// Write a program non-recursive and recursive program to calculate Fibonacci numbers and
// analyze their time and space complexity.

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int fibonacci_recursive(int n)
{
	if (n <= 1)
		return n;
	return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2);
}

int fibonacci_iterative(int n)
{
	int x = 2, y = 3, z = 5;
	int num = x;
	if (n <= 1)
		return n;
	if (n == 2)
		return 1;
	for (int i = 3; i <= n; i++)
	{
		num = x;
		z = x + y;
		x = y;
		y = z;
	}
	return num;
}

int main()
{
	int ch = 1;
	while (ch != 0)
	{
		cout << endl
			 << "1. Recursive";
		cout << endl
			 << "2. Iterative";
		cout << endl
			 << "0. Exit";
		cin >> ch;

		if (ch == 0)
			break;
		else if (ch == 1)

		{
			cout << endl
				 << "Enter number";
			int n;
			cin >> n;
			if (n >= 0)
				cout << fibonacci_recursive(n);
		}

		else if (ch == 2)
		{
			cout << endl
				 << "Enter number";
			int n;
			cin >> n;
			if (n >= 0)
				cout << fibonacci_iterative(n);
		}
		else
			cout << "Invalid input";
	}
}
