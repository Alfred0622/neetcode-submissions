class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        std::map<char, int> count1;
        std::map<char, int> count2;


        for (char c: s){
            if (count1.count(c) >= 0){
                count1[c] += 1;
            }

            else{
                count1[c] = 1;
            }
        }

        for (char c: t){
            if (count2.count(c) > 0){
                count2[c] += 1;
            }

            else{
                count2[c] = 1;
            }
        }

        for (const auto& pair : count1) {
            char key= pair.first;
            if (count2.count(key) == 0){
                return false;
            }

            else if (count1[key] != count2[key]){
                return false;
            }

        
    }
        return true;
    }
};
