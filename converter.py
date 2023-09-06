#Python 3.10
from PIL import Image
import sys
import os
import math
import time

class FileIO: #class for i/o operations
    @staticmethod
    def writeBin(out_binary_filename: str, byteArr: list) -> None:
        binArr = bytearray(byteArr)
        with open(out_binary_filename,'wb') as file:
            file.write(binArr)
        return
    
    @staticmethod
    def readBin(in_binary_filename) -> list:
        arr =[]
        with open(in_binary_filename,'rb') as file:
            contentBin = file.read()
        arr = list(contentBin)
        return arr
    
    @staticmethod
    def writeBitmap(out_bitmap_filename: str, byteArr: list) -> None: # writes 1d array of bytes to bitmap
        if not out_bitmap_filename.endswith('.bmp'):
            print(f'Error: file "{out_bitmap_filename}" should end with ".bmp"')
            sys.exit(1)

        # Add zeros to the end of byteArr to make its length divisible by 3
        reminder = len(byteArr)%3
        bytesToAdd = (3-reminder)%3
        zeroArr = [0 for _ in range(bytesToAdd)]
        byteArr += zeroArr

        # turpleArr with tuples (a1, a2, a3) from byteArr 
        turpleArr = [(byteArr[i], byteArr[i + 1], byteArr[i + 2]) for i in range(0, len(byteArr), 3)]

        # Add zero tuples (0, 0, 0) to turpleArr to make its length a square
        width = math.ceil(math.sqrt(len(turpleArr)))
        height = width
        elementsToAdd = int(math.pow(width, 2))-len(turpleArr)
        zeroTurpleArr = [(0,0,0) for _ in range(elementsToAdd)]    
        turpleArr += zeroTurpleArr
        
        # Write turpleArr to a bitmap image
        img = Image.new("RGB",(width,height))
        img.putdata(turpleArr)
        img.save(out_bitmap_filename)
        
        return

    @staticmethod
    def readBitmap(filename: str) -> list: #returns 1d array of bytes from pixels (r,g,b) in bmp
        if not filename.endswith('.bmp'):
            print(f"Error: file '{filename}' should end with '.bmp'")
            sys.exit(1)
        rgb_data = []
        img = Image.open(filename)
        rgb_data = list(img.getdata())
        img.close()
        byteArr = [el for px in rgb_data for el in px]
        return byteArr


class ArrFun:
    default_field_bytes = 4

    @staticmethod
    def encodeArray(byteArr: list, length_field_bytes: int = default_field_bytes) -> list:
        firstArr = list( len(byteArr).to_bytes(length_field_bytes, byteorder='little'))
        return firstArr + byteArr
    
    @staticmethod
    def decodeArray(encodedArr: list, length_field_bytes: int = default_field_bytes):
        try:
            firstArr = encodedArr[:length_field_bytes]
            bytesToRead = int.from_bytes(firstArr, byteorder='little')
            decodedArr = encodedArr[length_field_bytes:length_field_bytes+bytesToRead]
        except:
            print(f'Error while decoding array')
            sys.exit(1)
        return decodedArr

class Main:
    max_input_filesize_MB= 100

    @staticmethod
    def checkFile(fileName):
        if not os.path.exists(fileName):
            print(f'Error: file "{fileName}" does not exist')
            sys.exit(1) 
        if os.path.getsize(fileName) > Main.max_input_filesize_MB*1024**2:
            print(f'Error: file "{fileName}" exceeds max filesize {Main.max_input_filesize_MB} MB')
            sys.exit(1)

    def encode(in_binary_filename: str, out_bitmap_filename: str) -> None:
        print(f'encoding "{in_binary_filename}"')
        Main.checkFile(in_binary_filename)
        arrContent = FileIO.readBin(in_binary_filename)
        arrEncoded = ArrFun.encodeArray(arrContent)
        FileIO.writeBitmap(out_bitmap_filename, arrEncoded)
        return
    
    def decode(in_bitmap_filename: str, out_binary_filename: str) -> None:
        print(f'decoding "{in_bitmap_filename}"')
        Main.checkFile(in_bitmap_filename)
        arrContent = FileIO.readBitmap(in_bitmap_filename)
        arrDecoded = ArrFun.decodeArray(arrContent)
        
        FileIO.writeBin(out_binary_filename, arrDecoded)
        return


if __name__=="__main__":
    start_time = time.time()
    str_en = 'en'
    str_de = 'de'
    if len(sys.argv) != 4:
        print('Error: expected 3 arguments: (user_operation, in_filename, out_filename)')
        sys.exit(1)
    user_operation = sys.argv[1]
    in_filename = sys.argv[2]
    out_filename = sys.argv[3]
    if user_operation == str_en:
        Main.encode(in_filename, out_filename)
    elif user_operation == str_de:
        Main.decode(in_filename, out_filename)
    else:
        print(f'Error: unexpected command "{user_operation}". Expected "{str_en}" or "{str_de}"')
        sys.exit(1)
    elapsed_time = round(time.time() - start_time, 1)
    print(f'completed in {elapsed_time} s')
    sys.exit(0)
  
