impl Solution {
    pub fn find_min_height_trees(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        if n == 1 {
            return vec![0];
        }
        let mut graph = vec![vec![]; n as usize];
        let mut degree = vec![0; n as usize];
        for edge in edges {
            let u = edge[0] as usize;
            let v = edge[1] as usize;
            graph[u].push(v);
            graph[v].push(u);
            degree[u] += 1;
            degree[v] += 1;
        }
        let mut leaves = Vec::new();
        for i in 0..n as usize {
            if degree[i] == 1 {
                leaves.push(i);
            }
        }
        let mut remaining = n;
        while remaining > 2 {
            remaining -= leaves.len() as i32;
            let mut new_leaves = Vec::new();
            for &leaf in &leaves {
                for &nei in &graph[leaf] {
                    degree[nei] -= 1;
                    if degree[nei] == 1 {
                        new_leaves.push(nei);
                    }
                }
            }
            leaves = new_leaves;
        }
        leaves.into_iter().map(|x| x as i32).collect()
    }
}
