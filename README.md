# SPOJ-Bitmap
Dynamic programming solution for the Bitmap problem in Python

Complexity of the algorithm: O(n*m)
The algorithm computes the distance for every cell with value 0 to the nearest cell with value 1. 
To do that a dp matrix will storage the calculated distance, dp[i,j] = value corresponding to the distance to the nearest cell with value 1 for the cell in the position (i,j).
We start with the dp matrix having values in the position (i,j) = 0 if dp[i,j] == 1 else n*m which is the maximum value posible.
We are going to do two pass throught the matrix, one in top-down direction and the second one in bottom-up direction. We need to do two pass because when you are in the (i,j) position
and assuming all the cells araound the (i,j) cell have value = 0 then because the travel is top-down dp[i+1,j] have the maximum value and maybe dp[i,j] could be calculated wrong.
Is enough if dp[i-1,j] = 3 and dp[i-1,j] are the lowest value calculated around the dp[i,j]. Assumming that dp[i+2,j] = 0 then dp[i,j] = 2 but have value 3.
