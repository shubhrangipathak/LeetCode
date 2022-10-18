
def downwardDigonal(N, A): 
    # code here 
    ans = []
    for i in range(0,N):
        if(i==0):
            start=0
        else:
            start=N-1
            
        for j in range(start,N):
            x=i
            y=j
            while(i!=y+1):
                ans.append(A[x][y])
                x=x+1
                y=y-1

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