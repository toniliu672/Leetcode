impl Solution {
    pub fn longest_ideal_string(s: String, k: i32) -> i32 {
        let mut dp = vec![0; 26];
        let k = k as u8;
        
        for ch in s.bytes() {
            let ch = ch - b'a';
            let mut max_val = 0;
            
            for i in ch.saturating_sub(k)..=ch.saturating_add(k).min(25) {
                max_val = max_val.max(dp[i as usize]);
            }
            
            dp[ch as usize] = max_val + 1;
        }
        
        dp.into_iter().max().unwrap_or(0)
    }
}
