
class Museum:

    def __optimal_subset_value(value:list[int], weight:list[int], Cmax:int) -> list[list[int]]:
        n = len(weight)
        
        # initializing the 2d array
        S = [[None for _ in range(Cmax + 1)] for _ in range(n + 1)]
        
        #sets the first row and column to 0
        for i in range(len(S[0])):
            S[0][i] = 0
        for i in len(S):
            S[i][0] = 0    

        #sets the first row to the value of the first item as soon as it can fit.
        for index in range(len(S)):
            if weight[1] <= index:
                S[index][1] = value[1]


        for i in range(2, n + 1):
            for j in range(1, Cmax + 1):
                if weight[i] > j:
                    S[i][j] = S[i - 1][j]
                else:
                    without_item = S[i - 1][j]
                    with_item = S[i - 1][j - weight[i]] + value[i]
                    S[i][j] = max(without_item, with_item)
        return S
        

        





# def __build_subset(...):
#     subset = []
#     # iterate backwards through S to find which items are included
#     # ... your code here ...
#     return subset





