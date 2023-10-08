def vigenere(x,key):
    liste = []
    code = list(x)
    j = 0
	
    for i,char in enumerate(code):
        if char.isalpha():
            code[i] = key[(i+j)%len(key)]
            if encrypt:
                liste.append((ord(x[i]) + ord(code[i]) - 65 * 2) % 26)
            else:
                liste.append((ord(x[i]) - ord(code[i])) % 26)
        else:
            liste.append(ord(char))
            j -=1

    for i,char in enumerate(code):
        if char.isalpha():
            liste[i] = chr(liste[i] + 65)
        else:
            liste[i] = chr(liste[i])
			
    return ''.join(liste)

print("Vigenere Şifre Çözücüye Hoşgeldiniz Eğer Verilen Sayfadaki Şifreyi Çözmek İsterseniz Anahtar Kelime Kısmına -pines- Giriniz")

if True:
    x = input('Lütfen Mesajınızı Giriniz : ').upper()
    encrypt = False
    if input('Anahtar kelimeniz var mı? (y/n) : ') == "y":
        key = input('Lütfen anahtarı giriniz :').upper()
        print(vigenere(x,key))
    
       