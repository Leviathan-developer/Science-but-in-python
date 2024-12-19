import importlib

def quitter():
  res=input("Do you wish to continue Y/n: ")
  if res.lower()=="n":
    return True
  
def filecontent(path):
    with open(path,'r') as vectorfile:
        content=vectorfile.read()
        print(B+content)

def call(files,numericals):
  while True:
    re=input("Do you want help with numerical or note? ")
    re=re.upper()
    if re.startswith("NU"):
        try:
            module=importlib.import_module("contents.numerical."+numericals)
            module.main()
        except Exception as e:
            print(f"Error: {e}")
        break
    elif re.startswith("NO"):
        filecontent("contents/Notes/"+files+".txt")
        break
    else:
      print("No such options!!!")
      continue
def filecontent(path):
    with open(path,'r') as file:
        content=file.read()
        print(content)