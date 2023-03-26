#include<iostream>
#include<cmath>

using namespace std;

long double calculate_pi(int n) {
    long double migpi = 0.0;
    long double terme = 1.0;

    for (int i = 1; i < n; ++i) {
        migpi += terme;
        terme = terme * i/(i*2.0+1.0); 
    }

    return 2*migpi;
}

int main() {
    cout.setf(ios::fixed);
    cout.precision(59);

    int digits;
    cin >> digits;
    if (digits == -1) digits = 1000000;
    long double calculated_pi = calculate_pi(digits);

    cout << calculated_pi << endl;
    cout << M_PI << endl;
}