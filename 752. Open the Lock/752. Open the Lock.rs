use std::collections::HashSet;
use std::collections::VecDeque;

impl Solution {
    pub fn open_lock(deadends: Vec<String>, target: String) -> i32 {
        let deadends: HashSet<String> = deadends.into_iter().collect();
        if deadends.contains("0000") {
            return -1;
        }
        let mut queue = VecDeque::new();
        queue.push_back(("0000".to_string(), 0));
        let mut visited = HashSet::new();
        visited.insert("0000".to_string());
        while let Some((node, depth)) = queue.pop_front() {
            if node == target {
                return depth;
            }
            for i in 0..4 {
                for d in [-1, 1].iter() {
                    let mut next_node = node.clone();
                    let digit = ((next_node.remove(i).to_digit(10).unwrap() as i32 + d + 10) % 10) as u32;
                    next_node.insert(i, std::char::from_digit(digit, 10).unwrap());
                    if !visited.contains(&next_node) && !deadends.contains(&next_node) {
                        queue.push_back((next_node.clone(), depth + 1));
                        visited.insert(next_node);
                    }
                }
            }
        }
        -1
    }
}
