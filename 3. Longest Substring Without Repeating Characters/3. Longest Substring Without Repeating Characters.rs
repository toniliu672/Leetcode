impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        use std::collections::HashMap;

        let mut char_map = HashMap::new();
        let mut max_length = 0;
        let mut start = 0;

        for (end, ch) in s.chars().enumerate() {
            if let Some(&index) = char_map.get(&ch) {
                if index >= start {
                    start = index + 1;
                }
            }
            char_map.insert(ch, end);
            max_length = max_length.max(end - start + 1);
        }

        max_length as i32
    }
}
