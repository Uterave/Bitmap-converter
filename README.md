# Encoding and Decoding Utility

This is a Python utility for encoding and decoding binary files using bitmap images. You can use this tool to encode a binary file into a bitmap image or decode a bitmap image back into a binary file.

## Usage

To use this utility, follow the command-line format below:

```shell
python converter.py <user_operation> <in_filename> <out_filename>
```
- <user_operation>: Specify the operation you want to perform. Use 'en' to encode a binary file or 'de' to decode a bitmap image.
- <in_filename>: The input file to be encoded or decoded.
- <out_filename>: The output file where the result will be stored.

## Example Usage

### Encoding a Binary File

To encode a binary file, use the following command:
```
python converter.py en input.bin output.bmp
```
This command will encode the binary file 'input.bin' into a bitmap image and save it as 'output.bmp'.

### Decoding a Bitmap Image

To decode a bitmap image back into a binary file, use the following command:
```
python converter.py de input.bmp output.bin
```
This command will decode the bitmap image 'input.bmp' and save the binary content as 'output.bin'.

## Error Handling

- If the specified file does not exist, an error message will be displayed, and the program will exit.
- If the file size exceeds the maximum allowed size (100 MB), an error message will be displayed, and the program will exit.
  
The program consistently returns an exit code of 1 for any encountered errors.

## Requirements

- Python 3.10
- Pillow library (for working with bitmap images)

Install the Pillow library using the following command:
```
pip install Pillow
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.



