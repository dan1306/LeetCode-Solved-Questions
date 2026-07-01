#include <iostream>
#include <cstring>     // For std::strlen
#include <string_view> // For std::string_view
#include <string> // Required for std::string
#include <algorithm> // For std::max

class Solution {
public:
    string addBinary(string a, string b) {
        std::string dynamicStr = "";

        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;

        while(i >= 0 || j >= 0 || carry > 0){
            int sum = carry;

            if(i >= 0){
                sum += (a[i] - '0');
                i -= 1;
            }

            if(j>= 0){
                sum += (b[j] - '0');
                j -= 1;
            }
            
            dynamicStr += (sum % 2 == 0 ? '0' : '1');
            carry = sum / 2;
        }

        std::reverse(dynamicStr.begin(), dynamicStr.end());
        return dynamicStr;

    }

};