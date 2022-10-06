
#creating dummy matrix
data <- c(4,4,4,3,10,7,6,10,5,1,7,4,0,7,4,0,8,7,4,9,2,2,5,9,7,7,0,9,7,7,
          9,9,8,4,8,8,7,1,3,9,7,0,6,2,8,10,7,4,7,7)

mat <- matrix(data, ncol=5, nrow=10, byrow=TRUE)

#printing matrix
print(mat)
          

#storing the number of column and rows
m <- ncol(mat)
n <- nrow(mat)
nm <- n*m


#SYSTEM NOISE FUNCTION
system <- function(matrix) {
  
  all_terms <- c() #creating an empty list to store values
  
  for (i in seq(1,n)) { #i loop (summing rows)
    
    for (j in seq(1:m)) { #j loop (summing columns)
      
      x_ij <- mat[i,j]  #getting the matrix value in the i-th row and j-th column
      mu_j <- mean(mat[,j]) #calculating the mean of the j-th column
      
      term <- (x_ij - mu_j)^2 #squaring the term 
      
      all_terms <- append(all_terms, term) #appending value to the list 
    }

  }
  
  return(sum(all_terms)/nm) #dividing sum of all terms by the number of entries in the matrix
  
}

#LEVEL NOISE FUNCTION
level <- function(matrix) {
  
  all_terms <- c() 
  
  for (i in seq(1:n)) { #i loop (summing rows)
    
    mu_i <- mean(mat[i,]) #calculating the mean of the i-th row
    mu <- mean(mat) #calculating the overall mean of the matrix 
    
    term <- (mu_i - mu)^2 #squaring the term
    all_terms <- append(all_terms, term)
    
  }
  
  return(sum(all_terms)/n) #dividing sum of all terms by number of rows
  
}

#PATTERN NOISE FUNCTION
pattern <- function(matrix) {
  
  all_terms <- c() 
  
  for (i in seq(1,n)) { #i loop (summing rows)

    for (j in seq(1,m)) { #j loop (summing columns)
      
      x_ij <- mat[i,j] #getting the matrix value in the i-th row and j-th column
      mu_j <- mean(mat[,j]) #calculating the mean of the j-th column
      mu_i <- mean(mat[i,]) #calculating the mean of the i-th row
      mu <- mean(mat) #calculating the overall mean of the matrix
      
      term <- (x_ij - mu_j - mu_i + mu)^2 #squaring the term
      all_terms <- append(all_terms, term)
  
    }    
  }
  
  return(sum(all_terms)/nm) #dividing sum of all terms by the number of entries in the matrix
}

#Printing results
paste0('System Noise:', system(mat))

paste0('Level Noise:', level(mat))
paste0('Pattern Noise:', pattern(mat))

#checking that equation holds
system(mat) == level(mat) + pattern(mat)
