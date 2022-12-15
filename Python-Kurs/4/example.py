user_name = "ozgur"
parola = "1234"


while True:
    user_name_i = input("Kullanıcı Adınız: ")

    if user_name_i == user_name:

        parola_i = input("Parolanız: ")
        if parola_i == parola:
            print("Welcome")

        else:
            print("Parola hatalı")
    else:
        print("Kullanıcı adı hatalı")
    if user_name_i == user_name and parola_i == parola:
        break
    print("Tekrae deneyin")
