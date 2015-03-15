from PIL import Image

#path="C:\\Users\\user\\Downloads\\dataSample\\"
#filename="0A32eTdBKayjCWhZqDOQ.bytes"

def convert_memory2image(path,filename):
    f = open(path+filename,"r")
    lines = f.readlines()
    #height and width of the image
    h=len(lines)
    w=16
    #new a image
    img = Image.new( 'RGBA', (w,h), "black")
    pixels = img.load()
    #dump all memory value into image(gray sccale)
    for i in range(h):
        j=0
        for p in lines[i].replace("\n","").split(" ")[1:]:
            if p!="??":
                my_pixel,alpha = int(p,16),255
            else:
                my_pixel,alpha = 0,0
            pixels[j,i] = (my_pixel, my_pixel, my_pixel,alpha)
            j=j+1
    #save the image as png file so that alpha value will show        
    img.save(path+filename+".png")

path="C:\\Users\\user\\Downloads\\dataSample\\"
filename="0ACDbR5M3ZhBJajygTuf.bytes"    
convert_memory2image(path,filename)    