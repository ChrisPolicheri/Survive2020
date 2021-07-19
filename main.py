print('''
   .--""--.___.._
 (  <__>  )      `-.
 |`--..--'|'SOLD   |  
 |       :| OUT'  /
 |       :|--""-./
 `.__  __;' 
     ""     
''')

print("WELCOME TO 2020")
print("Your mission is to survive!")

choice1 = input(
    'Take that trip, you might live. Type "trip".   Safely stay stuck at home. Type "home"\n'
).lower()
if choice1 == "home":
    choice2 = input('''
           )
       (  (              .^.
        \) )           .'.^.'.
         (/          .'.'---'.'.
        _\)_       .'.'-------'.'.
       (__)()    .'.'-,=======.-'.'.
       (_)__)  .'.'---|   |   |---'.'.
       (__)_),'.'-----|   |   |-----'.'.
       ()__.'.'-------|___|___|-------'.'.
       (_.'.'---------------------------'.'.
       .'.'-------------------------------'.'.
      """""|====..====.=======.====..====|"""""
       ()_)|    ||    |.-----.|    ||    |
       (_)_|    ||    ||     ||    ||    |
       (...|____||____||_____||____||____|
      (_)_(|----------| _____o|----------|
      (_)(_|----------||     ||----------|
      (__)(|----------||_____||----------|
      (_)(_|---------|"""""""""|---------|
      ()()(|--------|"""""""""""|--------|
You\'re sitting at home. Type "blm" to get out in the crowds, support the movement! or Type "crafty" to stay at home.\n'''
                    ).lower()
    if choice2 == "crafty":
        choice3 = input(
            'Your craftiness consists of "painting", "sewing", or "knife throwing". Choose one.\n'
        ).lower()
        if choice3 == "painting":
            print(
                "You end up painting street sign designs on live animals for TikTok and get quite a following. You're Rich, you Win! Game Over"
            )
        elif choice3 == "sewing":
            print(
                "You sew facemasks at a record rate saving millions. You're a Hero, you Win! Game Over"
            )
        elif choice3 == "knife throwing":
            print(
                "Your awesome knife throwing skills make the Murder Hornets so jealous they end up just leaving Earth. You're a Hero, you Win! Game Over"
            )
        else:
            print(
                "That wasn't even an option! You get Covid and die! Game Over")
    else:
        print('''
                          ________________
                          \      __      /         __
                           \_____()_____/         /  )
                           '============`        /  /
                            #---\  /---#        /  /
                           (# @\| |/@  #)      /  /
                            \   (_)   /       /  /
                            |\ '---` /|      /  /
                    _______/  \_____// \____/ o_|
                   /       \  /     \  /   / o_|
                  / |           o|        / o_| 
                 /  |  _____     |       / /   \ \
                
You proudly protest with thousands and support the BLM movement but you were careful and masked up so you were fine... But then you decide to travel for Thanksgiving catch Covid and die. Game Over
''')
else:
    print('''
            mm###########mmm
        m####################m
      m#####`"#m m###"""'######m
     ######*"  "   "   "mm#######
   m####"  ,             m"#######m
  m#### m*" ,'  ;     ,   "########m
  ####### m*   m  |#m  ;  m ########
 |######### mm#  |####  #m##########|
  ###########|  |######m############
  "##########|  |##################"
   "#########  |## /##############"
     ########|  # |/ m###########
      "#######      ###########"
        You take that trip go to a giant beach party catch Covid and die! Game Over'''
          )
