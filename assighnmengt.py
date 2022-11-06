import random
import time
words=['almond', 'banana', 'blewits', 'brazil', 'carrot', 'casaba', 'cashew', 'celery', 'cherry', 
'chives', 'chocho', 'citron', 'citrus', 'cobnut', 'cooker', 'daikon', 'damson', 'endive', 'fennel',
 'garlic', 'girkin', 'greens', 'kiwano', 'lentil', 'lichee', 'lychee', 'marrow', 'medlar', 'nettle', 
 'orange', 'oyster', 'papaya', 'pawpaw', 'peanut', 'pepper', 'pignut', 'pippin', 'potato', 
'quince', 'radish', 'raisin', 'rocket', 'russet', 'squash', 'tomato', 'turnip', 'wakame', 'walnut']
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')
name = input("enter your name: ")
print("Hello " + name + "! Best of luck!\n")
time.sleep(1)
print("The game is about to start!\n Let's play Hangman! \n")
time.sleep(1)
n=int(input("1.Play \n2.Quit game\n Enter your choice : "))
if n==1:
    word=random.choice(words)
    leng = len(word)
    chance=-1
    ans=["_ "]*leng
    print(ans)
    for c in range(0,100):
        flag=True
        print("Clue: Word contains "+str(leng)+" Word ")
        g=input("Enter a Character: ")
        for i in range(0,leng):
            if g==word[i]:
                ans[i]=g
                flag=False;
                print("\n"+str(ans))               
        if flag:
            chance+=1
            if chance==0:
                print("   _____ \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n");print("!!!!!! You have "+str(4-chance)+" chance left !!!!!!\n\n")
            elif chance==1:
                 print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n");print("!!!!!! You have "+str(4-chance)+" chance left !!!!!!\n\n")
            elif chance==2:
                 print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n");print("!!!!!! You have "+str(4-chance)+" chance left !!!!!!\n\n")
            elif chance==3:
                print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n");print("!!!!!! You have "+str(4-chance)+" chance left !!!!!!\n\n")
            elif chance==4:
                print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
                print('''
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.---.
| |/         ||     |
| |          ||     |
| |          ( \___/
| |         .-----.
| |        /Y     Y|
| |       // |   |||
| |      //  |   |||  
| |     ()   |   |()
| |          || ||
| |          || ||
| |          || ||
| |          || ||
| |          || ||
| |          `-'`-' 
| |
''')
                print("Answer was : "+str(word))
                print("\n\n~~~~~~~~~~~ game Over ~~~~~~~~~~~")
                break
        if list(word)==ans :
                    print("~~~~~ Wohooooooo U Won ~~~~~")
                    break     
            
else:
    exit
