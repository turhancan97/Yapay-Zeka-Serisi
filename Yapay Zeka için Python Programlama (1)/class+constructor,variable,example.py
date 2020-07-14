class Calisan:
    
    zam_orani = 1.8
    counter = 0
    def __init__(self,isim,soyisim,maas): # constructor
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim+soyisim+"@asd.com"
        
        Calisan.counter = Calisan.counter + 1
    
    def giveNameSurname(self):
        return self.isim +" " +self.soyisim
        
    def zam_yap(self):
        self.maas = self.maas + self.maas*self.zam_orani
        
#isci1 = Calisan("ali", "veli",100) 
#print(isci1.maas)
#print(isci1.giveNameSurname())

# class variable
calisan1 = Calisan("ali", "veli",100) 
print("ilk maas: ",calisan1.maas)
calisan1.zam_yap()
print("yeni maas: ",calisan1.maas)

calisan2 = Calisan("ayse", "hatice",200) 
calisan3 = Calisan("ayse", "yelda",600) 
calisan4 = Calisan("eren", "hilal",500) 

#  class example
liste  = [calisan1,calisan2,calisan3,calisan4]

maxi_maas = -1
index = -1
for each in liste:
    if(each.maas>maxi_maas):
        maxi_maas = each.maas
        index = each
        
print(maxi_maas)
print(index.giveNameSurname()

# %%
class A:
    global a
    a = 5
    def __init__(self,x = 4):
        self.x = x
    def sum(self):
        return a + self.x

x = A(5)
x.sum()

# %%
class DataiTeam:
    def __init__(self, x = "hi"):
        self.x = x
    def show(self):
        print(self.x)

my_class = DataiTeam()
my_class.show()