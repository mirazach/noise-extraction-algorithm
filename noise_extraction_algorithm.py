import numpy as np

#creating dummy matrix 
mat = np.array([[4,4,4,3,10],
                [7,6,10,5,1],
                [7,4,0,7,4],
                [0,8,7,4,9],
                [2,2,5,9,7],
                [7,0,9,7,7],
                [9,9,8,4,8],
                [8,7,1,3,9],
                [7,0,6,2,8],
                [10,7,4,7,7]])

#printing matrix 
print(mat) 

#storing the number of column and rows
m = mat.shape[1] #columns
n = mat.shape[0] #rows
nm = n*m


#SYSTEM NOISE FUNCTION
def system(matrix): 
    all_terms = [] #creating an empty list to store values 
    
    for i in range(0,n): #i loop (summing rows)
        
        for j in range(0, m): #j loop (summing columns)
        
            x_ij = matrix[i,j]  #getting the matrix value in the i-th row and j-th column
            mu_j = matrix[:,j].mean() #calculating the mean of the j-th column
            
            term = (x_ij - mu_j)**2 #squaring the term 
            
            all_terms.append(term) #appending value to the list 
    
    return sum(all_terms)/nm #dividing sum of all terms by the number of entries in the matrix
    
    
#LEVEL NOISE FUNCTION
def level(matrix): 
    all_terms = [] #creating an empty list to store values 
    
    for i in range(0,n): #i loop (summing rows)
        
        mu_i = matrix[i,:].mean() #calculating the mean of the i-th row
        mu = matrix.mean()#calculating the overall mean of the matrix 
        
        term = (mu_i - mu)**2 #squaring the term
        
        all_terms.append(term) #appending value to the list 
    
    return sum(all_terms)/n #dividing sum of all terms by number of rows
    

#PATTERN NOISE FUNCTION
def pattern(matrix): 
    all_terms = [] #creating an empty list to store values 
    
    for i in range(0,n): #i loop (summing rows)
        
        for j in range(0, m): #j loop (summing columns)
        
            x_ij = matrix[i,j]  #getting the matrix value in the i-th row and j-th column
            mu_j = matrix[:,j].mean() #calculating the mean of the j-th column
            mu_i = matrix[i,:].mean() #calculating the mean of the i-th row
            mu = matrix.mean()#calculating the overall mean of the matrix 
            
            
            term = (x_ij - mu_j - mu_i + mu)**2 #squaring the term 
            
            all_terms.append(term) #appending value to the list 
    
    return sum(all_terms)/nm #dividing sum of all terms by the number of entries in the matrix

#Printing results
print('Results')    
print('System Noise:'+ str(round(system(mat), 2)))
print('Level Noise:' + str(round(level(mat), 2)))
print('Pattern Noise:' + str(round(pattern(mat), 2)))

print('') 

#checking that the equation holds
print('Checking that they are equal:')
print('System = ' + str(round(system(mat), 5)))
print('Level + Pattern = ' + str(round(level(mat) + pattern(mat), 5)))

