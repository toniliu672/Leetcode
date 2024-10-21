impl Solution {
    pub fn check_record(n: i32) -> i32 {
        let MOD = 1_000_000_007;
        let mut dp = vec![vec![vec![0; 3]; 2]; n as usize + 1];
        dp[0][0][0] = 1;
        for i in 1..=n as usize {
            for a in 0..2 {
                for l in 0..3 {
                    dp[i][a][0] = (dp[i][a][0] + dp[i-1][a][l]) % MOD;
                }
            }
            for l in 0..3 {
                dp[i][1][0] = (dp[i][1][0] + dp[i-1][0][l]) % MOD;
            }
            for a in 0..2 {
                for l in 1..3 {
                    dp[i][a][l] = (dp[i][a][l] + dp[i-1][a][l-1]) % MOD;
                }
            }
        }
        let mut sum = 0;
        for a in 0..2 {
            for l in 0..3 {
                sum = (sum + dp[n as usize][a][l]) % MOD;
            }
        }
        sum
    }
}
