#include <stdio.h>

string numbersToWords(int num)
{
    stack nums = new stack; //lol syntax tho
    int count = 0;
    string answer = "";
    //count gives us size of int
    // append to a stack that has the digit
    while(num >= 0)
    {
        num/=10;
        count++;
        nums.push(num);
    }

    while(count >0)
    {
        int res = stack.pop();
        string prfX = prefix.lookup_value(res);
        string sufX = prefix + suffix.lookup_value(count);
        answer += (sufX);
        count --;
    }

    return answer.reverse();



}
