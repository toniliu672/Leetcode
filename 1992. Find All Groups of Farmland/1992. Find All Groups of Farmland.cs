public class Solution {
    public int[][] FindFarmland(int[][] land) {
        int m = land.Length, n = land[0].Length;
        var res = new List<int[]>();
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (land[i][j] == 1) {
                    int r2 = i;
                    while (r2 + 1 < m && land[r2 + 1][j] == 1) {
                        ++r2;
                    }
                    int c2 = j;
                    while (c2 + 1 < n && land[i][c2 + 1] == 1) {
                        ++c2;
                    }
                    for (int r = i; r <= r2; ++r) {
                        for (int c = j; c <= c2; ++c) {
                            land[r][c] = 0;
                        }
                    }
                    res.Add(new int[] {i, j, r2, c2});
                }
            }
        }
        return res.ToArray();
    }
}
