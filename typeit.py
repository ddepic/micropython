import ssd1306ada
from machine import Pin, I2C
import font as fnt

i2c1 = I2C(1, scl=Pin(7), sda=Pin(6), freq=100000)

ssd = ssd1306ada.SSD1306_I2C(128, 64, i2c1)

    
    
def dc (z,zz):
    c= 0
    r = zz*16
    for q in str(z):
        z1=ord(q) 
         
        for d in range(5):
            b = fnt.toBinary(fnt.ASCII[z1-32][d])
            br =''.join(reversed(b))
            for i in br:
                if i == '1':
                    ssd.pixel(c, r, 1)
                    ssd.pixel(c, r+1, 1)
                    ssd.pixel(c+1, r, 1)
                    ssd.pixel(c+1, r+1, 1)
                r +=2
                if r > (15+zz*16):
                    r=0+zz*16
                    c +=2

