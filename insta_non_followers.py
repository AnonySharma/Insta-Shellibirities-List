import instaloader as il
import os
id=il.Instaloader()

if os.path.exists("followers.txt"): 
    os.remove("followers.txt")

if os.path.exists("following.txt"): 
    os.remove("following.txt")

if os.path.exists("wannabe_shellibirities.txt"): 
    os.remove("wannabe_shellibirities.txt")

username = "_ankitt._.sharma_"
password = "maiNahiBataungaaaa" #In Johny Lever's voice
id.login(username,password)
profile=il.Profile.from_username(id.context,username)

followers=[]
file = open("followers.txt",'w')
for f in profile.get_followers():
    followers.append(f.username)

for u in sorted(followers):
    file.write(u+'\n')

file.close()
following=[]
file = open("following.txt",'w')
for f in profile.get_followees():
    following.append(f.username)

for u in sorted(following):
    file.write(u+'\n')

file.close()
lst=set(following)-set(followers)
file = open("wannabe_shellibirities.txt", "w")
for u in lst:
    print(u)
    file.write(u+'\n')

file.close()
print("------------------------------")
b = input("Do you want to delete the temporary files created(Y/N)?")
if b=='Y' or b=='y':
    os.remove("followers.txt")
    os.remove("following.txt")
    os.remove("wannabe_shellibirities.txt")
