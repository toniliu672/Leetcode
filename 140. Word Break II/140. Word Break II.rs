impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> Vec<String> {
        let s = s.chars().collect::<Vec<_>>();
        let word_dict = word_dict.into_iter().collect::<std::collections::HashSet<_>>();
        let mut dp = vec![vec![]; s.len() + 1];
        dp[0].push(vec![]);
        for i in 1..=s.len() {
            for j in 0..i {
                if dp[j].is_empty() { continue }
                let word = s[j..i].iter().collect::<String>();
                if word_dict.contains(&word) {
                    let sentences = dp[j].clone();
                    for each in sentences {
                        let mut new = each;
                        new.push(word.clone());
                        dp[i].push(new);
                    }
                }
            }
        }
        dp[s.len()].iter().map(|v| v.join(" ")).collect()
    }
}
