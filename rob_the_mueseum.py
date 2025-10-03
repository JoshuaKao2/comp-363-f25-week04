
class Museum:

    def __optimal_subset_value(value:list[int], weight:list[int], Cmax:int) -> list[list[int]]:
        n = len(weight)
        
        # initializing the 2d array
        S = [[None for _ in range(Cmax + 1)] for _ in range(n + 1)]
        
        #sets the first row and column to 0
        for i in range(len(S[0])):
            S[0][i] = 0
        for i in range(len(S)):
            S[i][0] = 0    

        #sets the first row to the value of the first item as soon as it can fit.
        for index in range(len(S)):
            if weight[1] <= index:
                S[index][1] = value[1]
            else: 
                S[index][1] = 0

        # goes through the arrays starting from the 2nd row
        for i in range(2, n + 1):
            for j in range(1, Cmax + 1):
                #if the weight of the current item is greater than the carrying capacity,
                #make it the same as the previous.
                if weight[i] > j:
                    S[i][j] = S[i - 1][j]
                else:
                    #compare one with the item, and one without, and take which ever is better
                    without_item = S[i - 1][j]
                    with_item = S[i - 1][j - weight[i]] + value[i]
                    if without_item > with_item:
                        S[i][j] = without_item
                    else:
                        S[i][j] = with_item
        return S
        

    def __build_subset(value:list[int], weight:list[int], Cmax:int, S:list[list[int]]):
        subset = []
        n = len(value) - 1
        c = Cmax
        
        while n > 0 and c > 0:
            #checks if the item is in the best outcome
            #if the curent optimal is same as previous optimal,
            #then the item is not in optimal subset
            if S[n][c] != S[n - 1][c]:
                #if so, add it to the subset, and continue
                subset.append(n)
                c -= weight[n]
            n -= 1
        return subset