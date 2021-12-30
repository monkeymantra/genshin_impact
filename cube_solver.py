### A solver for those infuriating puzzles.
### Enter the effect map (what cubes affect what other cubes) in the format [[cubes_affected] for cube in cubes]
### For example, if hitting cube 0 affects 0,1 and 1 affects 0,1,2, and 2 affects 1,2,3, and 3 affects 2,3, you'll use:
### [[0,1],[0,1,2],[1,2,3],[2,3]].
### The "Max_iterations" parameter on the solve method is to avoid max recursion depth issues. I used 20, but some of these cubes are freaking terrible.

from enum import IntEnum
from math import inf

class CubeState(IntEnum):
    T=0
    RT=1
    B=2
    LT=3
    
    def rotated(self):
        if int(self) == 3:
            return CubeState(0)
        else:
            return CubeState(int(self)+1)
    

class GenshinCube:
    
    def __init__(self, effect_map: list[list[int]]):
        self.effect_map = effect_map
        
    def hit_cube(self, cube_hit, states):
        new_states = [CubeState(int(s)) for s in states]
        affected = self.effect_map[cube_hit]
        for cube_number in affected:
            new_states[cube_number] = new_states[cube_number].rotated()
        return new_states
    
    def solved(self, states):
        for state in states:
            if int(state) != 0:
                return False
        return True
    
    def solve(self, states, max_iterations=20):
        solutions = []
        memo = set()
        def solve_cubes(states: list[CubeState], cube_hit, solution_so_far=[], max_i=20):
            if len(solution_so_far) > max_i:
                return
            memo.add((cube_hit, tuple([int(s) for s in states])))
            new_states = self.hit_cube(cube_hit, states)
            so_far = solution_so_far + [cube_hit]
            if self.solved(new_states):    
                solutions.append(so_far)
                return
            elif max_iterations == 0:
                return
            else:
                for to_hit in range(len(new_states)):
                    if (to_hit, tuple([int(s) for s in new_states])) not in memo:
                        solve_cubes(new_states, to_hit, so_far, max_iterations - 1)
                        
        for idx, _ in enumerate(states):
            solve_cubes(states,  cube_hit=idx, solution_so_far=[], max_i=max_iterations-1)
        
        min_length = inf
        min_sol = None
        for sol in solutions:
            if len(sol) < min_length:
                min_sol = sol
        for cube in min_sol:
            print("Hit ", cube)
        return min_sol
    
if __name__ == "__main__":
  pass
  # For now, you can write this part yourself :P
