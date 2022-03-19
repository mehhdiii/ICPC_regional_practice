def make_matrix(r, c):
    mat = []
    for i in range(r):
        mat.append([])
        for j in range(c):
            mat[i].append(0)
            
    return mat


def dp(tel, dust,r, c):
    visited = make_matrix(r, c) 
    counting_dict = {}

    # for i in range(len(tel)):
    i = 0
    while i <len(tel):
        j = 0
        while j < len(tel[0]):
        # for j in range(len(tel[0])):
            if tel[i][j]==0: 
                visited[i][j] = 1
                
            else:
                count_i_jump = 1
                if visited[i][j]==0:
                    lst = [(i, j)]
                    counting_dict[(i, j)]=0
                    while(len(lst)!=0):
                        current = lst.pop()
                        row = current[0]
                        col = current[1]
                        if tel[row][col]!=0 and visited[row][col]!=1:
                            visited[row][col] = 1
                            if tel[row][col]==2 and dust[row][col]!=1:
                                counting_dict[(i, j)]+=1    
                            if col + 1 < len(tel[0]): 
                                if tel[row][col+1]!=0:
                                    lst.append((row, col+1))
                                    count_i_jump+=1
                                    
                            if row + 1 < len(tel[0]): 
                                if tel[row + 1][col]!=0:
                                    lst.append((row + 1, col))
            j+=1
                                    
        i+=count_i_jump
    return counting_dict
                            
                        

                
                



n = int(input())

for i in range(n):
    rc = list(map(int, input().split(' ')))

    r = rc[0]
    c = rc[1]
    tel = []
    for x in range(r):
        rows = list(map(int, input().split(' ')))
        tel.append(rows)
    
    dust = []
    for x in range(r):
        rows = list(map(int, input().split(' ')))
        dust.append(rows)
    
    out = dp(tel, dust,r, c)
    
    for k in out.keys():
        if out[k]==1:
            print('Galaxy starting at ', k[0], ' ', k[1], ' has ', out[k], ' planet.', sep='')
        else:
            print('Galaxy starting at ', k[0], ' ', k[1], ' has ', out[k], ' planets.', sep='')