def permutations(S, k, U):
    for i in range(len(U)):
        S.append(U[i])
        if k == 1:
            print(S)
        else:
            permutations(S, k - 1, U[:i] + U[i+1:])
        S.pop()

permutations([], 3, [1,2,3])