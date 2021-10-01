from flask import Blueprint, render_template, request, flash
import numpy as np
import math

auth = Blueprint('auth', __name__)

@auth.route('/basicalgebra', methods=['GET', 'POST'])
def basicanswer():
    data = request.form
    print(data)
    coeficient1 = request.form['coeficient1']
    constent1 = request.form['constent1']
    coeficient2 = request.form['coeficient2']
    constent2 = request.form['constent2']
    try:
        side1= float(coeficient1) - float(coeficient2)
        side2= float(constent2) - float(constent1)
        solution = float(side2)/float(side1)
    except Exception:
        return render_template('basicalgebra.html')
    if request.method == 'POST':
        return render_template('basicsolution.html', solution=solution)

@auth.route('/quadraticequations', methods=['GET', 'POST'])
def quadraticanswer():
    data = request.form
    print(data)
    a = request.form['coeficient1']
    b = request.form['coeficient2']
    c = request.form['constent1']
    #solution1 = ((-1*float(b))+((float(b)**2-(4*float(a)*float(c))**.5))/(2*float(a))
    #solution2 = ((-1*float(b))-((float(b)**2-(4*float(a)*float(c))**.5))/(2*float(a))
    try:
        beginning = -1 * float(b)
        middle= float(b)**2 - (4*float(a)*float(c))
        end= float(a) * 2
        middle2= float(middle)**.5
        solution1a= float(beginning) + float(middle2)
        solution2a= float(beginning) - float(middle2)
        solution1b= float(solution1a) / float(end)
        solution2b= float(solution2a) / float(end)
    except Exception:
        return render_template('quadraticequations.html')
    
    
    
    if request.method == 'POST':
        return render_template('quadraticsolution.html', solution1b=solution1b, solution2b = solution2b)
        
@auth.route('/quadraticfactor', methods=['GET', 'POST'])
def factoranswer():
    data = request.form
    print(data)
    a = request.form['coeficient1']
    b = request.form['coeficient2']
    c = request.form['constent1']
    #solution1 = ((-1*float(b))+((float(b)**2-(4*float(a)*float(c))**.5))/(2*float(a))
    #solution2 = ((-1*float(b))-((float(b)**2-(4*float(a)*float(c))**.5))/(2*float(a))
    try:
        beginning = -1 * float(b)
        middle= float(b)**2 - (4*float(a)*float(c))
        end= float(a) * 2
        middle2= float(middle)**.5
        solution1a= float(beginning) + float(middle2)
        solution2a= float(beginning) - float(middle2)
        solution1b= float(solution1a) / float(end)
        solution2b= float(solution2a) / float(end)
        solution1c= float(solution1b) * -1
        solution2c= float(solution2b) * -1
    except Exception:
        return render_template('quadraticfactor.html')
    
    
    
    if request.method == 'POST':
        return render_template('factorsolution.html', solution1c=solution1c, solution2c = solution2c)

@auth.route('/foil', methods=['GET', 'POST'])
def foilanswer():
    data = request.form
    print(data)
    coeficient1 = request.form['coeficient1']
    constent1 = request.form['constent1']
    coeficient2 = request.form['coeficient2']
    constent2 = request.form['constent2']
    try:
        f = float(coeficient1) * float(coeficient2)
        o = float(coeficient1) * float(constent2)
        i = float(constent1) * float(coeficient2)
        l = float(constent1) * float(constent2)
        beginning = float(f)
        middle = float(o) + float(i)
        end = float(l)
    except Exception:
        return render_template('foil.html')




    if request.method == 'POST':
        return render_template('foilsolution.html', beginning = beginning, middle = middle, end = end)

@auth.route('/foil2', methods=['GET', 'POST'])
def foil2answer():
    data = request.form
    print(data)
    coeficient1 = request.form['coeficient1']
    constent1 = request.form['constent1']
    coeficient2 = request.form['coeficient2']
    constent2 = request.form['constent2']
    try:
        f = float(coeficient1) * float(coeficient2)
        o = float(coeficient1) * float(constent2)
        i = float(constent1) * float(coeficient2)
        l = float(constent1) * float(constent2)
        beginning = float(f)
        middle = float(o) + float(i)
        end = float(l)
    except Exception:
        return render_template('foil2.html')




    if request.method == 'POST':
        return render_template('foil2solution.html', beginning = beginning, middle = middle, end = end)

@auth.route('/slopestuff', methods=['GET', 'POST'])
def slopestuff():
    data = request.form
    print(data)
    x1 = request.form['x1']
    y1 = request.form['y1']
    x2 = request.form['x2']
    y2 = request.form['y2']
    try:
        slope1a = float(y1) - float(y2)
        slope1b = float(x1) - float(x2)
        slope = float(slope1a) / float(slope1b)
        b1 = float(slope) * float(x1)
        b = float(y1) - float(b1)
        
    except Exception:
        return render_template('slopestuff.html')




    if request.method == 'POST':
        return render_template('slopestuffsolution.html', slope = slope, b = b)

@auth.route('/inequalities', methods=['GET', 'POST'])
def inequalitiesanswer():
    data = request.form
    print(data)
    coeficient1 = request.form['coeficient1']
    constent1 = request.form['constent1']
    coeficient2 = request.form['coeficient2']
    constent2 = request.form['constent2']
    try:
        side1= float(coeficient1) - float(coeficient2)
        side2= float(constent2) - float(constent1)
        solution = float(side2)/float(side1)
    except Exception:
        return render_template('basicalgebra.html')
    if request.method == 'POST':
        if float(side1) > 0:
            return render_template('basicinequalitysolution.html', solution=solution, symbol='>')
        else:
            return render_template('basicinequalitysolution.html', solution=solution, symbol='<')

@auth.route('/2x2systems', methods=['GET', 'POST'])
def systemsanswer():
    data = request.form
    print(data)
    coeficient1 = request.form['coeficient1']
    coeficient2 = request.form['coeficient2']
    coeficient3 = request.form['coeficient3']
    coeficient4 = request.form['coeficient4']
    constent1 = request.form['constent1']
    constent2 = request.form['constent2']
    try:
        bottoma= float(coeficient1) * float(coeficient4)
        bottomb= float(coeficient2) * float(coeficient3)
        bottom= float(bottoma) - float(bottomb)
        topxa= float(constent1) * float(coeficient4)
        topxb= float(constent2) * float(coeficient2)
        topx = float(topxa) - float(topxb)
        topya= float(constent2) * float(coeficient1)
        topyb= float(constent1) * float(coeficient3)
        topy = float(topya) - float(topyb)
        x = float(topx) / float(bottom)
        y = float(topy) / float(bottom)
        
    except Exception:
        return render_template('2x2systems.html')
    
    if request.method == 'POST':
        return render_template('systemsolution.html', x = x , y = y)

@auth.route('/triangle', methods=['GET', 'POST'])
def triangle():
    data = request.form
    print(data)
    A = request.form['A']
    C = request.form['C']
    a = request.form['a']
    b = request.form['b']
    c = request.form['c']
    try:
        if float(A) > 0:
            C = 90 - float(A)
        if float(C) > 0:
            A = 90 - float(C)

        if float(a) > 0 and float(A) > 0:
            ca = math.sin(math.radians(C))
            c = float(a) / float(ca)
            b1 = float(c)**2
            b2 = float(a)**2
            b3 = float(b1) - float(b2)
            b = float(b3)**.5
        
        elif float(b) > 0 and float(A) > 0:
            ca = math.cos(math.radians(C))
            c = float(b) / float(ca)
            a1 = float(c)**2
            a2 = float(b)**2
            a3 = float(a1) - float(a2)
            a = float(a3)**.5
        

        elif float(c) > 0 and float(A) > 0:
            aa = math.sin(math.radians(C))
            a = float(c) * float(aa)
            b1 = float(c)**2
            b2 = float(a)**2
            b3 = float(b1) - float(b2)
            b = float(b3)**.5
        

    
        elif float(c) > 0 and float(b)>0:
        
            aa = float(c)**2
            ab = float(b)**2
            ac = float(aa)-float(ab)
            a = float(ac)**.5
            Aa = float(a)/float(c)
            Ab = math.acos((Aa))
        
            A = float(Ab) * 57.2958
            C = 90 - A
        

        elif float(c) > 0 and float(a)>0:
        
            ba = float(c)**2
            bb = float(b)**2
            bc = float(ba)-float(bb)
            b = float(bc)**.5
            Aa = float(a)/float(c)
            Ab = math.acos((Aa))
        
            A = float(Ab) * 57.2958
            C = 90 - A
        
        elif float(a) > 0 and float(b)>0:
        
            ca = float(a)**2
            cb = float(b)**2
            cc = float(ca)+float(cb)
            c = float(cc)**.5
            Aa = float(a)/float(c)
            Ab = math.acos((Aa))
        
            A = float(Ab) * 57.2958
            C = 90 - A
        
      

        
    except Exception:
        return render_template('trianglegenerator.html')

    if request.method == 'POST':
        return render_template('trianglesolution.html', a = a , b = b, c = c, A = A, C = C)


@auth.route('/rectangle', methods=['GET', 'POST'])
def rectangle():
    data = request.form
    print(data)
    base = request.form['base']
    height = request.form['height']
    
    try:
        area = float(base) * float(height)
        perimitera = float(base) * 2
        perimiterb = float(height) * 2
        perimiter = float(perimitera) + float(perimiterb)
    except Exception:
        return render_template('rectangle.html')
    if request.method == 'POST':
        return render_template('rectsolution.html', perimiter = perimiter, area = area)

@auth.route('/circle', methods=['GET', 'POST'])
def circle():
    data = request.form
    print(data)
    radius = request.form['radius']
    
    
    try:
        area = math.pi * float(radius) * float(radius)
        circumference = float(radius) * 2 * math.pi
        
    except Exception:
        return render_template('circle.html')
    if request.method == 'POST':
        return render_template('circlesolution.html', circumference = circumference, area = area)

@auth.route('/rectangularprism', methods=['GET', 'POST'])
def rectangularprism():
    data = request.form
    print(data)
    base = request.form['base']
    height = request.form['height']
    depth = request.form['depth']
    try:
        volume = float(base) * float(height) * float(depth)
        surfaceareaa = float(base) * float(height)
        surfaceareab = float(height) * float(depth)
        surfaceareac = float(base) * float(depth)
        surfacearea = float(surfaceareaa) + float(surfaceareab) + float(surfaceareac)
    except Exception:
        return render_template('rectanguularprism.html')
    if request.method == 'POST':
        return render_template('rectprismsolution.html', volume = volume, surfacearea = surfacearea)

@auth.route('/cylinder', methods=['GET', 'POST'])
def cylinder():
    data = request.form
    print(data)
    radius = request.form['radius']
    height = request.form['height']
    
    try:
        toparea = math.pi * float(radius) * float(radius)
        topcircumference = float(radius) * 2 * math.pi
        middle = float(topcircumference) * float(height)
        surfacearea1 = float(toparea) * 2
        surfacearea = float(surfacearea1) + float(middle)
        volume = float(toparea) * float(height)
        
    except Exception:
        return render_template('cylinder.html')
    if request.method == 'POST':
        return render_template('cylindersolution.html', volume = volume, surfacearea = surfacearea)

@auth.route('/sphere', methods=['GET', 'POST'])
def sphere():
    data = request.form
    print(data)
    radius = request.form['radius']
    
    
    try:
        volume = (4/3) * math.pi * float(radius) * float(radius) * float(radius)
        surfacearea = 4 * float(radius) * float(radius) * math.pi
        
    except Exception:
        return render_template('sphere.html')
    if request.method == 'POST':
        return render_template('spheresolution.html', volume = volume, surfacearea = surfacearea)

@auth.route('/gtriangle', methods=['GET', 'POST'])
def gtriangle():
    data = request.form
    print(data)
    base = request.form['base']
    height = request.form['height']
    
    try:
        area = float(base) * float(height) * .5
        perimitera = float(base) ** 2
        perimiterb = float(height) ** 2
        perimiterc = float(perimitera) + float(perimiterb)
        perimiter = float(perimiterc) ** .5
    except Exception:
        return render_template('gtriangle.html')
    if request.method == 'POST':
        return render_template('gtrianglesolution.html', perimiter = perimiter, area = area)

@auth.route('/trapazoid', methods=['GET', 'POST'])
def trapazoid():
    data = request.form
    print(data)
    base1 = request.form['base1']
    base2 = request.form['base2']
    height = request.form['height']
    
    try:
        area1 = float(base1) + float(base2)
        area = float(area1) * float(height) * .5
        
    except Exception:
        return render_template('trapazoid.html')
    if request.method == 'POST':
        return render_template('trapazoidsolution.html', area = area)


        