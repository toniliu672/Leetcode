use std::collections::HashMap;

impl Solution {
    pub fn max_score_words(words: Vec<String>, letters: Vec<char>, score: Vec<i32>) -> i32 {
        fn calculate_word_score(word: &str, score: &Vec<i32>) -> i32 {
            word.chars().map(|ch| score[ch as usize - 'a' as usize]).sum()
        }

        fn can_form_word(word: &str, available: &HashMap<char, i32>) -> bool {
            let mut word_count = HashMap::new();
            for ch in word.chars() {
                *word_count.entry(ch).or_insert(0) += 1;
            }
            for (ch, &count) in word_count.iter() {
                if available.get(&ch).cloned().unwrap_or(0) < count {
                    return false;
                }
            }
            true
        }

        fn backtrack(
            index: usize,
            words: &Vec<String>,
            available: &mut HashMap<char, i32>,
            current_score: i32,
            score: &Vec<i32>,
        ) -> i32 {
            if index == words.len() {
                return current_score;
            }

            let mut max_score = backtrack(index + 1, words, available, current_score, score);

            let word = &words[index];
            if can_form_word(word, available) {
                let word_score = calculate_word_score(word, score);
                for ch in word.chars() {
                    *available.get_mut(&ch).unwrap() -= 1;
                }
                max_score = max_score.max(backtrack(index + 1, words, available, current_score + word_score, score));
                for ch in word.chars() {
                    *available.get_mut(&ch).unwrap() += 1;
                }
            }

            max_score
        }

        let mut available = HashMap::new();
        for ch in letters {
            *available.entry(ch).or_insert(0) += 1;
        }

        backtrack(0, &words, &mut available, 0, &score)
    }
}

