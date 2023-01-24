#include <iostream>
#include <cstdio>
#include <cmath>
#include <fstream>

using namespace std;

void compute_kronecker_symbol_table()
{
    int test_numbers[1000], table[1000][1000];
    for (int i = 0; i < 1000; i++) test_numbers[i] = i + 1;

    for (int i = 0; i < 1000; i++)
    {
        for (int j = 0; j < 1000; j++)
        {
            if (j + 1 % test_numbers[i] == 0)
                table[i][j] = 0;
            else
            {
                int legendre_symbol = pow(j + 1, (test_numbers[i] - 1) / 2) % test_numbers[i];
                if (legendre_symbol == 1)
                    table[i][j] = 1;
                else
                    table[i][j] = -1;
            }
        }
    }

    ofstream file;
    file.open("kronecker_table.csv");
    file << "test_number";
    for (int i = 1; i <= 1000; i++) file << "," << i;
    file << "\n";
    for (int i = 0; i < 1000; i++)
    {
        file << test_numbers[i];
        for (int j = 0; j < 1000; j++)
        {
            file << "," << table[i][j];
        }
        file << "\n";
    }
    file.close
