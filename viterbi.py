def viterbi(Obs, E, P):
    N = len(Obs)
    K = len(E)
    
    # Initialisation
    T1 = [[0] * N for _ in range(K)]
    T2 = [[0] * N for _ in range(K)]
    
    # Initial probabilities
    for i in range(K):
        T1[i][0] = E[Obs[0]][i]
        T2[i][0] = 0
    
    # Dynamic programming
    for j in range(1, N):
        for i in range(K):
            max_prob = float('-inf')
            max_state = 0
            for k in range(K):
                prob = T1[k][j-1] * P[k][i] * E[Obs[j]][i]
                if prob > max_prob:
                    max_prob = prob
                    max_state = k
            T1[i][j] = max_prob
            T2[i][j] = max_state
    
    # Backtracking
    max_prob = float('-inf')
    last_state = 0
    for i in range(K):
        if T1[i][N-1] > max_prob:
            max_prob = T1[i][N-1]
            last_state = i
    
    sequence = [0] * N
    sequence[N-1] = last_state
    for j in range(N-2, -1, -1):
        sequence[j] = T2[sequence[j+1]][j+1]
    
    return sequence

# Exemple d'utilisation
Obs = [2, 0]
E = [[0.7, 0.2, 0.3], [0.2, 0.7, 0.1], [0.1, 0.1, 0.6]]
P = [[0.3, 0.2, 0.5], [0.4, 0.4, 0.2], [0.2, 0.3, 0.5]]

decoded_sequence = viterbi(Obs, E, P)
print(f"Decoded sequence: {decoded_sequence}")