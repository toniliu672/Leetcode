impl Solution {
    pub fn find_farmland(mut land: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = land.len();
        let n = land[0].len();
        let mut res = vec![];
        for i in 0..m {
            for j in 0..n {
                if land[i][j] == 1 {
                    let mut r2 = i;
                    while r2 + 1 < m && land[r2 + 1][j] == 1 {
                        r2 += 1;
                    }
                    let mut c2 = j;
                    while c2 + 1 < n && land[i][c2 + 1] == 1 {
                        c2 += 1;
                    }
                    for r in i..=r2 {
                        for c in j..=c2 {
                            land[r][c] = 0;
                        }
                    }
                    res.push(vec![i as i32, j as i32, r2 as i32, c2 as i32]);
                }
            }
        }
        res
    }
}
