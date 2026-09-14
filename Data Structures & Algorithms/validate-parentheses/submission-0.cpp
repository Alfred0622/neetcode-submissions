class Solution {
public:
    bool isValid(string s) {
        string stack = "" ;
        for (char c: s){
            if (c == '(' || c == '[' || c == '{'){
                stack.push_back(c);
            }

            else {
                int N = stack.size();
                if (N == 0){
                    return false;
                }

                else {
                    if (c == '}' && stack[N - 1] != '{'){
                        return false;
                    }

                    if (c == ']' && stack[N - 1] != '['){
                        return false;
                    }

                    if (c == ')' && stack[N - 1] != '('){
                        return false;
                    }

                    stack.pop_back();
                }

            }
        }

        if (stack.empty()) {
            return true;
        }
        else{
            return false;
        }
    }
};
