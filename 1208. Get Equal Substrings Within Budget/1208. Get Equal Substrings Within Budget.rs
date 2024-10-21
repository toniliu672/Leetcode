impl Solution {
    pub fn equal_substring(s: String, t: String, max_cost: i32) -> i32 {
        let n = s.len();
        let s_bytes = s.as_bytes();
        let t_bytes = t.as_bytes();
        
        let mut max_len = 0;
        let mut current_cost = 0;
        let mut start = 0;
        
        for end in 0..n {
            current_cost += (s_bytes[end] as i32 - t_bytes[end] as i32).abs();
            
            while current_cost > max_cost {
                current_cost -= (s_bytes[start] as i32 - t_bytes[start] as i32).abs();
                start += 1;
            }
            
            max_len = max_len.max((end - start + 1) as i32);
        }
        
        max_len
    }
}
