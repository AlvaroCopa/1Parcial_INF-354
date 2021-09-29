from kanren import run, eq, conde, var, Relation, facts,lany
from kanren.constraints import neq 
x = var()

padre = Relation()
facts(padre,("teofilo","faustino"),
            ("teofilo","edgar"),
            ("teofilo","claudio"),
            ("teofilo","jovita"),
            ("teofilo","albertina"),
            ("ernesto","lizeth"),
            ("carmelo","margarita"),
            ("carmelo","ernesto"),
            ("carmelo","miguelina"),
            ("carmelo","cristina"),
            ("gustavo","diego"),
            ("faustino","angelica"),
            ("faustino","gustavo"),
            ("faustino","alvaro"),
            ("faustino","jhanet"),
            ("edgar","daniel"),
            ("edgar","kevin"),
            ("claudio","claudia"),
            ("claudio","alejandra"),
            ("claudio","fabricio"),
            ("gerardo","susan"),
            ("gerardo","paola"),
            ("gerardo","geovana"),
            ("pablo","juan pablo"),
            ("pablo","junior pablo"),
            ("pablo","roxana"),
            ("pablo","thelma"),
            ("pablo","dennis"),
            ("pablo","anelisse"),
            ("miguel","mario"))
madre = Relation()
facts(madre,("leandra","faustino"),
          ("leandra","edgar"),
          ("leandra","claudio"),
          ("leandra","jovita"),
          ("leandra","albertina"),
          ("zenobia","margarita"),
          ("zenobia","ernesto"),
          ("zenobia","cristina"),
          ("zenobia","miguelina"),
          ("margarita","angelica"),
          ("margarita","gustavo"),
          ("margarita","alvaro"),
          ("margarita","jhanet"),
          ("jovita","susan"),
          ("jovita","paola"),
          ("jovita","geovana"),
          ("albertina","juan pablo"),
          ("albertina","junior pablo"),
          ("albertina","roxana"),
          ("albertina","thelma"),
          ("albertina","dennis"),
          ("albertina","anelisse"),
          ("fabiola","daniel"),
          ("fabiola","kevin"),
          ("carmen","claudia"),
          ("carmen","alejandra"),
          ("carmen","fabricio"),
          ("lucy","diego"),
          ("miguelina","daniela"),
          ("miguelina","edwin"),
          ("cristina","danitza"),
          ("cristina","josue"),
          ("angelica","mario"))
def padres(x,y):
    return lany(padre(x,y),madre(x,y))

def hijos(x,y):
    return padres(y,x)

def hermanos(x,z):
    p = var()
    m = var()
    return conde((madre(m,x),padre(p,x),madre(m,z),padre(p,z),neq(x,z)))

def primos(x,y):
    p = var()
    m = var()
    return conde((lany(padre(p,x),madre(p,x)),lany(padre(m,y),madre(m,y)),hermanos(p,m)))

def tios(x,y):
    p = var()
    return conde((lany(madre(x,p),padre(x,p)),primos(p,y)))

def nietos(x,y):
    z=var()
    return conde((lany(madre(z,x),padre(z,x)),lany(madre(y,z),padre(y,z))))

def abuelos(x,z):
    return nietos(z,x)

print("Padres de margarita\n",run(30,x,padres(x,"margarita")))
print("Hijos de leandra\n ",run(30,x,hijos(x,"leandra")))
print("Hermanos de angelica\n",run(30,x,hermanos("angelica",x)))
print("Primos de alvaro\n",run(30,x,primos("alvaro",x)))
print("Tios de danitza\n",run(30,x,tios(x,"danitza")))
print("Abuelos de kevin\n",run(30,x,abuelos(x,"kevin")))
