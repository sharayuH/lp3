using namespace std;
#include <iostream>
#include <bits/stdc++.h>

void printAnswers(vector<vector<string>> &board)
{
    cout << "Total answers: " << board.size() << endl;

    if (board.size() > 0)
    {
        for (int i = 0; i < board.size(); i++)
        {
            for (int j = 0; j < board[0].size(); j++)
            {
                cout << board[i][j] << endl;
            }
            cout << endl;
        }
    }
}

bool isSafe(int row, int col, vector<string> &board, int n)
{
    int tempRow = row;
    int tempCol = col;

    while (row >= 0 and col >= 0)
    {
        if (board[row][col] == 'Q')
            return false;
        row--;
        col--;
    }

    row = tempRow;
    col = tempCol;

    while (row < n and col < n)
    {
        if (board[row][col] == 'Q')
            return false;
        row++;
        col++;
    }

    row = tempRow;
    col = tempCol;

    while (row < n and col >= 0)
    {
        if (board[row][col] == 'Q')
            return false;
        row++;
        col--;
    }

    row = tempRow;
    col = tempCol;

    while (row >= 0 and col < n)
    {
        if (board[row][col] == 'Q')
            return false;
        row--;
        col++;
    }

    row = tempRow;
    col = tempCol;

    while (col >= 0)
    {
        if (board[row][col] == 'Q')
            return false;
        col--;
    }

    row = tempRow;
    col = tempCol;

    while (col < n)
    {
        if (board[row][col] == 'Q')
            return false;
        col++;
    }

    return true;
}

void solve(int col, vector<string> &board, vector<vector<string>> &ans, int n, int fixedCol)
{
    if (col == n)
    {
        ans.push_back(board);
        return;
    }

    if (col == fixedCol)
    {
        solve(col + 1, board, ans, n, fixedCol);
    }

    for (int row = 0; row < n; row++)
    {
        if (isSafe(row, col, board, n))
        {
            board[row][col] = 'Q';
            solve(col + 1, board, ans, n, fixedCol);
            board[row][col] = '.';
        }
    }
}

vector<vector<string>> solveNQueens(int n, int fixedRow, int fixedCol)
{
    vector<vector<string>> ans;
    vector<string> board(n);
    string s(n, '.');

    for (int i = 0; i < n; i++)
    {
        board[i] = s;
    }

    board[fixedRow][fixedCol] = 'Q';

    solve(0, board, ans, n, fixedCol);
    return ans;
}

int main()
{
    int n;
    cout << "Enter the size of board: ";
    cin >> n;
    cout << endl;

    int fixedRow, fixedCol;
    cout << "Enter valid coordinates of the fixed queen: ";
    cin >> fixedRow >> fixedCol;

    vector<vector<string>> ans = solveNQueens(n, fixedRow, fixedCol);

    printAnswers(ans);
}