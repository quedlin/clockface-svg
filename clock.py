import cairo
from math import pi, sin, cos

# Thanks Andrew Walker!
# https://stackoverflow.com/questions/8463271/rotate-text-around-its-center-in-pycairo
def text(context, string, pos, theta = 0.0, face = 'Georgia', font_size = 18):

    context.save()
    context.select_font_face("Georgia", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    context.set_font_size(font_size)

    fascent, fdescent, fheight, fxadvance, fyadvance = context.font_extents()
    x_off, y_off, tw, th = context.text_extents(string)[:4]
    nx = -tw/2.0
    ny = fheight/2
    
    context.translate(pos[0],pos[1])
    context.rotate(theta)
    context.translate(nx,ny)

    context.scale(0.8,1.0);

    context.move_to(0,0)        
    context.show_text(string)
    context.restore()


with cairo.SVGSurface("clockface.svg", 200, 200) as surface:
    context = cairo.Context(surface)
    x, y, x1, y1 = 0.0, 0.5, 0.5, 1.0
    x2, y2, x3, y3 = 0.6, 0.1, 0.9, 0.5
    context.scale(200, 200)

    context.set_source_rgba(1, 1, 1)
    #context.set_line_width(0.2)
    context.arc(0.5, 0.5, 0.5, 0, 2 * pi)
    context.fill()
    
    def circle(radius=0.3,thickness=0.01):
        context.set_source_rgba(0, 0, 0)
        context.set_line_width(thickness)
        context.arc(0.5, 0.5, radius, 0, 2 * pi)
        context.stroke()

    def rovatka(r1=0.3,r2=0.35,d=12,thickness=0.01):
        context.set_source_rgba(0, 0, 0)
        context.set_line_width(thickness)

        for i in range(0,d):
            phi=pi*2/d * i
            x1=0.5 + (cos(phi) * r1)
            y1=0.5 + (sin(phi) * r1)
            x2=0.5 + (cos(phi) * r2)
            y2=0.5 + (sin(phi) * r2)
            context.move_to(x1, y1)
            context.line_to(x2, y2)
            context.stroke()    

    circle(radius=0.48,thickness=0.02)

    r_outer=0.45
    r_inner=0.42
    circle(radius=r_outer,thickness=0.01)
    circle(radius=r_inner,thickness=0.01)
    
    rovatka(r1=r_inner,r2=r_outer,d=12,thickness=0.02)
    rovatka(r1=r_inner,r2=r_outer,d=12*5,thickness=0.01)

    numerals = ['I', 'II', 'III', 'IIII', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
    d=12
    r=0.38
    for i in range(0,d):
        phi=pi*2/d * i
        phi = phi - (pi/6*2)
        x1=0.5 + (cos(phi) * r)
        y1=0.5 + (sin(phi) * r)
        text(context, numerals[i], (x1, y1), phi+(pi/2), font_size=0.1)
        
        
    


