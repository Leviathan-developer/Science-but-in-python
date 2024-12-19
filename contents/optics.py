from colorama import Fore
import contents.common as common
G=Fore.GREEN
B=Fore.BLUE
R=Fore.RED

def quitter():
  res=input("Do you wish to continue Y/n: ")
  if res.lower()=="n":
    return True
  
def filecontent(path):
    with open(path,'r') as vectorfile:
        content=vectorfile.read()
        print(B+content)


def wave():
  print("1) Reflection at curved mirror")
  print("2) Refraction at plane surfaces")
  print("3) Refraction through prisms")
  print("4) Lenes")
  print("5) Dispersion")
  while True:
      try: 
          mechno=int(input("Please choose a number of a chapters to go further deep!: "))
          if mechno==1:
              common.call('wavenoptics/reflaction','reflaction')
          if mechno==2:
              common.call('wavenoptics/refraction','refraction')
          if mechno==3:
              common.call('wavenoptics/prism','prism')
          if mechno==4:
              common.call('wavenoptics/lenses','lenses')
          if mechno==4:
              common.call('wavenoptics/dispersion','dispersion')
      except BaseException:
          print("Not an number")
      except:
            print("Out of option or option not open yet!")
      if common.quitter==True:
              break