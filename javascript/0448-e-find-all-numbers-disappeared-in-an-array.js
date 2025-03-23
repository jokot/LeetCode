// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    const result = [];
    const numsSet = new Set(nums);

    for(let i = 1; i < nums.length+1; i = i+1) {
        if (!numsSet.has(i)) {
            result.push(i);
        }
    }

    return result;
};