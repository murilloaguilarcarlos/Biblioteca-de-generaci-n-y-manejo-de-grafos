"Carlos Murillo Aguilar"
import random
import math
"Clases y funciones"
class Nodo:
    def __init__(self, i):
        self.idn=i              # Crear objeto nodo, conformado solo por
                                #  su identificador numérico
class Arista:
    def __init__(self, a, b):
        self.arista=[Nodo(a),Nodo(b)]# Crear objeto arista, conformado por una 
                                     #  lista de dos nodos
class Grafo:
    def __init__(self):            # Crear objeto grafo, conformado por una 
        self.nodos=[]              #  lista de los identificadores de cada nodo
        self.aristas=[]            #  y una lista de parejas de identificadores
                                   #  de cada nodo en cada arista
    def agregarNodo(self, n):
        if n not in self.nodos:
            nodo=Nodo(n)
            self.nodos.append(nodo.idn)
            
    def agregarArista(self, e1, e2):
        if e1 in self.nodos and e2 in self.nodos:
            aristaIds=Arista(e1, e2)
            self.aristas.append([aristaIds.arista[0].idn,  aristaIds.arista[1].idn])
            self.aristas.append([aristaIds.arista[1].idn,  aristaIds.arista[0].idn])
    
    def generar_archivo(self, tipo_de_grafo):         #Se define el nombre del archivo
        if tipo_de_grafo==1:
            s=open("Grafo de Malla.gv","w")
        elif tipo_de_grafo==2:
            s=open("Grafo de Erdös y Rényi.gv","w")
        elif tipo_de_grafo==3:
            s=open("Grafo de Gilbert.gv","w")
        elif tipo_de_grafo==4:
            s=open("Grafo Geográfico Simple.gv","w")
        elif tipo_de_grafo==5:
            s=open("Grafo Barabási-Albert.gv","w")
        elif tipo_de_grafo==6:
            s=open("Grafo Dorogovtsev-Mendes.gv","w")
        
        s.write("digraph sample {\n")
        for p in range(len(self.aristas)):
            e1=str(self.aristas[p][0])
            e2=str(self.aristas[p][1])
            flecha=" -> "
            puntocoma=";\n"
            w=e1+flecha+e2+puntocoma
            # print(w)
            s.write(w)
            
        for i in range(len(self.nodos)):
            b=False
            while b==False:
                for j in range(len(self.aristas)):
                    if self.nodos[i] in self.aristas[j]:
                        b=True
                if b==False:
                    # print(g.nodos[i])
                    ns=str(self.nodos[i])
                    w2=str(ns + puntocoma)
                    s.write(w2)
                b=True 
        s.write("}")
        s.close()

"Grafo de Malla"
def malla(i, j, dirigido=False): # i columnas, j filas
    tipo_de_grafo=1
    g=Grafo() 
    n=1
    m=[]
    for vi in range (i):
        r=[]
        for vj in range (j):
            r.append(n)
            g.agregarNodo(n)
            n+=1
        m.append(r)
    print(m)
    
    for vi in range (i):
        for vj in range (j):            
            nij=m[vi][vj]            
            if vi<(i-1):
                g.agregarArista(nij, m[vi+1][vj])
            if vj<(j-1):
                g.agregarArista(nij, m[vi][vj+1])
    g.generar_archivo(tipo_de_grafo)

"Grafo de Erdös y Rényi"
def eyR(n,a,dirigido=False): #n nodos, a aristas
    tipo_de_grafo=2
    g=Grafo()
    r=[]
    aristas=[]
    for i in range (n):
        g.agregarNodo(i+1)
        r.append(i+1)    
    
    for i in range (a+1):
        # print (r)
        n1=random.choice(r)        
        n2=random.choice(r)
        if [n1, n2] not in aristas and [n2, n1] not in aristas and n1!=n2:
            g.agregarArista(n1, n2)
            aristas.append([n1, n2])
        else:
            i=i-1
    print(aristas)
    g.generar_archivo(tipo_de_grafo)
    
"Grafo de Gilbert"
def gilbert(n, p, dirigido=False):
    tipo_de_grafo=3
    g=Grafo()
    r=[]
    aristas=[]
    for i in range (n):
        g.agregarNodo(i+1)
        r.append(i+1)    
    
    for i in r:
        for j in r:
            prob=random.random()
            if prob<=(p/200) and [i, j] not in aristas \
                             and [j, i] not in aristas and i!=j:
                g.agregarArista(i, j)
                aristas.append([i, j])
    print(aristas)
    g.generar_archivo(tipo_de_grafo)
    
"Grafo Geográfico Simple"
def simple(n, r, dirigido=False):
    tipo_de_grafo=4
    g=Grafo()
    nodos=[]
    coords=[]
    aristas=[]
    box=n*4
    for i in range (n):
        g.agregarNodo(i+1)
        nodos.append(i+1)
        x=random.randrange(-box,box)
        y=random.randrange(-box,box)
        coords.append([x, y])
    print(coords)
    for i in (nodos):
        for j in (nodos):            
            pd=math.sqrt((coords[j-1][0]-coords[i-1][0])**2+(coords[j-1][1]-coords[i-1][1])**2)
            if pd<=r and [i, j] not in aristas and [j, i] not in aristas and i!=j:
                g.agregarArista(i, j)
                aristas.append([i, j])
    # print(aristas)
    g.generar_archivo(tipo_de_grafo)
    
"Grafo Barabási-Albert"
def byA(n, a, dirigido=False):
    tipo_de_grafo=5
    g=Grafo()
    nod_vert=[]
    nodos=[]
    aristas=[]
    phi=(1+math.sqrt(5))/2
    for i in range (n):
        g.agregarNodo(i+1)
        nodos.append(i+1)
        nod_vert.append(0)
        for j in range (len(nodos)):
            prob=random.random()
            if prob<=(1/(phi**(0.5*nod_vert[j]))) and nod_vert[j]<=a \
                                            and nod_vert[i]<=a \
                                            and [i, j] not in aristas \
                                            and [j, i] not in aristas and i!=j:
                g.agregarArista(i, j)
                aristas.append([i, j])
                nod_vert[j]+=1
                nod_vert[i]+=1
    print(nod_vert)
    g.generar_archivo(tipo_de_grafo)
    
"Grafo Dorogovtsev-Mendes"
def dyM(n, dirigido=False):
    tipo_de_grafo=6
    g=Grafo()
    nodos=[1, 2, 3]
    for i in range(len(nodos)):
        g.agregarNodo(i+1)
    aristas=[[1,2], [2,3], [1,3]]
    for i in range(len(aristas)):
        g.agregarArista(aristas[i][0], aristas[i][1])    
    for i in range(4, n+1):        
        g.agregarNodo(i)
        nodos.append(i)
        a=random.choice(aristas)
        if [a[0], i] not in aristas and [i ,a[0]] not in aristas and \
           [a[1], i] not in aristas and [i ,a[1]] not in aristas and \
           i!=a[0] and i!=a[1]:
            g.agregarArista(a[0], i)
            g.agregarArista(a[1], i)
            aristas.append([a[0], i])
            aristas.append([a[1], i])
        
    g.generar_archivo(tipo_de_grafo)

# malla(20,25) # (5,6):30, (10,10):100, (20,25):500  columnas, filas
# eyR(500,499) # nodos, aristas
# gilbert(500,15) # nodos, porcentaje de probabilidad
# simple(100,100) # nodos, radio
# byA(500,5) #nodos, aristas máximas por nodo
# dyM(500) #nodos