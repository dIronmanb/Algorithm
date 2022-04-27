matrix = [ [6,  7,  12, 5 ], 
           [5,  3,  11, 18],
           [7,  17, 3,  3 ],
           [8,  10, 14, 9 ]]

cost_table = [[0 for _ in range(len(matrix[0]) + 1)] \
                 for _ in range(len(matrix) + 1)]

for j in range(1, len(cost_table)):
    for i in range(1, len(cost_table[0])):
        
        # if j == 0 or i == 0:
        #     cost_table = [j][i] = 0
        # 이미 0으로 table을 만들었기 때문에 모서리를 굳이 0으로 다시
        # 처리하지 않아도 된다.
        
        cost_table[j][i] = matrix[j-1][i-1] + \
                max(cost_table[j - 1][i], cost_table[j][i-1]) 

print("(result of cost table)")
for j in cost_table:
    print(j)
    
print("the max cost value({}, {}) is {}".format(len(matrix), len(matrix[0]), cost_table[len(matrix)][len(matrix[0])] ))