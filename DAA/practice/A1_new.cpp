#include <iostream>
using namespace std;

int fibo_rec(int n)
{
    if (n <= 1)
    {
        return n;
    }
    return fibo_rec(n - 1) + fibo_rec(n - 2);
}

int fibo_iter(int n)
{
    if (n <= 1)
    {
        return n;
    }

    int x, y, z, num;
    x = 2;
    y = 3;
    z = 5;

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
        cout << "\t================Fibo==================\t\n"
             << endl;

        cout << "Select method: " << endl;
        cout << "1. Iterative \n2. Recursive \n3. Exit\n";

        cin >> ch;

        if (ch == 0)
        {
            break;
        }

        else if (ch == 1)
        {
            int number;
            cout << "\nEnter number: \n";
            cin >> number;
            if (number >= 0)
            {
                cout << fibo_iter(number) << endl;
            }
        }

        else if (ch == 2)
        {
            int number;
            cout << "\nEnter number: \n";
            cin >> number;
            if (number >= 0)
            {
                cout << fibo_rec(number) << endl;
            }
        }

        else
        {
            cout << "\tPlease enter valid choice\n"
                 << endl;
        }
    }
    return 0;
}