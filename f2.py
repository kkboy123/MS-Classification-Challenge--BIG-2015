Python 2.7.6 (default, Nov 10 2013, 19:24:24) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from PIL import Image
>>> im = Image.open("C:\\11.jpg")
>>> im.show()
>>> img = Image.new( 'RGB', (255,255), "black")
>>> img.show()
>>> for i in range(img.size[0]):
	for j in range(img.size[1]):
		pixels[i,j] = (i, j, 100)

		

Traceback (most recent call last):
  File "<pyshell#10>", line 3, in <module>
    pixels[i,j] = (i, j, 100)
NameError: name 'pixels' is not defined
>>> pixels = img.load()
>>> for i in range(img.size[0]):
	for j in range(img.size[1]):
		pixels[i,j] = (i, j, 100)

		
>>> img.show()
>>> im.save("C:\\12.jpg")

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    im.save("C:\\12.jpg")
  File "C:\Python27\lib\site-packages\PIL\Image.py", line 1676, in save
    fp = builtins.open(fp, "wb")
IOError: [Errno 13] Permission denied: 'C:\\12.jpg'
>>> im.save("C:\\Users\\user\D\ocuments\\12.jpg")

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    im.save("C:\\Users\\user\D\ocuments\\12.jpg")
  File "C:\Python27\lib\site-packages\PIL\Image.py", line 1676, in save
    fp = builtins.open(fp, "wb")
IOError: [Errno 2] No such file or directory: 'C:\\Users\\user\\D\\ocuments\\12.jpg'
>>> im.save("C:\\Users\\user\\Documents\\12.jpg")
>>> img.save("C:\\Users\\user\\Documents\\12.jpg")
>>> 
