
number = int(
    input("Lütfen faktöriyelini bulmak istediğiniz sayıyı giriniz...\n"))
factorial = 1

if number >= 0:
    for i in range(1, number+1):  # range varsayılan olarak 0'dan başlar ve son değeri kapsamaz
        factorial = factorial*i
    print("Girdiğiniz sayının faktöriyeli:", factorial)
else:
    print("Negatif sayıların faktöriyeli olmaz!")
