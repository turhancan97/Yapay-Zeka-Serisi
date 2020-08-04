# Hesap Makinesi
# class -> init -> method/attribute -> funct vs method

class Calculator: # Calculator adında class oluşturuyoruz.
    "Hesap Makinesi Projesi"
    
    def __init__(self, a, b): # Initialize metodunu ilk ve ikinci değeri oluşturmak için kullanıyoruz
        "initialize Değerleri"
        
        # attribute
        self.value1 = a # İlk değer
        self.value2 = b # ikinci değer
    
    def add(self): # Toplama metodumuzu oluşturuyoruz
        "Toplama v1+v2 = Sonuç -> return Sonuç"
        return self.value1 + self.value2 # Toplama sonucunu döndürüyoruz
    
    def subt(self): # Çıkarma metodumuzu oluşturuyoruz
        "Çıkarma v1-v2 = Sonuç -> return Sonuç"
        return self.value1 - self.value2 # Çıkarma sonucunu döndürüyoruz
         
    def multiply(self): # Çarpma metodumuzu oluşturuyoruz
        "Çarpma v1*v2 = Sonuç -> return Sonuç"
        return self.value1 * self.value2 # Çarpma sonucunu döndürüyoruz
    
    def division(self): # Bölme metodumuzu oluşturuyoruz
        "Bölme v1/v2 = Sonuç -> return Sonuç"
        return self.value1 / self.value2 # Bölme sonucunu döndürüyoruz
           
print("Toplama(1),Çıkarma(2), Çarpma(3), Bölme(4)") # Girmemiz gereken numaraları yazdırıyoruz
selection = input("1 - 2 - 3 - 4 \n") # 1, 2, 3, 4 değerlerini input olarak okuyoruz

v1 = int(input("Birinci Değer  = ")) # Birinci değeri input olarak okuyoruz
v2 = int(input("İkinci Değer = ")) # İkinci değeri input olarak okuyoruz

hesap_mak = Calculator(v1,v2) # Classımızı çağırıyoruz
if selection == "1":  # 1 ise Toplama
    add_result = hesap_mak.add()
    print("\nToplama Sonucu : {}".format(add_result))
elif selection == "2": # 2 ise çıkarma
    subtraction_result = hesap_mak.subt()
    print("\nÇıkarma Sonucu : {}".format(subtraction_result))
elif selection == "3": # 3 ise çarpma
    multiply_result = hesap_mak.multiply()
    print("\nÇarpma Sonucu : {}".format(multiply_result))
elif selection == "4": # 4 ise bölme
    div_result = hesap_mak.division()
    print("\nBölme Sonucu : {}".format(div_result))
else: # Girilen diğer değerler için hata mesajı yazdırma
    print("\nHata! uygun rakam giriniz")