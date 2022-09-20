from instagram_private_api import Client
import time


print("******************************************")
print("All copyrights belong to @ts._.taha in IG")
print("******************************************")
print()
print("Script [ON]")
user_name = input('Input your instagram username here: ')
print("Dont worry , this script store 0% of your data..")
print("The full source code is available in Github..")
password = input('Input your instagram password here: ')
tar_usr1 = "lamborghini"
tar_usr2 = "maccosmetics"
tar_usr3 = "lunamaya"
tar_usr4 = "mercedesbenz"
tar_usr5 = "floydmayweather"
tar_usr6 = "kevinho"
tar_usr7 = "433"
tar_usr8 = "gisel_la"
tar_usr9 = "bmw"
tar_usr10 = "nusr_et"
tar_usr11 = "ciara"
tar_usr12 = "adidas"
tar_usr13 = "lunasantana"
tar_usr14 = "psg"
tar_usr15 = "voguemagazine"
tar_usr16 = "50cent"
tar_usr17 = "dishapatani"
tar_usr18 = "marvelstudios"
tar_usr19 = "amandacerny"
tar_usr20 = "maisa"
tar_usr21 = "victoriabeckham"
tar_usr22 = "dior"
tar_usr23 = "wizkhalifa"
tar_usr24 = "colesprouse"
tar_usr25 = "karimbenzema"
tar_usr26 = "cristiano"
tar_usr27 = "mosalah"
tar_usr28 = "billieeilish"
tar_usr29 = "jbalvin"


private_api = Client(user_name, password)
print("Connected succesfully..")
time.sleep(3)
def auto_follow(tar_usr1=tar_usr1):
    info = private_api.username_info(tar_usr1)
    private_key = info['user']['pk']
    private_api.friendships_create(private_key)
def auto_unfollow(tar_usr1 = tar_usr1):
    infoo = private_api.username_info(tar_usr1)
    private_keyy = infoo['user']['pk']
    private_api.friendships_destroy(private_keyy)
def s():
    time.sleep(2)
def gain_follow():
    auto_follow()
    s()
    auto_follow(tar_usr2)
    s()
    auto_follow(tar_usr3)
    s()
    auto_follow(tar_usr4)
    s()
    auto_follow(tar_usr5)
    s()
    auto_follow(tar_usr6)
    s()
    auto_follow(tar_usr7)
    s()
    auto_follow(tar_usr8)
    s()
    auto_follow(tar_usr9)
    s()
    auto_follow(tar_usr10)
    s()
    auto_follow(tar_usr11)
    s()
    auto_follow(tar_usr12)
    s()
    auto_follow(tar_usr13)
    s()
    auto_follow(tar_usr14)
    s()
    auto_follow(tar_usr15)
    s()
    auto_follow(tar_usr16)
    s()
    auto_follow(tar_usr17)
    s()
    auto_follow(tar_usr18)
    s()
    auto_follow(tar_usr19)
    s()
    auto_follow(tar_usr20)
    s()
    auto_follow(tar_usr21)
    s()
    auto_follow(tar_usr22)
    s()
    auto_follow(tar_usr23)
    s()
    auto_follow(tar_usr24)
    s()
    auto_follow(tar_usr25)
    s()
    auto_follow(tar_usr26)
    s()
    auto_follow(tar_usr27)
    s()
    auto_follow(tar_usr28)
    s()
    auto_follow(tar_usr29)

def gain_unfollow():
    auto_unfollow()
    s()
    auto_unfollow(tar_usr2)
    s()
    auto_unfollow(tar_usr3)
    s()
    auto_unfollow(tar_usr4)
    s()
    auto_unfollow(tar_usr5)
    s()
    auto_unfollow(tar_usr6)
    s()
    auto_unfollow(tar_usr7)
    s()
    auto_unfollow(tar_usr8)
    s()
    auto_unfollow(tar_usr9)
    s()
    auto_unfollow(tar_usr10)
    s()
    auto_unfollow(tar_usr11)
    s()
    auto_unfollow(tar_usr12)
    s()
    auto_unfollow(tar_usr13)
    s()
    auto_unfollow(tar_usr14)
    s()
    auto_unfollow(tar_usr15)
    s()
    auto_unfollow(tar_usr16)
    s()
    auto_unfollow(tar_usr17)
    s()
    auto_unfollow(tar_usr18)
    s()
    auto_unfollow(tar_usr19)
    s()
    auto_unfollow(tar_usr20)
    s()
    auto_unfollow(tar_usr21)
    s()
    auto_unfollow(tar_usr22)
    s()
    auto_unfollow(tar_usr23)
    s()
    auto_unfollow(tar_usr24)
    s()
    auto_unfollow(tar_usr25)
    s()
    auto_unfollow(tar_usr26)
    s()
    auto_unfollow(tar_usr27)
    s()
    auto_unfollow(tar_usr28)
    s()
    auto_unfollow(tar_usr29)
print("Starting Follow gain.. ETA : 1min")
gain_follow()
print("Follow gain : done..")
print("Cooldown of 1 min is starting..")
time.sleep(60)
print("Cooldown is finished, Starting Unfollow gain.. ETA 1min")
gain_unfollow()
print("Unfollow gain : done..")
print("Cooldown of 4min is starting..")
time.sleep(240)
print('Cooldown is finished , Starting the last Follow gain..ETA 1min')
gain_follow()
print("Last Follow gain : done..")
print("Cooldown of 1min is starting..")
time.sleep(60)
print("Cooldown is finished , Starting the last Unfollow gain..ETA 1min")
gain_unfollow()
print("Last Unfollow gain : done..")
print("Logging out..")
time.sleep(3)
private_api.logout()
print("Logged out!")
# ETA till finish is 10Min'ish
print("Script [OFF]")
print()
print("******************************************")
print("All copyrights belong to @ts._.taha in IG")
print("******************************************")
print()





