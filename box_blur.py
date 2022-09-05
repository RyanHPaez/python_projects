def solution(image):
    sum=0
    matrix=[]
    start=0
    for i in range(0,len(image)-2):
        row = []
        for j in range(0,len(image[i])-2):
            sum=0
            for k in range(i,i+3):
                for l in range(j,j+3):
                    sum+=image[k][l]
            row.append(sum//9)
        matrix.append(row)

    return matrix
image = [[1, 1, 1], 
         [1, 7, 1], 
         [1, 1, 1]]
print(solution(image))