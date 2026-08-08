from PIL import Image
file = "" #Paste your image file path right here, INSIDE the quote

if file:
    pdf = file.rsplit('.', 1)[0] + '.pdf'
    Image.open(file).convert('RGB').save(pdf)
    print(f"Successfully saved as: {pdf}")
# pip install Pillow (required dependency)
