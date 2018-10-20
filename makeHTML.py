#Joan Chirinos
#4 fxn html calculator

#MAX_NUM is the max input value of the calculator - 1.
#Default is 5 --> [0, 4], which should generate 126 html files

#This generates 4(MAX_NUM ^ 2) + 5(MAX_NUM) + 1 html files, so good luck

#NOTE: MAX_NUM = 20 MAKES 1701 HTML FILES, SO BE CAREFUL WITH WHAT
#MAX_NUM IS AND WHERE YOU RUN THIS FILE FROM

MAX_NUM = 10

#generates main calculator.html site
def step_1():
    open('calculator.html', 'w').close()
    html = open('calculator.html', 'w')
    html.write('<html><body><a href="graph.html">Graph</a><br>')
    for i in range(MAX_NUM):
        html.write('<a href="{}.html">{}</a><br>'.format(str(i), str(i)))
        step_2(i)
    html.write('</body></html>')
    html.close()

#generates number.html sites, which let you choose a fxn
def step_2(n):
    open('{}.html'.format(str(n)), 'w').close()
    nhtml = open('{}.html'.format(str(n)), 'w')
    nhtml.write('<html><body><h1>{}</h1><br>'.format(str(n)))
    for fxn in ['plus', 'minus', 'times', 'divide']:
        step_3(n, fxn)
        nhtml.write('<a href="{}{}.html">{}</a><br>'.format(str(n), str(fxn), str(fxn)))
    nhtml.write('</body></html>')
    nhtml.close()

#generates numberFXN.html sites, which let you choose the 2nd value
def step_3(n, fxn):
    open('{}{}.html'.format(str(n), str(fxn)), 'w').close()
    nfhtml = open('{}{}.html'.format(str(n), str(fxn)), 'w')
    fxn_sign = ''
    if fxn == 'plus':
        fxn_sign = '+'
    elif fxn == 'minus':
        fxn_sign = '-'
    elif fxn == 'times':
        fxn_sign = '*'
    else:
        fxn_sign = '/'
    nfhtml.write('<html><body><h1>{} {}</h1><br>'.format(str(n), fxn_sign))
    for i in range(MAX_NUM):
        nfhtml.write('<a href="{}{}{}.html">{}</a><br>'.format(str(n), str(fxn), str(i), str(i)))
        step_4(n, fxn, i)
    nfhtml.write('</body></html>')
    nfhtml.close()

#generates numberFXNnumber.html files, which give the solution
def step_4(n, fxn, m):
    open('{}{}{}.html'.format(str(n), str(fxn), str(m)), 'w').close()
    nmhtml = open('{}{}{}.html'.format(str(n), str(fxn), str(m)), 'w')
    fxn_sign = ''
    if fxn == 'plus':
        fxn_sign = '+'
        nmhtml.write('<html><body><h1>{} {} {} = {}</h1>'.format(str(n), fxn_sign, str(m), str(n + m)))
    elif fxn == 'minus':
        fxn_sign = '-'
        nmhtml.write('<html><body><h1>{} {} {} = {}</h1>'.format(str(n), fxn_sign, str(m), str(n - m)))
    elif fxn == 'times':
        fxn_sign = '*'
        nmhtml.write('<html><body><h1>{} {} {} = {}</h1>'.format(str(n), fxn_sign, str(m), str(n * m)))
    else:
        fxn_sign = '/'
        if m == 0:
            nmhtml.write('<html><body><h1>{} {} {} = {}</h1>'.format(str(n), fxn_sign, str(m), str('undefined')))
        else:
            nmhtml.write('<html><body><h1>{} {} {} = {}</h1>'.format(str(n), fxn_sign, str(m), str('%.5f' % (n / m))))
    nmhtml.write('<br><a href="calculator.html">Back to calculator</a></body></html>')
    nmhtml.close()

# graphing
# x: [-10, 10]
# y: [-10, 10]

# g[x][y]

def graph():
    open("graph.html", 'w').close()
    html = open("graph.html", 'w')
    html.write('<html><body><h1>Linear fxn: y=mx+b</h1><br><h2>m = ?</h2>')
    for i in range(MAX_NUM):
        html.write('<a href="{}xplusb.html">{}</a><br>'.format(i, i))
        do_m(i)
    html.write('</body></html>')
    html.close()

# linear
def do_m(m):
    open('{}xplusb.html', 'w'.format(m)).close()
    html = open('{}xplusb.html'.format(m), 'w')
    html.write('<html><body><h1>Linear fxn: y={}x+b</h1><br><h2>b = ?</h2>'.format(m))
    for i in range(MAX_NUM):
        html.write('<a href="{}xplus{}.html">{}</a><br>'.format(m, i, i))
        do_b(m, i)
    html.write('</body></html>')
    html.close()

def do_b(m, b):
    open('{}xplus{}.html'.format(m, b), 'w').close()
    endlinear = open('{}xplus{}.html'.format(m, b), 'w')

    g = []
    xrange = 51
    yrange = 51
    xmid = int((xrange - 1) / 2)
    ymid = int((yrange - 1) / 2)

    dot_char = '.'
    if m == 0:
        dot_char = '&mdash;'
    if m == 1 or m == 2:
        dot_char = '/'
    if m == -1 or m == -2:
        dot_char = '\\'

    for x in range(xrange):
        to_add = []
        for y in range(yrange):
            if x == xmid and y == ymid:
                to_add += ['+']
            elif x == xmid:
                to_add += ['|']
            elif y == ymid:
                to_add += ['-']
            else:
                to_add += ['&nbsp;']
        g += [to_add]

    for x in range(xrange):
        y = m * (x - xmid) + b
        if y in range(-xmid, ymid + 1):
            g[x][y + ymid] = dot_char
            #print('(x, y) = ({}, {})'.format(x, y))

    html = '<html><head><style>@font-face {font-family: "square"; src: url("http://homer.stuy.edu/~jchirinos/square.ttf") format("truetype");} .square {font-family: "square", monospace;}</style></head><body><h1>y='+str(m)+'x+'+str(b)+'</h1><p class="square">'
    for y in range(yrange - 1, 0, -1):
        for x in range(xrange):
            html += str(g[x][y])
        html += '<br>\n'

    html += '</p><a href="calculator.html">Back to calculator</a></body></html>'

    endlinear.write(html)
    endlinear.close()


#I like writing go() at the end xD
def go():
    step_1()
    graph()

#go!
go()
