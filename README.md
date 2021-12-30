# genshin_impact
Scripts and solvers


   
### A solver for those infuriating puzzles.
### Enter the effect map (what cubes affect what other cubes) in the format [[cubes_affected] for cube in cubes]
### For example, if hitting cube 0 affects 0,1 and 1 affects 0,1,2, and 2 affects 1,2,3, and 3 affects 2,3, you'll use:
### [[0,1],[0,1,2],[1,2,3],[2,3]].
### The "Max_iterations" parameter on the solve method is to avoid max recursion depth issues. I used 20, but some of these cubes are freaking terrible.
