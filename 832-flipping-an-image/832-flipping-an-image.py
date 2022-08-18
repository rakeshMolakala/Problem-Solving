class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        # for i in range(m):
        #     image[i] = image[i][::-1]
        #     for j in range(n):
        #         if(image[i][j]==1):
        #             image[i][j]=0
        #         else:
        #             image[i][j]=1
        
        def invert(i,j):
            if(image[i][j]==1):
                image[i][j] = 0
            else:
                image[i][j] = 1
                
        for i in range(m):
            for j in range((n+1)//2):
                invert(i,j)
                if(j!=n-j-1):
                    invert(i,n-j-1)
                    image[i][j], image[i][n-j-1] = image[i][n-j-1], image[i][j]    
        return image
                

                
        