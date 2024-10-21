impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        if s.is_empty() {
            return "".to_string();
        }

        let s_chars: Vec<char> = s.chars().collect();
        let mut start = 0;
        let mut end = 0;

        fn expand_around_center(s_chars: &Vec<char>, left: i32, right: i32) -> (i32, i32) {
            let (mut l, mut r) = (left, right);
            while l >= 0 && r < s_chars.len() as i32 && s_chars[l as usize] == s_chars[r as usize] {
                l -= 1;
                r += 1;
            }
            (l + 1, r - 1)
        }

        for i in 0..s_chars.len() {
            let (left1, right1) = expand_around_center(&s_chars, i as i32, i as i32);
            let (left2, right2) = expand_around_center(&s_chars, i as i32, (i + 1) as i32);

            if right1 - left1 > end - start {
                start = left1;
                end = right1;
            }
            if right2 - left2 > end - start {
                start = left2;
                end = right2;
            }
        }

        s_chars[start as usize..=end as usize].iter().collect()
    }
}

