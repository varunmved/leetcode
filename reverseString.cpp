void reverseStr(string &str)
{
    char * tortoise;
    char * hare;
    string res = "";
    int sizeOfArr = str.size();
    stack words <string>;

    for(int i = 0; i < sizeOfArr; i++)
    {
        if(str[i] == ' ')
        {
            hare = str[i];
            stack.push(str.range(tortoise,hare));
            tortoise = hare;
        }
    }

    while(words != NULL)
    {
        print(words.pop() + " ");
        words = words -> next;
    }
}
