print("Welcome User!")
print("\n"*3)
print("*"*30)
phone = input("Enter a phone number with 3 or 4 letter words. Split each word with a dash: ").lower()
print("*"*30)
final_phone = ""
lettersDict = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"cat":228,"dog":364,"car":227,"door":3667,"rat":728,"run":786,"gold":4653,"ball":2255,"bank":2265,"hand":4263,"home":4663,"call":2255,"cook":2665,"care":2273,"cold":2653,"hot":468,"bag":224,"fun":386,"eat":328,"art":278,"air":247,"-":"-"," ":" "}

phone_split = phone.split("-")
print(phone_split)

for i in phone_split:
  if i[0] == ("0" or "1" or "2" or "3" or "4" or "5" or "9"):
    for j in i:
      final_phone += str(lettersDict[j])
  else:
    print("This digit is ", i)
    final_phone += str(lettersDict[i])
  final_phone += "-"

print("*"*30)
print(phone)
print(final_phone)
