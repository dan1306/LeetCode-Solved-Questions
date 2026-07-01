#include <iostream>
#include <string> // Required for std::to_string
#include <algorithm>
class Solution {
public:
    int addDigits(int num) {

        while(num >= 10){
            std::string str = std::to_string(num);
            int sum = 0;
            for(int i = 0; i < str.length(); i++){
                sum += (str[i] - '0');
            }
            num = sum;
        }
        
        return num;
    }
};