#include <iostream>

long long delit_prod(long long n){
    int counter = 0;
    long long acc = 1;
    for(long long i = 2; i <=(n/2); i++) {
        if (n % i == 0){
            acc *= i;
            counter ++;
        }
        if (counter == 5){
            return acc;
        }
    }
    return 0;
}


int main() {
    long long a = 247000000;
    long long b = 10000000000;
    for (long long i = a; i < b; i++){
        long long prod = delit_prod(i);
        if ((prod % 100 == 52) && (prod < i)){
            std::cout << prod << " " << i << std::endl;
        }
    }
}
