#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

#Below example with Sierpinski numbers
void compute_kronecker_symbol_table() {
    vector<int> kronecker_input = { 78557,271129,271577,322523,327739,482719,575041,
 603713,903983,934909,965431,1259779,1290677,
 1518781,1624097,1639459,1777613,2131043,2131099,
 2191531,2510177,2541601,2576089,2931767,2931991,
 3083723,3098059,3555593,3608251 };
    vector<vector<int>> table;
    for (int p : kronecker_input) {
        vector<int> row;
        for (int a = 1; a <= 100000; a++) {
            if (a % p == 0) {
                row.push_back(0);
            }
            else {
                int kronecker_symbol = (int)(pow(a, (p - 1) / 2)) % p;
                if (kronecker_symbol == 1) {
                    row.push_back(1);
                }
                else {
                    row.push_back(-1);
                }
            }
        }
        table.push_back(row);
    }

    ofstream csvfile;
    csvfile.open("Sierpinski_values.csv");
    csvfile << "p";
    for (int a = 1; a <= 100000; a++) {
        csvfile << "," << a;
    }
    csvfile << endl;
    for (int i = 0; i < kronecker_input.size(); i++) {
        csvfile << kronecker_input[i];
        for (int j = 0; j < 100000; j++) {
            csvfile << "," << table[i][j];
        }
        csvfile << endl;
    }
    csvfile.close();
}

int main() {
    compute_kronecker_symbol_table();
    return 0;
}
