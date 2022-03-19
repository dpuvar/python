from PIL import Image

# Path for your image where it is
image_1 = Image.open(r"C:\\Users\\dhruv\\OneDrive\\Desktop\\pip\\result.jpg")

# Converting it into pdf
img_1 = image_1.convert('RGB')

# Path where your PDF file will bw saved
img_1.save(r'C:\\Users\\dhruv\\OneDrive\\Desktop\\pip\\result3.pdf')


