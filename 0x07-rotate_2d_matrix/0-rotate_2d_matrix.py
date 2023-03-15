#!/usr/bin/python3
''' rotate  2D matrix '''

def rotate_2d_matrix(matrix):
    ''' rotate it 90 degrees clockwise '''
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            # topleft value
            topleft = matrix[top][left + i]
            #move bottom left to the top left
            matrix[top][left + i] = matrix[bottom - i][left]
            #move bottom right to the bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]
            # move top right to bottom right
            matrix[bottom][right - i] = matrix [top + i][right]
            # move top left to top right
            matrix[top + i][right] = topleft
        right -= 1
        lrft += 1
