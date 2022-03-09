image = cv2.imread('Your File',0) #Note that your image file should be present inside the folder where code file is present
row = image.shape[0]
column = image.shape[1]
originalSize = round((((row*column*8)/8)/1024)/1024,2) #Multiplied 8 with rows and columns because the image we are reading is in black and white form so its bpp(bits per pixel) are 8
print('Original Size of Image ',originalSize, 'Mb')

left_right_borders = int(column*0.1)
top_bottom_borders = left_right_borders+column-row

pattern = np.full((top_bottom_borders+row,left_right_borders+column,3),0,np.uint8)

newSizeofImage = round((((((row + top_bottom_borders)*(column + left_right_borders)*8)/8)/1024)/1024),2)

print('New Size of Image is ',newSizeofImage,' Mb')

top_bottom_borders = int(top_bottom_borders/2)
left_right_borders = int(left_right_borders/2)

for i in range(top_bottom_borders,top_bottom_borders+row):
    for j in range(left_right_borders,left_right_borders+column):
        pattern[i][j] = image[i-top_bottom_borders][j-left_right_borders]

cv2.imshow('Image',pattern)
cv2.waitKey(0)
cv2.destroyAllWindows()
