import hashlib

flag = 0
counter = 0

pass_hash = input("enter MD5 hash: ")
wordlist = input("Wordlist file name: ")

try:
    pass_file = open(wordlist, "r", errors="ignore")

except:
    print(("no file found!"))
    quit()

for word in pass_file:
    encoded_word = word.encode('utf-8')
    digest = hashlib.md5(encoded_word.strip()).hexdigest()
    
    counter +=1
    
    if digest == pass_hash:
        print("password has been found!")
        print("the number of tries were: ", counter)
        print("password is: " + word)
        flag = 1
        break
    
if flag == 0:
    print("password is not in the wordlist.")
