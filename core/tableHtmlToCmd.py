
"""
Usa o cabeçalho th para definir a quantidade de colunas.
"""

def get_head(html):
    c = html
    o = []
    aux = 0
    s = '</th>'
    x3 = c.find(s)
    aux = x3 + len(s)
    s = '>'
    x4 = c[aux:].find(s)
    col = aux + x4
    aux += x4 + len(s)
    while x3 != -1:
        s = '</th>'
        x5 = c[aux:].find(s)
        end = aux + x5
        aux += x5 + len(s)
        o += [c[col:end]]
        s = '>'
        x3 = c[aux:].find(s)
        aux += x3 + len(s)
        col = aux + x3
    return o
    
def f(file):
    with open(file) as f:
        c = f.read()
    c = ''.join(c.split('\n'))
    t = []
    #x1 = c.find('<table')
    #x2 = c.find('<thead><tr><th')
    s = '</th>'
    x3 = c.find(s)
    if x3 == -1:
        print('A tabelra precisa ter o cabeçalho com th.')
        exit()
    #t += [get_head(c
    t.append([])
    s = '</th>'
    x3 = c.find(s)
    aux = x3 + len(s)
    s = '>'
    x4 = c[aux:].find(s)
    col = aux + x4
    aux += x4 + len(s)
    s = '</th>'
    x5 = c[aux:].find(s)
    end = aux + x5
    aux += x5 + len(s)
    t[0] += [c[col:end]]
    
    for _ in range(4):
        s = '>'
        x4 = c[aux:].find(s)
        col = aux + x4
        aux += x4 + len(s)
        s = '</th>'
        x5 = c[aux:].find(s)
        end = aux + x5
        aux += x5 + len(s)
        t[0] += [c[col:end]]

    
    for j in range(len(t)):
        for i in range(len(t[0])):
            print('|', t[j][i], '|', end='')
        print('\n')
            

if __name__ == '__main__':
    import sys
    f(sys.argv[1])