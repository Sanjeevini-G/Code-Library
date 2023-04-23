def countParenth(symbols, operators):
    n = len(symbols)
    F = [[0 for i in range(n)] for j in range(n)]
    T = [[0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        F[i][i] = 1 if symbols[i] == 'F' else 0
        T[i][i] = 1 if symbols[i] == 'T' else 0
    
    for gap in range(1, n):
        i = 0
        for j in range(gap, n):
            T[i][j] = F[i][j] = 0
            for g in range(gap):
                k = i + g
                
                tik = T[i][k] + F[i][k]
                tkj = T[k+1][j] + F[k+1][j]
                
                if operators[k] == '&':
                    T[i][j] += T[i][k] * T[k+1][j]
                    F[i][j] += (tik * tkj - T[i][k] * T[k+1][j])
                elif operators[k] == '|':
                    F[i][j] += F[i][k] * F[k+1][j]
                    T[i][j] += (tik * tkj - F[i][k] * F[k+1][j])
                elif operators[k] == '^':
                    T[i][j] += F[i][k] * T[k+1][j] + T[i][k] * F[k+1][j]
                    F[i][j] += T[i][k] * T[k+1][j] + F[i][k] * F[k+1][j]
            i += 1
    
    return T[0][n-1]
