import random
import colorama as clr
clr.init(autoreset=True)
y=clr.Fore.YELLOW
g=clr.Fore.GREEN
b=clr.Fore.BLUE
def main():
    while True:
        mode=input("Enter exam mode or upload question or exit: ")
        if mode.lower()=='exit':
            break
        else:
            mode=mode.upper()
            if mode.startswith("U"):
                while True:
                    question=input(g+"Please enter a question directly or exit: ")
                    if question.lower()=="exit":
                        break
                    else:
                        answer=input(g+"Please enter a answer: ")
                        with open("contents/question.txt","a") as que:
                            que.write(question+"\n")
                        with open("contents/answer.txt","a") as ans:
                            ans.write(answer+"\n")

            elif mode.startswith("E"):
                with open("contents/question.txt","r") as f:
                    questionline=f.readlines()
                with open("contents/answer.txt",'r') as an:
                    answerline=an.readlines()
                while True:
                    fate=random.randint(0,len(questionline)-1)
                    print(b+questionline[fate])
                    while True:
                        choice=input(g+"Please enter y to reveal answer or s to skip or exit:  ")
                        choice=choice.lower()
                        if choice in ["y","s","exit"]:
                            break
                        else:
                            print("Please type y or s or exit only!")
                            continue
                    if choice=="y":
                        print(y+answerline[fate])
                    elif choice=="s":
                        continue
                    elif choice=="exit":
                        break
                    yno=input(g+"Do you want to continue? Y/n: ")
                    if yno.lower().startswith("n"):
                        break
                        