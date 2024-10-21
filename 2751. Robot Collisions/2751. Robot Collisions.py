class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted(zip(positions, healths, directions, range(len(positions))), key=lambda x: x[0])
        stack = []
        
        for pos, health, dir, idx in robots:
            if dir == 'R':
                stack.append((pos, health, dir, idx))
            else:
                while stack and stack[-1][2] == 'R' and health > 0:
                    prev_pos, prev_health, prev_dir, prev_idx = stack[-1]
                    if prev_health > health:
                        health = 0
                        stack[-1] = (prev_pos, prev_health - 1, prev_dir, prev_idx)
                    elif prev_health < health:
                        health -= 1
                        stack.pop()
                    else:
                        health = 0
                        stack.pop()
                if health > 0:
                    stack.append((pos, health, dir, idx))
        
        surviving_robots = sorted(stack, key=lambda x: x[3])
        return [health for pos, health, dir, idx in surviving_robots]