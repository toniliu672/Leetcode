public class Solution {
    public IList<int> FindMinHeightTrees(int n, int[][] edges) {
        if (n == 1) {
            return new List<int> {0};
        }
        List<int>[] graph = new List<int>[n];
        int[] degree = new int[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new List<int>();
        }
        foreach (var edge in edges) {
            int u = edge[0];
            int v = edge[1];
            graph[u].Add(v);
            graph[v].Add(u);
            degree[u]++;
            degree[v]++;
        }
        List<int> leaves = new List<int>();
        for (int i = 0; i < n; i++) {
            if (degree[i] == 1) {
                leaves.Add(i);
            }
        }
        while (n > 2) {
            n -= leaves.Count;
            List<int> newLeaves = new List<int>();
            foreach (var leaf in leaves) {
                foreach (var nei in graph[leaf]) {
                    degree[nei]--;
                    if (degree[nei] == 1) {
                        newLeaves.Add(nei);
                    }
                }
            }
            leaves = newLeaves;
        }
        return leaves;
    }
}
