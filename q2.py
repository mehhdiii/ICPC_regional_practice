

def make_matrix(r, c, lst):
    mat = []
    for i in range(r):
        mat.append([])
        for j in range(c):
            mat[i].append(lst[0])
            lst = lst[1:]
    # print(mat)
    return mat

def mat_mul(m1, m2):
    out_m = []
    # for rindex, r1 in enumerate(m1): # rows of m1
    #     # multiply with every column
    #     for allcolums in range(row2)
    #     c2 = []
    #     for  in m2: # cols of m2
    #         m2_c = m2[]
    #         m1[r1] * m2[c2]
    m3 = []
    for i in range(len(m1)):
        result = []

        for j in range(len(m2[0])):
            ans= 0

            for k in range(len(m1[0])):
                ans+= m1[i][k]*m2[k][j]
            result.append(ans)

        m3.append(result)
    return m3


def trans(A):
    B = []
    for i in range(len(A[0])):
        res = []
        for j in range(len(A)):
            new = A[j][i]
            res.append(new)        
        B.append(res)
    # print(B)
    return B


def summer(m3):
    ans = 0
    for i in range(len(m3)):
        for j in range(len(m3[0])):
            ans += m3[i][j]

    return ans



n = int(input())
for i in range(n):
    testcase  = list(map(int, input().split(' ')))
    r1 = testcase[0]
    c1 = testcase[1]
    testcase = testcase[2:]
    mat1 = testcase[0:r1*c1]


    testcase = testcase[r1*c1:]
    r2 = testcase[0]
    c2 = testcase[1]
    # print(r2, c2)
    
    testcase = testcase[2:]
    mat2 = testcase[0:r2*c2]

    m1 = make_matrix(r1,c1, mat1)
    m2 = make_matrix(r2, c2, mat2)
    print('Case #', i+1, ': ',sep='', end='')
    if c1!=r2:
        if c1==c2:
            m2 = trans(m2)
            
        else:
            print('Not possible')
            continue

    out = mat_mul(m1,m2)
    # out = transposed(m1, m2)
    out = summer(out)
    print(out)
    #3 4 1 2 3 4 5 6 7 8 9 10 11 12 3 4 1 0 3 4 5 6 1 8 0 0 0 12