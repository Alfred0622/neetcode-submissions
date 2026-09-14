class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> existed;
        int N = nums.size();
        for (int i = 0; i < N ; ++i){
            if (existed.count(nums[i]) > 0){
                return true;
            }

            existed.insert(nums[i]);
        }

        return false;
    }
};