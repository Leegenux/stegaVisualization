from PIL import Image as img
from copy import deepcopy

def LSB_extract(filename):
    '''
    This script does a job of create a picture whose RGB channels's values 
    depend on a picture.
    '''
    origImage = img.open(filename)
    newImage  = img.new('RGB', (origImage.size[0], origImage.size[1]) )

    colors = ['red', 'green', 'blue']
    for colorInd in range(3):
        for bit in range(8, 0, -1):
            for row in range(origImage.size[1]):
                for col in range(origImage.size[0]):
                    rgb = origImage.getpixel((col, row))
                    newImage.putpixel((col, row), (255, 255, 255) if len(bin(rgb[colorInd]))-2 >= bit and bin(rgb[colorInd])[0-bit] == '1' else (0, 0, 0))
            newImage.save('result_' + colors[colorInd] + '_' + str(bit) + '.png', 'png')

def LSB_encode(payloadPath):
    from math import floor

    f = open(payloadPath)
    
    payloadContent = f.read()
    payloadBinary = ''.join(format(ord(x), 'b') for x in payloadContent)

    origImage = img.open('./Lenna_orig.png').convert('RGB')
    newImage  = deepcopy(origImage)

    row = 0
    col = 0
    for bit in payloadBinary:
        rgb = origImage.getpixel((col, row))
        newImage.putpixel((col, row), (2*floor(rgb[0]/2)+int(bit), rgb[1], rgb[2]))

        row += 1
        if row >= newImage.size[1]:
            row = 0
            col += 1
        if col >= newImage.size[0]:
            break

        # DEBUG 
        print(row, col, origImage.size[1], origImage.size[0])

    print('saving')
    newImage.save('./payload-filled.png', 'png')

LSB_encode('./payload.txt')
LSB_extract('./payload-filled.png')
