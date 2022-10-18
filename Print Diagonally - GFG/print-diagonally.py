#User function Template for python3

def downwardDigonal(N, A): 
    # code here 
    d = {}
    for i in range(N):
        for j in range(N):
            if (i+j) in d: 
                d[i+j].append(A[i][j])
            else:
                d[i+j]=[]
                d[i+j].append(A[i][j])
    ans = []
    for i in d:
        for j in d[i]:
            ans.append(j)
    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix =[]
        for i in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        ans = downwardDigonal(n,matrix)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends