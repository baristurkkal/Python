
import re
emails = []
if __name__ == '__main__':
    while(True) :
        email = input()
        if email == "":
            break
        emails.append(email)
print(emails, sep="\n")

def fun(s):
    # return True if s is a valid email, else return False
    # allowed1 = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-")
    # allowed2 = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    # allowed3 = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    # is_valid = all(c in allowed1 for c in str)
    valid_format = "@" in s and "." in s
    if valid_format :
        username = s.split("@")[0]
        dm = s.split("@")[1]
        domain = dm.split(".")[0]
        ext = dm.split(".")[1]
        print(username,domain,ext, sep=" ")
    else :
        print("Invalid format: ",s)

fun(emails[0])    
    
# allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-")

# is_valid = all(c in allowed for c in str)