impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        let final_xor = nums.iter().fold(0, |acc, &num| acc ^ num);
        (final_xor ^ k).count_ones() as i32
    }
}
