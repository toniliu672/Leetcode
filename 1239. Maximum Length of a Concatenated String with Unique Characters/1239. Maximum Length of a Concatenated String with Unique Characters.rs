impl Solution {
    pub fn max_length(arr: Vec<String>) -> i32 {
        fn is_unique(s: &str) -> bool {
            let mut chars = vec![false; 26];
            for ch in s.chars() {
                if chars[ch as usize - 'a' as usize] {
                    return false;
                }
                chars[ch as usize - 'a' as usize] = true;
            }
            true
        }

        fn backtrack(arr: &Vec<String>, index: usize, current: &str) -> i32 {
            if !is_unique(current) {
                return 0;
            }

            let mut max_length = current.len() as i32;

            for i in index..arr.len() {
                let mut new_current = current.to_string();
                new_current.push_str(&arr[i]);
                max_length = max_length.max(backtrack(arr, i + 1, &new_current));
            }

            max_length
        }

        backtrack(&arr, 0, "")
    }
}


