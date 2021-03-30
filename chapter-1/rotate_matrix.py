# 7 - Rotate Matrix - rotate_matrix.py 
# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes
# write a method to rotate the image by 90 degrees. Can you do this in place?

input_image = [
    [0,0,0,1], # 0,[0] -> [0],3 | 0,[1] -> [1],3 | 0,[2] -> [2],3 | 0,[3] -> [3],3 
    [0,0,1,0], # 1,[0] -> [0],2 | [,[1] -> [1],2 | 1,[2] -> [2],2 | 1,[3] -> [3],2 
    [0,1,0,0], # 2,[0] -> [0],1 | 2,[1] -> [1],1 | 2,[2] -> [2],1 | 2,[3] -> [3],1 
    [1,0,0,0]  # 3,[0] -> [0],0 | 3,[1] -> [1],0 | 3,[2] -> [2],0 | 3,[3] -> [3],0 
]

image_rotated = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
]

def rotate_image(img):
    rows = len(img)
    cols = len(img[0])
    
    # initialize matrix 
    output = []
    for i in range(rows):
        output.append([9] * cols)

    # create output matrix
    for i in range(rows):
        for j in range(cols):
            output[i][j] = img[j][(cols-i-1)]

    return output

if rotate_image(input_image) == image_rotated:
    print("Image rotated sucessfully!")
else:
    print("Dude... image wasn't rotated....")