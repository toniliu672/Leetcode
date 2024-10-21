public class Solution {
    public int OpenLock(string[] deadends, string target) {
        var dead = new HashSet<string>(deadends);
        var queue = new Queue<(string, int)>();
        queue.Enqueue(("0000", 0));
        var seen = new HashSet<string> {"0000"};
        
        while (queue.Count > 0) {
            var (node, depth) = queue.Dequeue();
            if (node == target) return depth;
            if (dead.Contains(node)) continue;
            for (var i = 0; i < 4; ++i) {
                for (var d = -1; d <= 1; d += 2) {
                    var newNode = node.ToCharArray();
                    newNode[i] = (char)(((newNode[i] - '0') + d + 10) % 10 + '0');
                    var next = new string(newNode);
                    if (seen.Add(next)) queue.Enqueue((next, depth + 1));
                }
            }
        }
        return -1;
    }
}
