import string
import random
def generate_password(length,use_digits=True,use_special=True):
    characters=string.ascii_letters
    if use_digits:
        characters +=string.digits
    if use_special:
        characters += string.punctuation
    if not characters:
        print("INVALID CHARACTERS!!!!")
        return ""
    password=''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("PASSWORD GENERATOR")
    try:
        length=int(input("Enter the length of password=>"))
        if length<=0:
            print("PLEASE ENTER A POSITIVE LENGTH FOR PASSWORD")
            return 
    except ValueError:
        print("PLEASE BE VALID!!!")
        return
    use_digits=input("YOU WANT TO USE digits (y/n)=>").strip().lower() == 'y'
    use_special=input("YOU WANT TO USE SPECIAL CHARACTERS (y/n)=>").strip().lower() == 'y'
    password=generate_password(length,use_digits,use_special)
    print("GENRATED PASSWORD IS=>",password)
    print("DO YOU WANT TO SAVE PASSWORD TO FILE???")
    FILE="password_save.txt"
    save_file=input("DO YOU WANT TO SAVE PASSWORD (y/n)=>").strip().lower()
    if save_file== 'y':
        with open(FILE,"w") as f:
           f.write(password)
           print("PASSWORD SAVED TO YOUR FILE(y/n)")
        
if __name__ == "__main__":
    main()




    