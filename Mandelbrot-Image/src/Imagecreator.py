from PIL import Image
import math

def checkMandelbrot(x, y, iterations):
    xold = 0
    yold = 0
    for i in range(iterations):
        xnew = xold**2 - yold**2 + x
        ynew = 2*xold*yold + y
        xold, yold = xnew, ynew
        if xnew**2 + ynew**2 > 4:
            return i
    return iterations

#Linearer Farbverlauf fuer Pixel die nicht zur MbM gehoeren
def colourGradient(x, y, i, iterations,image):
    gradient = i/iterations
    potBase = int(iterations/100 * 3)
    #Wo der Farbverlauf zwischen RGB1 und RGB2 zu RGB2 und RGB3 wechseln soll
    colourswitch = 0.2
    #Innerste Farbe
    r1, g1, b1 = 255, 180, 0
    #Mittlere Farbe
    r2, g2, b2 = 255, 120, 0
    #Aeusserste Farbe
    r3, g3, b3 = 0, 0, 139
    
    if gradient > colourswitch:
        gradient = (gradient - colourswitch) / (1-colourswitch)
        gradient = math.log(gradient*potBase**2+1)/math.log(potBase**2+1)
        gradient = (math.sin(gradient * math.pi - math.pi/2)+1)/2
        r = int(r1 * (1-gradient) + r2*(gradient))
        g = int(g1 * (1-gradient) + g2*(gradient))
        b = int(b1 * (1-gradient) + b2*(gradient))
    else:
        gradient = gradient / colourswitch
        gradient = math.log(gradient*potBase**2+1)/math.log(potBase**2+1)
        gradient = (math.sin(gradient * math.pi - math.pi/2)+1)/2
        r = int(r3 * (1-gradient) + r2*(gradient))
        g = int(g3 * (1-gradient) + g2*(gradient))
        b = int(b3 * (1-gradient) + b2*(gradient))
        
    image.putpixel((x, y), (r, g, b))
    
iterations = 300
#Bildaufloesung
xwidth = 12000
ywidth = int(xwidth/3*2.5)
xincrement = 3/xwidth
yincrement = 2.5/ywidth
image = Image.new("RGB", (xwidth, ywidth), "white")

for x in range(xwidth):
    for y in range(ywidth):
        i = checkMandelbrot(x*xincrement-2, y*yincrement-1.25, iterations)
        if i == iterations:
            image.putpixel((x, y), (0, 0, 0))     
        else:
            colourGradient(x, y, i, iterations, image)
    print(str(round(x/xwidth*100, 1)) + " %")
print("DONE!!!!")
#Jeweiliger Dateipfad fuer Bild eingeben
image.save("C://Users//janho//OneDrive//Dokumente//Schule//Mathematik//Mandelbrot//highrezv2.png")