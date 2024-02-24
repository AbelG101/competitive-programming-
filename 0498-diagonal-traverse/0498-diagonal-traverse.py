class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        # initialize an empty dict to store diagonals
        # get number of rows and columns in the matrix
        # loop through each cell in the matrix
            # calc the sum of row and column indices to get the diagonal
            # check if diagonal sum is already present in dict
                # if not, initialize an empty list for that diagonal
            # add the current element to the diagonal dict, list value
                # if diagonal sum is even, insert element at the beginning of the list (to reverse it later)
                # if diagonal sum is odd, append element to the end of the list
        # concatenate all diagonal lists into a single list & return that
        
        diagonal_dict = {}
        rows = len(mat)
        cols = len(mat[0])

        # loop through the matrix
        for i in range(rows):
            for j in range(cols):
                diagonal_sum = i + j
                # if no entry in dict for sum of indices, create one
                if diagonal_sum not in diagonal_dict:
                    diagonal_dict[diagonal_sum] = []
                # add element to the diagonal list
                if diagonal_sum % 2 == 0:
                    diagonal_dict[diagonal_sum].insert(0, mat[i][j])
                else:
                    diagonal_dict[diagonal_sum].append(mat[i][j])

        ans = [elem for sublist in diagonal_dict.values() for elem in sublist]
        return ans