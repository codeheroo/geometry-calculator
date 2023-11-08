# Подключение библеотеки
from math import *
import tkinter as tk
from sympy import *
from tkinter import ttk


# Создание функций кнопок
def SegmentMiddle():



    def draw_vector():
        try:
            x1 = int(entry_x1.get())
            y1 = int(entry_y1.get())
            x2 = int(entry_x2.get())
            y2 = int(entry_y2.get())
        except ValueError:
            return
        koeff = 200 / max([x1, y1, x2, y2])
        dx1 = x1*koeff
        dy1 = y1*koeff
        dx2 = x2*koeff
        dy2 = y2*koeff
        canvas.delete("all")
        
        canvas.create_line(0, HEIGHT/2, WIDTH, HEIGHT/2, arrow=tk.LAST)
        canvas.create_text(WIDTH-10, HEIGHT/2-10, text="x")
        canvas.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, arrow=tk.FIRST)
        canvas.create_text(WIDTH/2+10, 10, text="y")
        
        x = x2 - x1
        y = y2 - y1

        
        canvas.create_line(WIDTH/2+dx1, HEIGHT/2-dy1, WIDTH/2+dx2, HEIGHT/2-dy2, arrow=tk.LAST)
        canvas.create_text(WIDTH/2+dx1, HEIGHT/2-dy1-10, text=f"({x1}, {y1})")
        canvas.create_text(WIDTH/2+dx2, HEIGHT/2-dy2-10, text=f"({x2}, {y2})")
        canvas.create_text(WIDTH/2+x1+x/2, HEIGHT/2-y1-y/2-10, text=f"({x1+x/2}, {y1+y/2})")
        

    WIDTH = 700
    HEIGHT = 700

    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.grid()

    text_x1 = tk.Label(frame, text='x1=')
    text_x1.grid(column=0, row=0)

    entry_x1 = tk.Entry(frame)
    entry_x1.grid(column=1, row=0)

    text_y1 = tk.Label(frame, text='y1=')
    text_y1.grid(column=0, row=1)

    entry_y1 = tk.Entry(frame)
    entry_y1.grid(column=1, row=1)

    text_x2 = tk.Label(frame, text='x2=')
    text_x2.grid(column=0, row=2)

    entry_x2 = tk.Entry(frame)
    entry_x2.grid(column=1, row=2)

    text_y2 = tk.Label(frame, text='y2=')
    text_y2.grid(column=0, row=3)
    entry_y2 = tk.Entry(frame)
    entry_y2.grid(column=1, row=3)

    button = tk.Button(frame, text="Draw segment", command=draw_vector)
    button.grid(column=0, row=4)

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
    canvas.grid(column=0, row=5)

    root.mainloop()



def VektorModul():

    def draw_vector():
        try:
            x = int(entry_x.get())
            y = int(entry_y.get())
            xroot = int(entry_xroot.get())
            yroot = int(entry_yroot.get())
        except ValueError:
            return
        koeff = 200 / max([x, y])
        dx = x*koeff
        dy = y*koeff

        canvas.delete("all")
        
        canvas.create_line(0, HEIGHT/2, WIDTH, HEIGHT/2, arrow=tk.LAST)
        canvas.create_text(WIDTH-10, HEIGHT/2-10, text="x")
        canvas.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, arrow=tk.FIRST)
        canvas.create_text(WIDTH/2+10, 10, text="y")
        
        length=sqrt((x*sqrt(xroot)**2+(y*sqrt(yroot)**2)))

        
        canvas.create_line(WIDTH/2, HEIGHT/2, WIDTH/2+dx, HEIGHT/2-dy, arrow=tk.LAST)

        canvas.create_text(WIDTH/2+dx/2, HEIGHT/2-dy/2-10, text=simplify(length))
      

    WIDTH = 700
    HEIGHT = 700

    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.grid()

    text_x = tk.Label(frame, text='x=')
    text_x.grid(column=0, row=0)

    entry_x = tk.Entry(frame)
    entry_x.grid(column=1, row=0)

    text_y = tk.Label(frame, text='y=')
    text_y.grid(column=0, row=1)

    entry_y = tk.Entry(frame)
    entry_y.grid(column=1, row=1)

    text_xroot = tk.Label(frame, text='√')
    text_xroot.grid(column=2, row=0)

    entry_xroot = tk.Entry(frame)
    entry_xroot.grid(column=3, row=0)

    text_yroot = tk.Label(frame, text='√')
    text_yroot.grid(column=2, row=1)
    entry_yroot = tk.Entry(frame)
    entry_yroot.grid(column=3, row=1)

    button = tk.Button(frame, text="Draw vector", command=draw_vector)
    button.grid()

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
    canvas.grid()

    root.mainloop()  
    
    

def DotDistance():


    def draw_vector():
        try:
            x1 = int(entry_x1.get())
            y1 = int(entry_y1.get())
            x2 = int(entry_x2.get())
            y2 = int(entry_y2.get())
            x1root = int(entry_x1root.get())
            y1root = int(entry_y1root.get())
            x2root = int(entry_x2root.get())
            y2root = int(entry_y2root.get())
        except ValueError:
            return
        koeff = 200 / max([x1, y1, x2, y2])
        dx1 = x1*koeff
        dy1 = y1*koeff
        dx2 = x2*koeff
        dy2 = y2*koeff
        canvas.delete("all")
        
        canvas.create_line(0, HEIGHT/2, WIDTH, HEIGHT/2, arrow=tk.LAST)
        canvas.create_text(WIDTH-10, HEIGHT/2-10, text="x")
        canvas.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, arrow=tk.FIRST)
        canvas.create_text(WIDTH/2+10, 10, text="y")
        
        x = x2 - x1
        y = y2 - y1
        distance=sqrt(((x2*sqrt(x2root)-x1*sqrt(x1root))**2+y2*sqrt(y2root)-y1*sqrt(y1root))**2)
        
        canvas.create_line(WIDTH/2+dx1, HEIGHT/2-dy1, WIDTH/2+dx2, HEIGHT/2-dy2)
        canvas.create_text(WIDTH/2+dx1, HEIGHT/2-dy1-10, text=f"({x1}√{x1root}, {y1}√{y1root})")
        canvas.create_text(WIDTH/2+dx2, HEIGHT/2-dy2-10, text=f"({x2}√{x2root}, {y2}√{y2root})")

        texttt = tk.Label(frame, text=f"{simplify(distance)}")
        texttt.grid()
        

    WIDTH = 700
    HEIGHT = 700

    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.grid()

    text_x1 = tk.Label(frame, text='x1=')
    text_x1.grid(column=0, row=0)


    entry_x1 = tk.Entry(frame)
    entry_x1.grid(column=1, row=0)

    text_x1root = tk.Label(frame, text='√')
    text_x1root.grid(column=2, row=0)

    entry_x1root = tk.Entry(frame)
    entry_x1root.grid(column=3, row=0)

    text_y1 = tk.Label(frame, text='y1=')
    text_y1.grid(column=0, row=1)


    entry_y1 = tk.Entry(frame)
    entry_y1.grid(column=1, row=1)

    text_y1root = tk.Label(frame, text='√')
    text_y1root.grid(column=2, row=1)

    entry_y1root = tk.Entry(frame)
    entry_y1root.grid(column=3, row=1)

    text_x2 = tk.Label(frame, text='x2=')
    text_x2.grid(column=0, row=2)

    entry_x2 = tk.Entry(frame)
    entry_x2.grid(column=1, row=2)

    text_x2root = tk.Label(frame, text='√')
    text_x2root.grid(column=2, row=2)

    entry_x2root = tk.Entry(frame)
    entry_x2root.grid(column=3, row=2)

    text_y2 = tk.Label(frame, text='y2=')
    text_y2.grid(column=0, row=3)

    entry_y2 = tk.Entry(frame)
    entry_y2.grid(column=1, row=3)

    text_y2root = tk.Label(frame, text='√')
    text_y2root.grid(column=2, row=3)

    entry_y2root = tk.Entry(frame)
    entry_y2root.grid(column=3, row=3)

    button = tk.Button(frame, text="draw segment", command=draw_vector)
    button.grid()

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
    canvas.grid()

    root.mainloop()


def VectorMultiplication():
    def getmultiply():


        cosinus=[0,[1,1],30,[3,2],45,[2,2],60,[1,2],90,[0,1],120,[-1,2],135,[-2,2],150,[-3,2]]

        try:
            a = int(entry_a.get())
            aroot = int(entry_aroot.get())

            b = int(entry_b.get())
            broot = int(entry_broot.get())

            alph=int(entry_alph.get())
        except ValueError:
            return

        if alph in cosinus: alphacos=sqrt(cosinus[cosinus.index(alph)+1][0])/cosinus[cosinus.index(alph)+1][1]
        else: alphacos=round(cos(radians(alph)),4)


        multiplication=simplify(a*b*sqrt(aroot*broot)*alphacos)
        label.config(text=f"{multiplication}")

    WIDTH = 700
    HEIGHT = 700

    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.grid()

    text_a = tk.Label(frame, text='a=')
    text_a.grid(column=0, row=0)

    entry_a = tk.Entry(frame)
    entry_a.grid(column=1, row=0)

    text_aroot = tk.Label(frame, text='√')
    text_aroot.grid(column=2, row=0)

    entry_aroot = tk.Entry(frame)
    entry_aroot.grid(column=3, row=0)

    text_b = tk.Label(frame, text='b=')
    text_b.grid(column=0, row=1)

    entry_b = tk.Entry(frame)
    entry_b.grid(column=1, row=1)

    text_broot = tk.Label(frame, text='√')
    text_broot.grid(column=2, row=1)

    entry_broot = tk.Entry(frame)
    entry_broot.grid(column=3, row=1)

    text_alph = tk.Label(frame, text='α=')
    text_alph.grid(column=0, row=2)

    entry_alph = tk.Entry(frame)
    entry_alph.grid(column=1, row=2)

    button = tk.Button(frame, text="рассчитать", command=getmultiply)
    button.grid()

    label = tk.Label(root, text="")
    label.grid()

    root.mainloop()



def StraightsEquation():


    
    
    def draw_vector():
        try:
            x1 = int(entry_x1.get())
            y1 = int(entry_y1.get())
            x2 = int(entry_x2.get())
            y2 = int(entry_y2.get())
            x1root = int(entry_x1root.get())
            y1root = int(entry_y1root.get())
            x2root = int(entry_x2root.get())
            y2root = int(entry_y2root.get())
        except ValueError:
            return
        x,y=symbols("x,y")
        equation=(y2*sqrt(y2root)-y1*sqrt(y1root))*x-(x2*sqrt(x2root)-x1*sqrt(x1root))*y+(x2*sqrt(x2root)*y1*sqrt(y1root)-x1*sqrt(x2root)*y2*sqrt(y2root))
        label.config(text=f"{simplify(equation)} = 0")

    WIDTH = 700
    HEIGHT = 700

    root = tk.Tk()
    root.title('Уравнение прямой')
    root.geometry(f"{WIDTH}x{HEIGHT}")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.grid()

    x1label = tk.Label(frame, text='x1=')
    x1label.grid(column=0, row=0)

    entry_x1 = tk.Entry(frame)
    entry_x1.grid(column=1, row=0)

    x1rootlabel = tk.Label(frame, text='√')
    x1rootlabel.grid(column=2, row=0)

    entry_x1root = tk.Entry(frame)
    entry_x1root.grid(column=3, row=0)

    y1label = tk.Label(frame, text='y1=')
    y1label.grid(column=0, row=1)

    entry_y1 = tk.Entry(frame)
    entry_y1.grid(column=1, row=1)
    
    y1rootlabel = tk.Label(frame, text='√')
    y1rootlabel.grid(column=2, row=1)

    entry_y1root = tk.Entry(frame)
    entry_y1root.grid(column=3, row=1)

    x2label = tk.Label(frame, text='x2=')
    x2label.grid(column=0, row=2)

    entry_x2 = tk.Entry(frame)
    entry_x2.grid(column=1, row=2)

    x2rootlabel = tk.Label(frame, text='√')
    x2rootlabel.grid(column=2, row=2)

    entry_x2root = tk.Entry(frame)
    entry_x2root.grid(column=3, row=2)

    y2label = tk.Label(frame, text='y2=')
    y2label.grid(column=0, row=3)

    entry_y2 = tk.Entry(frame)
    entry_y2.grid(column=1, row=3)

    y2rootlabel = tk.Label(frame, text='√')
    y2rootlabel.grid(column=2, row=3)

    entry_y2root = tk.Entry(frame)
    entry_y2root.grid(column=3, row=3)

    button = tk.Button(frame, text="Рассчитать", command=draw_vector)
    button.grid()

    label = tk.Label(root, text="")
    label.grid()

    root.mainloop()


def CircleEquation():

    


    def draw_vector():
        try:
            x0 = int(entry_x0.get())
            y0 = int(entry_y0.get())
            x0root = int(entry_x0root.get())
            y0root = int(entry_y0root.get())
            r = int(entry_r.get())
            rroot = int(entry_rroot.get())
        except ValueError:
            return
        x,y=symbols("x,y")
        equation=(x-x0*sqrt(x0root))**2+(y-y0*sqrt(y0root))**2
        label.config(text=f"{simplify(equation)} = {r**2*rroot}")

    WIDTH = 700
    HEIGHT = 700

    root = tk.Tk()
    root.title('Уравнение окружности')
    root.geometry(f"{WIDTH}x{HEIGHT}")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.grid()

    x0label = tk.Label(frame, text='x0=')
    x0label.grid(column=0, row=0)

    entry_x0 = tk.Entry(frame)
    entry_x0.grid(column=1, row=0)

    x0rootlabel = tk.Label(frame, text='√')
    x0rootlabel.grid(column=2, row=0)

    entry_x0root = tk.Entry(frame)
    entry_x0root.grid(column=3, row=0)

    y0label = tk.Label(frame, text='y0=')
    y0label.grid(column=0, row=1)

    entry_y0 = tk.Entry(frame)
    entry_y0.grid(column=1, row=1)

    y0root = tk.Label(frame, text='√')
    y0root.grid(column=2, row=1)

    entry_y0root = tk.Entry(frame)
    entry_y0root.grid(column=3, row=1)

    rlabel = tk.Label(frame, text='r=')
    rlabel.grid(column=0, row=2)

    entry_r = tk.Entry(frame)
    entry_r.grid(column=1, row=2)

    rrootlabel = tk.Label(frame, text='√')
    rrootlabel.grid(column=2, row=2)

    entry_rroot = tk.Entry(frame)
    entry_rroot.grid(column=3, row=2)

    button = tk.Button(frame, text="Рассчитать", command=draw_vector)
    button.grid()

    label = tk.Label(root, text="")
    label.grid()

    root.mainloop()


def VectorCoordinates():



    


    def draw_vector():
        try:
            x1 = int(entry_x1.get())
            y1 = int(entry_y1.get())
            x2 = int(entry_x2.get())
            y2 = int(entry_y2.get())
            x1root = int(entry_x1root.get())
            y1root = int(entry_y1root.get())
            x2root = int(entry_x2root.get())
            y2root = int(entry_y2root.get())
        except ValueError:
            return
        koeff = 200 / max([x1, y1, x2, y2])
        dx1 = x1*koeff
        dy1 = y1*koeff
        dx2 = x2*koeff
        dy2 = y2*koeff
        canvas.delete("all")
        
        canvas.create_line(0, HEIGHT/2, WIDTH, HEIGHT/2, arrow=tk.LAST)
        canvas.create_text(WIDTH-10, HEIGHT/2-10, text="x")
        canvas.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, arrow=tk.FIRST)
        canvas.create_text(WIDTH/2+10, 10, text="y")
        
        x=x2*sqrt(x2root)-x1*sqrt(x1root)
        y=y2*sqrt(y2root)-y1*sqrt(y1root)
        distance=sqrt(((x2*sqrt(x2root)-x1*sqrt(x1root))**2+y2*sqrt(y2root)-y1*sqrt(y1root))**2)
        
        canvas.create_line(WIDTH/2+dx1, HEIGHT/2-dy1, WIDTH/2+dx2, HEIGHT/2-dy2, arrow=tk.LAST)
        canvas.create_text(WIDTH/2+dx1, HEIGHT/2-dy1-10, text=f"({x1}√{x1root}, {y1}√{y1root})")
        canvas.create_text(WIDTH/2+dx2, HEIGHT/2-dy2-10, text=f"({x2}√{x2root}, {y2}√{y2root})")
        canvas.create_text(WIDTH/2+x1, HEIGHT/2-y1-10, text=f"{simplify(x)};{simplify(y)}")
        

    WIDTH = 700
    HEIGHT = 700

    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.grid()

    x1label = tk.Label(frame, text='x1=')
    x1label.grid(column=0, row=0)

    entry_x1 = tk.Entry(frame)
    entry_x1.grid(column=1, row=0)

    x1rootlabel = tk.Label(frame, text='√')
    x1rootlabel.grid(column=2, row=0)

    entry_x1root = tk.Entry(frame)
    entry_x1root.grid(column=3, row=0)

    y1label = tk.Label(frame, text='y1=')
    y1label.grid(column=0, row=1)

    entry_y1 = tk.Entry(frame)
    entry_y1.grid(column=1, row=1)
    
    y1rootlabel = tk.Label(frame, text='√')
    y1rootlabel.grid(column=2, row=1)

    entry_y1root = tk.Entry(frame)
    entry_y1root.grid(column=3, row=1)

    x2label = tk.Label(frame, text='x2=')
    x2label.grid(column=0, row=2)

    entry_x2 = tk.Entry(frame)
    entry_x2.grid(column=1, row=2)

    x2rootlabel = tk.Label(frame, text='√')
    x2rootlabel.grid(column=2, row=2)

    entry_x2root = tk.Entry(frame)
    entry_x2root.grid(column=3, row=2)

    y2label = tk.Label(frame, text='y2=')
    y2label.grid(column=0, row=3)

    entry_y2 = tk.Entry(frame)
    entry_y2.grid(column=1, row=3)

    y2rootlabel = tk.Label(frame, text='√')
    y2rootlabel.grid(column=2, row=3)

    entry_y2root = tk.Entry(frame)
    entry_y2root.grid(column=3, row=3)

    button = tk.Button(frame, text="Draw vector", command=draw_vector)
    button.grid()

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
    canvas.grid()

    root.mainloop()


def TwoSidesOneAngle():
    def printall(c, alpha, beta, S, R, r, halpha, hbeta, hgamma, malpha, mbeta, mgamma, lalpha, lbeta, lgamma):
        c_label = tk.Label(root, text=c)
        c_label.grid()

        alpha_label = tk.Label(root, text=alpha)
        alpha_label.grid()

        beta_label = tk.Label(root, text=beta)
        beta_label.grid()
        
        S_label = tk.Label(root, text=S)
        S_label.grid()

        R_label = tk.Label(root, text=R)
        R_label.grid()

        r_label = tk.Label(root, text=r)
        r_label.grid()

        halpha_label = tk.Label(root, text=halpha)
        halpha_label.grid()

        hbeta_label = tk.Label(root, text=hbeta)
        hbeta_label.grid()

        hgamma_label = tk.Label(root, text=hgamma)
        hgamma_label.grid()



    def draw_vector():
        try:
            a = int(entry_a.get())
            b = int(entry_b.get())
            aroot = int(entry_aroot.get())
            broot = int(entry_broot.get())
            gam = int(entry_gam.get())

        except ValueError:
            return

        cosinus=[0,[1,1],30,[3,2],45,[2,2],60,[1,2],90,[0,1],120,[-1,2],135,[-2,2],150,[-3,2]]
        sinus=[0,[0,1],30,[1,2],45,[2,2],60,[3,2],90,[1,1],120,[3,2],135,[2,2],150,[1,2]]

        if gam in cosinus: # Находим с
            gammacos=sqrt(cosinus[cosinus.index(gam)+1][0])/cosinus[cosinus.index(gam)+1][1]
            c=simplify(sqrt(a**2*aroot+b**2*broot-2*a*b*sqrt(aroot*broot)*gammacos))
            print(f"c={c}")

        else: 
            gammacos=round(cos(radians(gam)),4)
            c=simplify(a**2*aroot+b**2*broot-2*a*b*sqrt(aroot*broot)*gammacos)
            print(f"c=sqrt({c})")
            c=sqrt(c)
        alphacos=((b*sqrt(broot))**2+c**2-(a*sqrt(aroot))**2)/(2*b*broot*c) # Находим альфа
        alph=round(degrees(acos(simplify(alphacos))),1)



        bet=180-alph-gam # Находим бета
        bet=round(bet,1)



        if gam in sinus: gammasin=sqrt(sinus[sinus.index(gam)+1][0])/sinus[sinus.index(gam)+1][1]
        else: gammasin=round(sin(radians(gam)),3)

        if bet in sinus: betasin=sqrt(sinus[sinus.index(bet)+1][0])/sinus[sinus.index(bet)+1][1]
        else: betasin=round(sin(radians(bet)),3)

        if alph in sinus: alphasin=sqrt(sinus[sinus.index(alph)+1][0])/sinus[sinus.index(alph)+1][1]
        else: alphasin=round(sin(radians(alph)),3)

        area=simplify(a*b*sqrt(aroot*broot)*gammasin/2) # Находим площадь



        BigRadius=simplify(c/gammasin/2) # Находим радиус описанной около треугольника окружности



        SmallRadius=simplify(2*area/(a*aroot+b*broot+c))



        halpha=simplify(b*broot*gammasin)

        hbeta=simplify(a*aroot*gammasin)

        hgamma=simplify(b*broot*alphasin)

        malpha=simplify(sqrt(2*b**2*broot+2*c**2-a**2*aroot)/2)

        mbeta=simplify(sqrt(2*a**2*aroot+2*c**2-b**2*broot)/2)

        mgamma=simplify(sqrt(2*a**2*aroot+2*b**2*broot-c**2)/2)

        lalpha=simplify(sqrt(b*sqrt(broot)*c*(a*sqrt(aroot)+b*sqrt(broot)+c)*(b*sqrt(broot)+c-a*sqrt(aroot)))/(b*sqrt(broot)+c))

        lbeta=simplify(sqrt(a*sqrt(aroot)*c*(a*sqrt(aroot)+b*sqrt(broot)+c)*(a*sqrt(aroot)+c-b*sqrt(broot)))/(a*sqrt(aroot)+c))

        lgamma=simplify(sqrt(a*b*sqrt(aroot*broot)*(a*sqrt(aroot)+b*sqrt(broot)+c)*(a*sqrt(aroot)+b*sqrt(broot)-c))/(a*sqrt(aroot)+b*sqrt(broot)))

        printall(f"c={c}", f"α={float(alph):g}°", f"β={float(bet):g}°", f"S={area}", f"R={BigRadius}", f"r={SmallRadius}", f"h(a)={halpha}",f"h(b)={hbeta}",f"h(c)={hgamma}",f"m(a)={malpha}",f"m(b)={mbeta}",f"m(c)={mgamma}",f"l(a)={lalpha}",f"l(b)={lbeta}",f"l(c)={lgamma}")



    WIDTH = 700
    HEIGHT = 700

    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.title('По 2 сторонам и углу между ними')
    frame = tk.Frame(root, padx=20, pady=20)
    frame.grid()

    alabel = tk.Label(frame, text='a=')
    alabel.grid(column=0, row=0)

    entry_a = tk.Entry(frame)
    entry_a.grid(column=1, row=0)

    arootlabel = tk.Label(frame, text='√')
    arootlabel.grid(column=2, row=0)

    entry_aroot = tk.Entry(frame)
    entry_aroot.grid(column=3, row=0)

    blabel = tk.Label(frame, text='b=')
    blabel.grid(column=0, row=1)

    entry_b = tk.Entry(frame)
    entry_b.grid(column=1, row=1)

    brootlabel = tk.Label(frame, text='√')
    brootlabel.grid(column=2, row=1)

    entry_broot = tk.Entry(frame)
    entry_broot.grid(column=3, row=1)

    gamlabel = tk.Label(frame, text='γ=')
    gamlabel.grid(column=0, row=2)

    entry_gam = tk.Entry(frame)
    entry_gam.grid(column=1, row=2)

    button = tk.Button(frame, text="Рассчитать", command=draw_vector)
    button.grid()



    root.mainloop()




def OneSideTwoAngles():
    print("Если отсутствует корень, то напишите на его месте 1")
    print("Введите все известные элементы треугольника")
    print("b - сторона треугольника, а γ и α - углы, прилежащие к этой стороне")

    sinus=[0,[0,1],30,[1,2],45,[2,2],60,[3,2],90,[1,1],120,[3,2],135,[2,2],150,[1,2]]

    def printall(array):
        for element in array:
            tk.Label(frame, text=element).grid()

    def draw_vector():
        try:

            b = int(entry_b.get())
            
            broot = int(entry_broot.get())
            gam = int(entry_gam.get())
            alph = int(entry_alph.get())

        except ValueError:
            return
        sinus=[0,[0,1],30,[1,2],45,[2,2],60,[3,2],90,[1,1],120,[3,2],135,[2,2],150,[1,2]]

        bet=180-gam-alph # Находим бета
        print(f"β={bet}")


        if gam in sinus: gammasin=sqrt(sinus[sinus.index(gam)+1][0])/sinus[sinus.index(gam)+1][1]
        else: gammasin=round(sin(radians(gam)),3)

        if bet in sinus: betasin=sqrt(sinus[sinus.index(bet)+1][0])/sinus[sinus.index(bet)+1][1]
        else: betasin=round(sin(radians(bet)),3)

        if alph in sinus: alphasin=sqrt(sinus[sinus.index(alph)+1][0])/sinus[sinus.index(alph)+1][1]
        else: alphasin=round(sin(radians(alph)),3)


        a=simplify(b*sqrt(broot)*alphasin/betasin) # Находим a



        c=simplify(b*sqrt(broot)*gammasin/betasin) # Находим с



        area=simplify(a*b*sqrt(broot)*gammasin/2) # Находим площадь



        BigRadius=simplify(c/gammasin/2) # Находим радиус описанной около треугольника окружности



        SmallRadius=simplify(2*area/(a+b*sqrt(broot)+c))


        halpha=simplify(b*sqrt(broot)*gammasin)

        hbeta=simplify(a*gammasin)

        hgamma=simplify(b*sqrt(broot)*alphasin)




        malpha=simplify(sqrt(2*b**2*broot+2*c**2-a**2)/2)

        mbeta=simplify(sqrt(2*a**2+2*c**2-b**2*broot)/2)

        mgamma=simplify(sqrt(2*a**2+2*b**2*broot-c**2)/2)




        lalpha=simplify(sqrt(b*sqrt(broot)*c*(a+b*sqrt(broot)+c)*(b*sqrt(broot)+c-a))/(b*sqrt(broot)+c))

        lbeta=simplify(sqrt(a*c*(a+b*sqrt(broot)+c)*(a+c-b*sqrt(broot)))/(a+c))

        lgamma=simplify(sqrt(a*b*sqrt(broot)*(a+b*sqrt(broot)+c)*(a+b*sqrt(broot)-c))/(a+b*sqrt(broot)))

        printall([f"β={float(bet):g}°", f"S={area}", f"R={BigRadius}", f"r={SmallRadius}", f"h(a)={halpha}",f"h(b)={hbeta}",f"h(c)={hgamma}"])
        
    



    WIDTH = 700
    HEIGHT = 700

    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.title('По стороне и 2 прилежащим углам')
    frame = tk.Frame(root, padx=20, pady=20)
    frame.grid()

    blabel = tk.Label(frame, text='b=')
    blabel.grid(column=0, row=0)

    entry_b = tk.Entry(frame)
    entry_b.grid(column=1, row=0)

    brootlabel = tk.Label(frame, text='√')
    brootlabel.grid(column=2, row=0)

    entry_broot = tk.Entry(frame)
    entry_broot.grid(column=3, row=0)

    gamlabel = tk.Label(frame, text='γ=')
    gamlabel.grid(column=0, row=1)

    entry_gam = tk.Entry(frame)
    entry_gam.grid(column=1, row=1)

    alphlabel = tk.Label(frame, text='α=')
    alphlabel.grid(column=0, row=2)

    entry_alph = tk.Entry(frame)
    entry_alph.grid(column=1, row=2)

    button = tk.Button(frame, text="Рассчитать", command=draw_vector)
    button.grid()



    root.mainloop()


def ThreeSides():
    print("Если отсутствует корень, то напишите на его месте 1")
    print("Введите все известные элементы треугольника")
    print("a, b и c - стороны треугольника")
    def printall(array):
        for element in array:
            UWU = tk.Label(root, text = element)
            UWU.grid()
    def draw_vector():
        try:
            a = int(entry_a.get())
            aroot = int(entry_aroot.get())
            b = int(entry_b.get())
            broot = int(entry_broot.get())
            c = int(entry_c.get())
            croot = int(entry_croot.get())

        except ValueError:
            return
        alphacos=simplify((b**2*broot+c**2*croot-a**2*aroot)/(2*b*sqrt(broot)*c*sqrt(croot))) # Находим альфа
        alph=round(degrees(acos(simplify(alphacos))),2)



        betacos=simplify((a**2*aroot+c**2*croot-b**2*broot)/(2*a*sqrt(aroot)*c*sqrt(croot))) # Находим бета
        bet=round(degrees(acos(simplify(betacos))),2)



        gam=180-alph-bet # Находим гамма



        if gam in sinus: gammasin=sqrt(sinus[sinus.index(gam)+1][0])/sinus[sinus.index(gam)+1][1]
        else: gammasin=round(sin(radians(gam)),3)
    
        if bet in sinus: betasin=sqrt(sinus[sinus.index(bet)+1][0])/sinus[sinus.index(bet)+1][1]
        else: betasin=round(sin(radians(bet)),3)
    
        if alph in sinus: alphasin=sqrt(sinus[sinus.index(alph)+1][0])/sinus[sinus.index(alph)+1][1]
        else: alphasin=round(sin(radians(alph)),3)


        area=simplify(a*b*sqrt(aroot*broot)*gammasin/2) # Находим площадь


        BigRadius=simplify(c*sqrt(croot)/gammasin/2) # Находим радиус описанной около треугольника окружности



        SmallRadius=simplify(2*area/(a*sqrt(aroot)+b*sqrt(broot)+c*sqrt(croot)))



        
        
        halpha=simplify(b*sqrt(broot)*gammasin)

        hbeta=simplify(a*sqrt(aroot)*gammasin)

        hgamma=simplify(b*sqrt(broot)*alphasin)




        malpha=simplify(sqrt(2*b**2*broot+2*c**2*croot-a**2*aroot)/2)

        mbeta=simplify(sqrt(2*a**2*aroot+2*c**2*croot-b**2*broot)/2)

        mgamma=simplify(sqrt(2*a**2*aroot+2*b**2*broot-c**2*croot)/2)




        lalpha=simplify(sqrt(b*c*sqrt(broot*croot)*(a*sqrt(aroot)+b*sqrt(broot)+c*sqrt(croot))*(b*sqrt(broot)+c*sqrt(croot)-a*sqrt(aroot)))/(b*sqrt(broot)+c*sqrt(croot)))

        lbeta=simplify(sqrt(a*sqrt(aroot*croot)*c*(a*sqrt(aroot)+b*sqrt(broot)+c*sqrt(croot))*(a*sqrt(aroot)+c*sqrt(croot)-b*sqrt(broot)))/(a*sqrt(aroot)+c*sqrt(croot)))

        lgamma=simplify(sqrt(a*b*sqrt(aroot*broot)*(a*sqrt(aroot)+b*sqrt(broot)+c*sqrt(croot))*(a*sqrt(aroot)+b*sqrt(broot)-c*sqrt(croot)))/(a*sqrt(aroot)+b*sqrt(broot)))

        printall([f"α={float(alph):g}°", f"β={float(bet):g}°", f"γ={float(gam):g}°", f"S={area}", f"R={BigRadius}", f"r={SmallRadius}", f"h(a)={halpha}", f"h(b)={hbeta}", f"h(c)={hgamma}"])
    sinus=[0,[0,1],30,[1,2],45,[2,2],60,[3,2],90,[1,1],120,[3,2],135,[2,2],150,[1,2]]
    WIDTH = 700
    HEIGHT = 700

    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.title('По 3 сторонам')

    frame = tk.Frame(root, padx=20, pady=20)
    frame.grid()

    alabel = tk.Label(frame, text='a=')
    alabel.grid(column=0, row=0)

    entry_a = tk.Entry(frame)
    entry_a.grid(column=1, row=0)

    arootlabel = tk.Label(frame, text='√')
    arootlabel.grid(column=2, row=0)

    entry_aroot = tk.Entry(frame)
    entry_aroot.grid(column=3, row=0)

    blabel = tk.Label(frame, text='b=')
    blabel.grid(column=0, row=1)

    entry_b = tk.Entry(frame)
    entry_b.grid(column=1, row=1)

    brootlabel = tk.Label(frame, text='√')
    brootlabel.grid(column=2, row=1)

    entry_broot = tk.Entry(frame)
    entry_broot.grid(column=3, row=1)

    clabel = tk.Label(frame, text='c=')
    clabel.grid(column=0, row=2)

    entry_c = tk.Entry(frame)
    entry_c.grid(column=1, row=2)

    crootlabel = tk.Label(frame, text='√')
    crootlabel.grid(column=2, row=2)

    entry_croot = tk.Entry(frame)
    entry_croot.grid(column=3, row=2)

    button = tk.Button(frame, text="Рассчитать", command=draw_vector)
    button.grid()


def HeightSide():


    

    def draw_vector():
        a = int(entry_a.get())
        h = int(entry_h.get())
        aroot = int(entry_aroot.get())
        hroot = int(entry_hroot.get())
        area=simplify(a*h*sqrt(aroot*hroot)/2)
        uwu = tk.Label(root, text = f"S={area}")
        uwu.grid()
    WIDTH = 700
    HEIGHT = 700

    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.grid()

    text_a = tk.Label(frame, text = 'a=')
    text_a.grid(column=0, row=0)

    entry_a = tk.Entry(frame)
    entry_a.grid(column=1, row=0)

    arootlabel = tk.Label(frame, text='√')
    arootlabel.grid(column=2, row=0)

    entry_aroot = tk.Entry(frame)
    entry_aroot.grid(column=3, row=0)

    text_h = tk.Label(frame, text = 'h=')
    text_h.grid(column=0, row=1)


    entry_h = tk.Entry(frame)
    entry_h.grid(column=1, row=1)

    hrootlabel = tk.Label(frame, text='√')
    hrootlabel.grid(column=2, row=1)

    entry_hroot = tk.Entry(frame)
    entry_hroot.grid(column=3, row=1)

    

    button = tk.Button(frame, text="Draw vector", command=draw_vector)
    button.grid(column=0, row=2)




def AngleTwoSides():


    def printall(c, alpha, beta, S, R, r, halpha, hbeta, hgamma, malpha, mbeta, mgamma, lalpha, lbeta, lgamma):

        S_label = tk.Label(root, text=S)
        S_label.grid(row=4, column=0)

        
    def draw_vector():
        try:
            a = int(entry_a.get())
            b = int(entry_b.get())
            aroot = int(entry_aroot.get())
            broot = int(entry_broot.get())
            gam = int(entry_gam.get())

        except ValueError:
            return

        cosinus=[0,[1,1],30,[3,2],45,[2,2],60,[1,2],90,[0,1],120,[-1,2],135,[-2,2],150,[-3,2]]
        sinus=[0,[0,1],30,[1,2],45,[2,2],60,[3,2],90,[1,1],120,[3,2],135,[2,2],150,[1,2]]

        if gam in cosinus: # Находим с
            gammacos=sqrt(cosinus[cosinus.index(gam)+1][0])/cosinus[cosinus.index(gam)+1][1]
            c=simplify(sqrt(a**2*aroot+b**2*broot-2*a*b*sqrt(aroot*broot)*gammacos))
            print(f"c={c}")

        else: 
            gammacos=round(cos(radians(gam)),4)
            c=simplify(a**2*aroot+b**2*broot-2*a*b*sqrt(aroot*broot)*gammacos)
            print(f"c=sqrt({c})")
            c=sqrt(c)
        alphacos=((b*sqrt(broot))**2+c**2-(a*sqrt(aroot))**2)/(2*b*broot*c) # Находим альфа
        alph=round(degrees(acos(simplify(alphacos))),1)



        bet=180-alph-gam # Находим бета
        bet=round(bet,1)



        if gam in sinus: gammasin=sqrt(sinus[sinus.index(gam)+1][0])/sinus[sinus.index(gam)+1][1]
        else: gammasin=round(sin(radians(gam)),3)

        if bet in sinus: betasin=sqrt(sinus[sinus.index(bet)+1][0])/sinus[sinus.index(bet)+1][1]
        else: betasin=round(sin(radians(bet)),3)

        if alph in sinus: alphasin=sqrt(sinus[sinus.index(alph)+1][0])/sinus[sinus.index(alph)+1][1]
        else: alphasin=round(sin(radians(alph)),3)

        area=simplify(a*b*sqrt(aroot*broot)*gammasin/2) # Находим площадь



        BigRadius=simplify(c/gammasin/2) # Находим радиус описанной около треугольника окружности



        SmallRadius=simplify(2*area/(a*aroot+b*broot+c))



        halpha=simplify(b*broot*gammasin)

        hbeta=simplify(a*aroot*gammasin)

        hgamma=simplify(b*broot*alphasin)

        malpha=simplify(sqrt(2*b**2*broot+2*c**2-a**2*aroot)/2)

        mbeta=simplify(sqrt(2*a**2*aroot+2*c**2-b**2*broot)/2)

        mgamma=simplify(sqrt(2*a**2*aroot+2*b**2*broot-c**2)/2)

        lalpha=simplify(sqrt(b*sqrt(broot)*c*(a*sqrt(aroot)+b*sqrt(broot)+c)*(b*sqrt(broot)+c-a*sqrt(aroot)))/(b*sqrt(broot)+c))

        lbeta=simplify(sqrt(a*sqrt(aroot)*c*(a*sqrt(aroot)+b*sqrt(broot)+c)*(a*sqrt(aroot)+c-b*sqrt(broot)))/(a*sqrt(aroot)+c))

        lgamma=simplify(sqrt(a*b*sqrt(aroot*broot)*(a*sqrt(aroot)+b*sqrt(broot)+c)*(a*sqrt(aroot)+b*sqrt(broot)-c))/(a*sqrt(aroot)+b*sqrt(broot)))

        printall(f"c={c}", f"α={float(alph):g}°", f"β={float(bet):g}°", f"S={area}", f"R={BigRadius}", f"r={SmallRadius}", f"h(α)={halpha}",f"h(β)={hbeta}",f"h(γ)={hgamma}",f"m(α)={malpha}",f"m(β)={mbeta}",f"m(γ)={mgamma}",f"l(α)={lalpha}",f"l(β)={lbeta}",f"l(γ)={lgamma}")



    WIDTH = 700
    HEIGHT = 700

    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.grid()

    text_a = tk.Label(frame, text = 'a=')
    text_a.grid(column=0, row=0)

    entry_a = tk.Entry(frame)
    entry_a.grid(column=1, row=0)

    arootlabel = tk.Label(frame, text='√')
    arootlabel.grid(column=2, row=0)

    entry_aroot = tk.Entry(frame)
    entry_aroot.grid(column=3, row=0)

    text_h = tk.Label(frame, text = 'b=')
    text_h.grid(column=0, row=1)


    entry_b = tk.Entry(frame)
    entry_b.grid(column=1, row=1)

    hrootlabel = tk.Label(frame, text='√')
    hrootlabel.grid(column=2, row=1)

    entry_broot = tk.Entry(frame)
    entry_broot.grid(column=3, row=1)

    text_gam = tk.Label(frame, text='α=')
    text_gam.grid(column=0, row=2)
    entry_gam = tk.Entry(frame)
    entry_gam.grid(column=1, row=2)

    button = tk.Button(frame, text="рассчитать", command=draw_vector)
    button.grid()



    root.mainloop()



def SidesThree():
    print("Если отсутствует корень, то напишите на его месте 1")
    print("Введите все известные элементы треугольника")
    print("a, b и c - стороны треугольника")
    def printall(array):
        for element in array:
            UWU = tk.Label(root, text = element)
            UWU.grid(row=4, column=0)
    def draw_vector():
        try:
            a = int(entry_a.get())
            aroot = int(entry_aroot.get())
            b = int(entry_b.get())
            broot = int(entry_broot.get())
            c = int(entry_c.get())
            croot = int(entry_croot.get())

        except ValueError:
            return
        alphacos=simplify((b**2*broot+c**2*croot-a**2*aroot)/(2*a*sqrt(aroot)*c*sqrt(croot))) # Находим альфа
        alph=round(degrees(acos(simplify(alphacos))),2)



        betacos=simplify((a**2*aroot+c**2*croot-b**2*broot)/(2*a*sqrt(aroot)*c*sqrt(croot))) # Находим бета
        bet=round(degrees(acos(simplify(betacos))),2)



        gam=180-alph-bet # Находим гамма



        if gam in sinus: gammasin=sqrt(sinus[sinus.index(gam)+1][0])/sinus[sinus.index(gam)+1][1]
        else: gammasin=round(sin(radians(gam)),3)

        if bet in sinus: betasin=sqrt(sinus[sinus.index(bet)+1][0])/sinus[sinus.index(bet)+1][1]
        else: betasin=round(sin(radians(bet)),3)

        if alph in sinus: alphasin=sqrt(sinus[sinus.index(alph)+1][0])/sinus[sinus.index(alph)+1][1]
        else: alphasin=round(sin(radians(alph)),3)


        area=simplify(a*b*sqrt(aroot*broot)*gammasin/2) # Находим площадь


        BigRadius=simplify(c*sqrt(croot)/gammasin/2) # Находим радиус описанной около треугольника окружности



        SmallRadius=simplify(2*area/(a*sqrt(aroot)+b*sqrt(broot)+c*sqrt(croot)))



        
        
        halpha=simplify(b*sqrt(broot)*gammasin)

        hbeta=simplify(a*sqrt(aroot)*gammasin)

        hgamma=simplify(b*sqrt(broot)*alphasin)




        malpha=simplify(sqrt(2*b**2*broot+2*c**2*croot-a**2*aroot)/2)

        mbeta=simplify(sqrt(2*a**2*aroot+2*c**2*croot-b**2*broot)/2)

        mgamma=simplify(sqrt(2*a**2*aroot+2*b**2*broot-c**2*croot)/2)




        lalpha=simplify(sqrt(b*c*sqrt(broot*croot)*(a*sqrt(aroot)+b*sqrt(broot)+c*sqrt(croot))*(b*sqrt(broot)+c*sqrt(croot)-a*sqrt(aroot)))/(b*sqrt(broot)+c*sqrt(croot)))

        lbeta=simplify(sqrt(a*sqrt(aroot*croot)*c*(a*sqrt(aroot)+b*sqrt(broot)+c*sqrt(croot))*(a*sqrt(aroot)+c*sqrt(croot)-b*sqrt(broot)))/(a*sqrt(aroot)+c*sqrt(croot)))

        lgamma=simplify(sqrt(a*b*sqrt(aroot*broot)*(a*sqrt(aroot)+b*sqrt(broot)+c*sqrt(croot))*(a*sqrt(aroot)+b*sqrt(broot)-c*sqrt(croot)))/(a*sqrt(aroot)+b*sqrt(broot)))

        printall([f"S={area}"])
    sinus=[0,[0,1],30,[1,2],45,[2,2],60,[3,2],90,[1,1],120,[3,2],135,[2,2],150,[1,2]]
    WIDTH = 700
    HEIGHT = 700

    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.grid()

    text_a = tk.Label(frame, text = 'a=')
    text_a.grid(column=0, row=0)

    entry_a = tk.Entry(frame)
    entry_a.grid(column=1, row=0)

    arootlabel = tk.Label(frame, text='√')
    arootlabel.grid(column=2, row=0)

    entry_aroot = tk.Entry(frame)
    entry_aroot.grid(column=3, row=0)

    text_h = tk.Label(frame, text = 'b=')
    text_h.grid(column=0, row=1)


    entry_b = tk.Entry(frame)
    entry_b.grid(column=1, row=1)

    hrootlabel = tk.Label(frame, text='√')
    hrootlabel.grid(column=2, row=1)

    entry_broot = tk.Entry(frame)
    entry_broot.grid(column=3, row=1)

    text_h = tk.Label(frame, text = 'c=')
    text_h.grid(column=0, row=2)


    entry_c = tk.Entry(frame)
    entry_c.grid(column=1, row=2)

    hrootlabel = tk.Label(frame, text='√')
    hrootlabel.grid(column=2, row=2)

    entry_croot = tk.Entry(frame)
    entry_croot.grid(column=3, row=2)

    button = tk.Button(frame, text="рассчитать", command=draw_vector)
    button.grid()




def TwoСathets():




    def printall(array):
        for element in array:
            UWU = tk.Label(root, text = element)
            UWU.grid(row=3, column=0)
    def draw_vector():
        try:
            a = int(entry_a.get())
            aroot = int(entry_aroot.get())
            b = int(entry_b.get())
            broot = int(entry_broot.get())


        except ValueError:
            return
        area=simplify(a*b*sqrt(aroot*broot)/2)



        


        printall([f"S={area}"])
    sinus=[0,[0,1],30,[1,2],45,[2,2],60,[3,2],90,[1,1],120,[3,2],135,[2,2],150,[1,2]]
    WIDTH = 700
    HEIGHT = 700

    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.grid()

    text_a = tk.Label(frame, text = 'a=')
    text_a.grid(column=0, row=0)

    entry_a = tk.Entry(frame)
    entry_a.grid(column=1, row=0)

    arootlabel = tk.Label(frame, text='√')
    arootlabel.grid(column=2, row=0)

    entry_aroot = tk.Entry(frame)
    entry_aroot.grid(column=3, row=0)

    text_h = tk.Label(frame, text = 'b=')
    text_h.grid(column=0, row=1)


    entry_b = tk.Entry(frame)
    entry_b.grid(column=1, row=1)

    hrootlabel = tk.Label(frame, text='√')
    hrootlabel.grid(column=2, row=1)

    entry_broot = tk.Entry(frame)
    entry_broot.grid(column=3, row=1)

    

    button = tk.Button(frame, text="рассчитать", command=draw_vector)
    button.grid()

def EqualSides():


    frame = tk.Tk()
    frame.geometry("300x200")

    # Создаем поля ввода
    text_a = tk.Label(frame, text = 'a=')
    text_a.grid(column=0, row=0)

    a = tk.Entry(frame)
    a.grid(column=1, row=0)

    arootlabel = tk.Label(frame, text='√')
    arootlabel.grid(column=2, row=0)

    aroot = tk.Entry(frame)
    aroot.grid(column=3, row=0)

    # Функция для вывода сообщения
    def display_message():
        area=simplify(int(a.get())**2*int(aroot.get())*sqrt(3)/4)
        message = tk.Label(frame, text=f"S={area}")
        message.grid()

    # Создаем кнопку
    button = tk.Button(frame, text="рассчитать", command=display_message)
    button.grid()

    # Запускаем окно
    #window.mainloop()


def SmallRadius():
    window = tk.Tk()
    window.title('По радиусу вписанной окружности и периметру')
    window.geometry("600x400")

    # Создаем поля ввода
    plabel = tk.Label(window, text='P=')
    plabel.grid(column=0, row=0)

    p_input = tk.Entry(window)
    p_input.grid(column=1, row=0)

    prootlabel = tk.Label(window, text='√')
    prootlabel.grid(column=2, row=0)

    proot_input = tk.Entry(window)
    proot_input.grid(column=3, row=0)

    rlabel = tk.Label(window, text='r=')
    rlabel.grid(column=0, row=1)

    r_input = tk.Entry(window)
    r_input.grid(column=1, row=1)

    rrootlabel = tk.Label(window, text='√')
    rrootlabel.grid(column=2, row=1)

    rroot_input = tk.Entry(window)
    rroot_input.grid(column=3, row=1)

    # Функция для вывода сообщения
    def display_message():
        P = int(p_input.get())
        r = int(r_input.get())
        Proot = int(proot_input.get())
        rroot = int(rroot_input.get())

        result = P*r*sqrt(Proot*rroot)/2
        message = tk.Label(window, text=f"Результат: {result}")
        message.grid(row=3, column=0)

    # Создаем кнопку
    button = tk.Button(window, text="Рассчитать", command=display_message)
    button.grid()

    # Запускаем окно
    window.mainloop()


def BigRadius():
    window = tk.Tk()
    window.geometry("300x250")

    # Создаем поля ввода
    text_a = tk.Label(window, text='a=')
    text_a.grid(column=0, row=0)

    a_input = tk.Entry(window)
    a_input.grid(column=1, row=0)

    text_b = tk.Label(window, text='b=')
    text_b.grid(column=0, row=1)

    b_input = tk.Entry(window)
    b_input.grid(column=1, row=1)

    text_c = tk.Label(window, text='c=')
    text_c.grid(column=0, row=2)

    c_input = tk.Entry(window)
    c_input.grid(column=1, row=2)

    text_r = tk.Label(window, text='r=')
    text_r.grid(column=0, row=3)

    r_input = tk.Entry(window)
    r_input.grid(column=1, row=3)

    text_aroot = tk.Label(window, text='√')
    text_broot = tk.Label(window, text='√')
    text_croot = tk.Label(window, text='√')
    text_rroot = tk.Label(window, text='√')
    text_aroot.grid(column=2, row=0)
    aroot_input = tk.Entry(window)
    aroot_input.grid(column=3, row=0)
    text_broot.grid(column=2, row=1)
    broot_input = tk.Entry(window)
    broot_input.grid(column=3, row=1)
    text_croot.grid(column=2, row=2)
    croot_input = tk.Entry(window)
    croot_input.grid(column=3, row=2)
    text_rroot.grid(column=2, row=3)
    rroot_input = tk.Entry(window)
    rroot_input.grid(column=3, row=3)

    # Функция для вывода сообщения
    def display_message():
        a = float(a_input.get())
        b = float(b_input.get())
        c = float(c_input.get())
        r = float(r_input.get())
        aroot = float(aroot_input.get())
        broot = float(broot_input.get())
        croot = float(croot_input.get())
        rroot = float(rroot_input.get())

        numerator = a * b * c * sqrt(aroot * broot * croot)
        denominator = 4 * r * sqrt(rroot)

        result = numerator / denominator
        message = tk.Label(window, text=f"Результат: {result:.2f}")
        message.grid()

    # Создаем кнопку
    button = tk.Button(window, text="Рассчитать", command=display_message)
    button.grid()

    # Запускаем окно
    window.mainloop()


def OneSideThreeAngles():
    print("Если отсутствует корень, то напишите на его месте 1")
    print("a - сторона треугольника, α, β и γ - его углы")

    sinus=[0,[0,1],30,[1,2],45,[2,2],60,[3,2],90,[1,1],120,[3,2],135,[2,2],150,[1,2]]


    window = tk.Tk()
    window.geometry("300x250")

    # Создаем поля ввода
    text_a = tk.Label(window, text='a=')
    text_a.grid(column=0, row=0)

    a_input = tk.Entry(window)
    a_input.grid(column=1, row=0)

    text_alph = tk.Label(window, text='α=')
    text_alph.grid(column=0, row=1)

    alph_input = tk.Entry(window)
    alph_input.grid(column=1, row=1)

    text_bet = tk.Label(window, text='β=')
    text_bet.grid(column=0, row=2)

    bet_input = tk.Entry(window)
    bet_input.grid(column=1, row=2)

    text_gam = tk.Label(window, text='γ=')
    text_gam.grid(column=0, row=3)

    gam_input = tk.Entry(window)
    gam_input.grid(column=1, row=3)

    text_aroot = tk.Label(window, text='√')
    text_aroot.grid(column=2, row=0)

    aroot_input = tk.Entry(window)
    aroot_input.grid(column=3, row=0)

    

    # Функция для вывода сообщения
    def display_message():
        a = float(a_input.get())
        alph = float(alph_input.get())
        bet = float(bet_input.get())
        gam = float(gam_input.get())
        aroot = float(aroot_input.get())
        sinus=[0,[0,1],30,[1,2],45,[2,2],60,[3,2],90,[1,1],120,[3,2],135,[2,2],150,[1,2]]

        

        if gam in sinus: gammasin=sqrt(sinus[sinus.index(gam)+1][0])/sinus[sinus.index(gam)+1][1]
        else: gammasin=round(sin(radians(gam)),3)

        if bet in sinus: betasin=sqrt(sinus[sinus.index(bet)+1][0])/sinus[sinus.index(bet)+1][1]
        else: betasin=round(sin(radians(bet)),3)

        if alph in sinus: alphasin=sqrt(sinus[sinus.index(alph)+1][0])/sinus[sinus.index(alph)+1][1]
        else: alphasin=round(sin(radians(alph)),3)


        area=simplify(a**2*aroot*betasin*gammasin/alphasin)
        message = tk.Label(window, text=f"Результат: {area}")
        message.grid(row=5, column=0)

    # Создаем кнопку
    button = tk.Button(window, text="Рассчитать", command=display_message)
    button.grid()

    # Запускаем окно
    window.mainloop()


def BigRadiusThreeAngles():


    window = tk.Tk()
    window.geometry("300x250")

    # Создаем поля ввода
    text_a = tk.Label(window, text='r=')
    text_a.grid(column=0, row=0)

    r_input = tk.Entry(window)
    r_input.grid(column=1, row=0)

    text_alph = tk.Label(window, text='α=')
    text_alph.grid(column=0, row=1)

    alph_input = tk.Entry(window)
    alph_input.grid(column=1, row=1)

    text_bet = tk.Label(window, text='β=')
    text_bet.grid(column=0, row=2)

    bet_input = tk.Entry(window)
    bet_input.grid(column=1, row=2)

    text_gam = tk.Label(window, text='γ=')
    text_gam.grid(column=0, row=3)

    gam_input = tk.Entry(window)
    gam_input.grid(column=1, row=3)

    text_aroot = tk.Label(window, text='√')
    text_aroot.grid(column=2, row=0)

    rroot_input = tk.Entry(window)
    rroot_input.grid(column=3, row=0)

    

    # Функция для вывода сообщения
    def display_message():
        r = float(r_input.get())
        alph = float(alph_input.get())
        bet = float(bet_input.get())
        gam = float(gam_input.get())
        rroot = float(rroot_input.get())
        sinus=[0,[0,1],30,[1,2],45,[2,2],60,[3,2],90,[1,1],120,[3,2],135,[2,2],150,[1,2]]

        

        if gam in sinus: gammasin=sqrt(sinus[sinus.index(gam)+1][0])/sinus[sinus.index(gam)+1][1]
        else: gammasin=round(sin(radians(gam)),3)

        if bet in sinus: betasin=sqrt(sinus[sinus.index(bet)+1][0])/sinus[sinus.index(bet)+1][1]
        else: betasin=round(sin(radians(bet)),3)

        if alph in sinus: alphasin=sqrt(sinus[sinus.index(alph)+1][0])/sinus[sinus.index(alph)+1][1]
        else: alphasin=round(sin(radians(alph)),3)


        area=simplify(2*r**2*rroot*alphasin*betasin*gammasin)
        message = tk.Label(window, text=f"Результат: {area}")
        message.grid(row=5, column=0)

    # Создаем кнопку
    button = tk.Button(window, text="Рассчитать", command=display_message)
    button.grid()

    # Запускаем окно
    window.mainloop()


def CircleLenght():
    print("Если отсутствует корень, то напишите на его месте 1")
    print("R - радиус окружности")




    


    window = tk.Tk()
    window.geometry("300x200")

    # Создаем поля ввода
    text_r = tk.Label(window, text='r=')
    text_r.grid(column=0, row=0)
    r = tk.Entry(window)
    r.grid(column=1, row=0)
    text_rroot = tk.Label(window, text='√')
    text_rroot.grid(column=2, row=0)
    rroot = tk.Entry(window)
    rroot.grid(column=3, row=0)

    # Функция для вывода сообщения
    def display_message():
        π=symbols("π")
        lenght=simplify(2*int(r.get())*sqrt(int(rroot.get()))*π)
        message = tk.Label(window, text=f"Длина окружности: {lenght}")
        message.grid(row=2, column=0)

    # Создаем кнопку
    button = tk.Button(window, text="рассчитать", command=display_message)
    button.grid()

    # Запускаем окно
    window.mainloop()


def ArcLenght():
    print("Если отсутствует корень, то напишите на его месте 1")
    print("R - радиус окружности, α - градусная мера дуги окружности")



    window = tk.Tk()
    window.geometry("300x200")

    # Создаем поля ввода
    text_r = tk.Label(window, text='r=')
    text_r.grid(column=0, row=0)
    r = tk.Entry(window)
    r.grid(column=1, row=0)
    text_rroot = tk.Label(window, text='√')
    text_rroot.grid(column=2, row=0)
    rroot = tk.Entry(window)
    rroot.grid(column=3, row=0)

    text_alph = tk.Label(window, text='α=')
    text_alph.grid(column=0, row=1)
    alph = tk.Entry(window)
    alph.grid(column=1, row=1)

    # Функция для вывода сообщения
    def display_message():
        π=symbols("π")
        lenght=simplify(2*int(r.get())*sqrt(int(rroot.get()))*π*int(alph.get())/360)
        message = tk.Label(window, text=f"Длина дуги окружности: {lenght}")
        message.grid(row=3, column=0)

    # Создаем кнопку
    button = tk.Button(window, text="рассчитать", command=display_message)
    button.grid()

    # Запускаем окно
    window.mainloop()


def CircleArea():
    print("Если отсутствует корень, то напишите на его месте 1")
    print("R - радиус окружности")






    window = tk.Tk()
    window.geometry("300x200")

    # Создаем поля ввода
    text_r = tk.Label(window, text='r=')
    text_r.grid(column=0, row=0)
    r = tk.Entry(window)
    r.grid(column=1, row=0)
    text_rroot = tk.Label(window, text='√')
    text_rroot.grid(column=2, row=0)
    rroot = tk.Entry(window)
    rroot.grid(column=3, row=0)



    # Функция для вывода сообщения
    def display_message():
        π=symbols("π")
        area=simplify(int(r.get())**2*int(rroot.get())*π)
        message = tk.Label(window, text=f"{area}")
        message.grid(row=2, column=0)

    # Создаем кнопку
    button = tk.Button(window, text="рассчитать", command=display_message)
    button.grid()

    # Запускаем окно
    window.mainloop()


def SectorArea():
    print("Если отсутствует корень, то напишите на его месте 1")
    print("R - радиус окружности, α - градусная мера дуги окружности")



    window = tk.Tk()
    window.geometry("300x200")

    # Создаем поля ввода
    text_r = tk.Label(window, text='r=')
    text_r.grid(column=0, row=0)
    r = tk.Entry(window)
    r.grid(column=1, row=0)
    text_rroot = tk.Label(window, text='√')
    text_rroot.grid(column=2, row=0)
    rroot = tk.Entry(window)
    rroot.grid(column=3, row=0)

    text_alph = tk.Label(window, text='α=')
    text_alph.grid(column=0, row=1)
    alph = tk.Entry(window)
    alph.grid(column=1, row=1)

    # Функция для вывода сообщения
    def display_message():
        π=symbols("π")
        area=simplify(int(r.get())**2*int(rroot.get())*π*int(alph.get())/360)
        message = tk.Label(window, text=f"Площадь сектора круга: {area}")
        message.grid(row=3, column=0)

    # Создаем кнопку
    button = tk.Button(window, text="рассчитать", command=display_message)
    button.grid()

    # Запускаем окно
    window.mainloop()


def SegmentArea():
    print("Если отсутствует корень, то напишите на его месте 1")
    print("R - радиус окружности, α - градусная мера дуги окружности")



    window = tk.Tk()
    window.geometry("500x300")
    window.title('Площадь сегмента круга')
    rlabel = tk.Label(window, text='r=')
    rlabel.grid(column=0, row=0)
    # Создаем поля ввода
    r_entry = tk.Entry(window)
    r_entry.grid(column=1, row=0)

    rrootlabel = tk.Label(window, text='√')
    rrootlabel.grid(column=2, row=0)

    rroot_entry = tk.Entry(window)
    rroot_entry.grid(column=3, row=0)

    alphlabel = tk.Label(window, text='α=')
    alphlabel.grid(column=0, row=1)

    alph_entry = tk.Entry(window)
    alph_entry.grid(column=1, row=1)

    # Функция для вывода сообщения
    def display_message():
        sinus=[0,[0,1],30,[1,2],45,[2,2],60,[3,2],90,[1,1],120,[3,2],135,[2,2],150,[1,2]]
        π=symbols("π")
        r=int(r_entry.get())
        rroot=int(rroot_entry.get())
        alph=int(alph_entry.get())
        area=0

        if alph in sinus: alphasin=sqrt(sinus[sinus.index(alph)+1][0])/sinus[sinus.index(alph)+1][1]
        else: alphasin=round(sin(radians(alph)),3)

        π=symbols("π")

        if alph<180: area=simplify(r**2*rroot*π*alph/360-r**2*rroot*alphasin/2)
        else: area=simplify(r**2*rroot*π*alph/360+r**2*rroot*alphasin/2)

        message = tk.Label(window, text=f"S= {area}")
        message.grid(row=3, column=0)

    # Создаем кнопку
    button = tk.Button(window, text="Рассчитать", command=display_message)
    button.grid()

    # Запускаем окно
    window.mainloop()




window=tk.Tk()
window.title("Калькулятор")
window.geometry("750x550")
window["bg"]="white"

intro=tk.Label(window, text = "Выбор действия", font=("Arial", 15, "bold"), bg="white").grid(pady=2, column=0, row=0)



veklabel=tk.Label(window, text = "Векторы:", font=("Arial", 12), bg="white").grid(pady=2, column=0, row=1)
btn7=tk.Button(text="Координаты вектора", width=50, command=VectorCoordinates).grid(pady=2, column=0, row=2)
btn2=tk.Button(text="Середина отрезка", width=50, command=SegmentMiddle).grid(pady=2, column=0, row=3)
btn1=tk.Button(text="Расстояние между двумя точками", width=50, command=DotDistance).grid(pady=2, column=0, row=4)
btn3=tk.Button(text="Длина вектора", width=50, command=VektorModul).grid(pady=2, column=0, row=5)
btn5=tk.Button(text="Скалярное произведение векторов", width=50, command=VectorMultiplication).grid(pady=2, column=0, row=6)
strilabel=tk.Label(window, text = "Площадь треугольника:", font=("Arial", 12), bg="white").grid(pady=2, column=0, row=7)
sbtn1=tk.Button(text="По высоте и стороне, к которой она проведена", width=50, command=HeightSide).grid(pady=2, column=0, row=8)
sbtn2=tk.Button(text="По 2 сторона и углу между ними", width=50, command=AngleTwoSides).grid(pady=2, column=0, row=9)
sbtn3=tk.Button(text="По 3 сторонам", width=50, command=SidesThree).grid(pady=2, column=0, row=10)
sbtn4=tk.Button(text="По катетам прямоугольного треугольника", width=50, command=TwoСathets).grid(pady=2, column=0, row=11)
sbtn5=tk.Button(text="По стороне правильного треугольника", width=50, command=EqualSides).grid(pady=2, column=0, row=12)
sbtn6=tk.Button(text="По радиусу вписанной окружности и периметру", width=50, command=SmallRadius).grid(pady=2, column=0, row=13)
sbtn7=tk.Button(text="По радиусу описанной окружности и 3 сторонам", width=50, command=BigRadius).grid(pady=2, column=0, row=14)
sbtn8=tk.Button(text="По стороне и 3 углам", width=50, command=OneSideThreeAngles).grid(pady=2, column=0, row=15)
sbtn9=tk.Button(text="По радиусу описанной окружности и 3 углам", width=50, command=BigRadiusThreeAngles).grid(pady=2, column=0, row=16)



rtrilabel=tk.Label(window, text = "Решение треугольника:", font=("Arial", 12), bg="white").grid(pady=2, column=1, row=1)
rbtn1=tk.Button(text="По 2 сторонам и углу между ними", width=50, command=TwoSidesOneAngle).grid(pady=2, column=1, row=2)
rbtn2=tk.Button(text="По стороне и 2 прилежащим углам", width=50, command=OneSideTwoAngles).grid(pady=2, column=1, row=3)
rbtn3=tk.Button(text="По 3 сторонам", width=50, command=ThreeSides).grid(pady=2, column=1, row=4)

okrlabel=tk.Label(window, text = "Окружность:", font=("Arial", 12), bg="white").grid(pady=2, column=1, row=5)
okbtn1=tk.Button(text="Длина окружности", width=50, command=CircleLenght).grid(pady=2, column=1, row=6)
okbtn2=tk.Button(text="Длина дуги окружности", width=50, command=ArcLenght).grid(pady=2, column=1, row=7)

kruglabel=tk.Label(window, text = "Круг:", font=("Arial", 12), bg="white").grid(pady=2, column=1, row=8)

okbtn3=tk.Button(text="Площадь круга", width=50, command=CircleArea).grid(pady=2, column=1, row=9)
okbtn4=tk.Button(text="Площадь сектора круга", width=50, command=SectorArea).grid(pady=2, column=1, row=10)
okbtn5=tk.Button(text="Площадь сегмента круга", width=50, command=SegmentArea).grid(pady=2, column=1, row=11)

urlabel=tk.Label(window, text = "Уравнения:", font=("Arial", 12), bg="white").grid(pady=2, column=1, row=12)
btn4=tk.Button(text="Уравнение прямой", width=50, command=StraightsEquation).grid(pady=2, column=1, row=13)
btn6=tk.Button(text="Уравнение окружности", width=50, command=CircleEquation).grid(pady=2, column=1, row=14)

#btn8=tk.Button(text="Решение треугольника", width=30, command=ReshitTreugolnik).grid(pady=2)
#btn9=tk.Button(text="Площадь треугольника", width=30, command=TriangleAreas).grid(pady=2)
#btn10=tk.Button(text="Круг и окружность", width=30, command=CircleRound).grid(pady=2)
window.mainloop()


