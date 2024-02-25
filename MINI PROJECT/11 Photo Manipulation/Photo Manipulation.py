from PIL import Image, ImageFilter, ImageEnhance
import os

print("Import the image in .jpg format to the parent directory and select the options: ")
for f in os.listdir('./'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, text = os.path.splitext(f)

        resizeinput = int(input("\n 1. Resize the image\n 2. Rotate the image\n 3. Convert the image\n 4. Blur the image\n 5. Enhance the image\n Select: "))


        if resizeinput == 1:
            print("\nEnter the x,y values for Resizing the image")
            a = int(input("Enter the x length in px: "))
            b = int(input("Enter the y length in px: "))
            size = (a, b)
            i.thumbnail(size)
            i.save('pngs/{}.png'.format(fn))
            i.save('Sized/{}_sized.png'.format(fn))

        elif resizeinput == 2:
            print("\nEnter the Valid value for Rotating the image")
            r = int(input("Enter the Rotation Angle of the Image: "))
            ro = Image.open(f)
            ro.rotate(r).save('Orientation/{}_rotated.png'.format(fn))

        elif resizeinput == 3:
            # Convert to black and white
            co = Image.open(f)
            co.convert(mode='L').save('Black and white/{}_converted.png'.format(fn))

        elif resizeinput == 4:
            # Blur the image
            blur = Image.open(f)
            blur.filter(ImageFilter.GaussianBlur(15)).save('Gaussian Blur/{}_gblur.png'.format(fn))

        elif resizeinput == 5:
            en = Image.open(f)
            enhancer = ImageEnhance.Brightness(en)
            enhancer.enhance(0.5).save('Brightness/{}_lowb.png'.format(fn))
            enhancer.enhance(1.5).save('Brightness/{}_highb.png'.format(fn))
print("Open the Respected folders")