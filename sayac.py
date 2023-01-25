sesli_h="aeioüöuı"
sayac=0

kelime=input("kelime girin: ")

for harf in kelime:
    if harf in sesli_h:
        sayac+=1

sonuc=print(f"{kelime} kelimesinde {sayac} tane sesli harf var.") 

mesaj="{} kelimesinde {} tane sesli harf var."
print(mesaj.format(kelime,sayac))