import time
def converter(conv1,conv2,value1):
    #values
    content=["CE","FA","KE","RE","RA","UN"]

    #melting and boiling point
    point={
        "CE":[0,100],
        "FA":[32,212],
        "KE":[273,373],
        "RE":[0,80],
        "RA":[492,672],
    }

    #un on conv1 case
    if conv1.startswith("UN"):
        while True:
            try:
                print("Ok so faluty thermometer is the one who have the reading!")
                bp=int(input("Enter boiling point of the faulty scale: "))
                fp=int(input("Enter a freezing of the faulty scale point: "))
                break
            except:
                print("Number only!")
                continue
        point["UN"]=[fp,bp]

    #un on conv2 case
    if conv2.startswith("UN"):
        while True:
            try:
                print("Ok so faluty thermometer is the one who needs reading!")
                bp=int(input("Enter boiling point of the faulty scale: "))
                fp=int(input("Enter a freezing point of faulty scale: "))
                break
            except:
                print("Number only!")
                continue
        point["UN"]=[fp,bp]

    #finds ame and bme
    ame=float(0)
    bme=float(0)
    for i in range(len(content)):
        if conv1.startswith(content[i]):
            points=point[content[i]]
            ame=float((value1-points[0])/(points[1]-points[0])) #formula to find value of lhs which have value or whos value is given.
            #find bme
            for j in range(len(content)):
                if conv2.startswith(content[j]):
                    point2=point[content[j]]
                    bme=float((ame*(point2[1]-point2[0]))+point2[0]) #formula to find value of rhs aka the value we want bme is the reading of the value we are looking for.
    print(f"ame is: {ame}")
    print(f"The reading in {conv2.lower()} is {bme}")

#menu
options=[
    '1) Conversion of temperature from one reading to another',

]
for line in options:
    print(line)
    time.sleep(0.5)

#options
bruh=input("Please choose the corresponing number of your choise : ")
if bruh=="1" or bruh.startswith("Con"):
    options1 = [
        "Fahrenheit scale",
        "Celsius scale",
        "Kelvin scale",
        "Reaumer scale",
        "Rankine scale",
        "Unknown or malfunctuning scale",
    ]

    #conv1
    for line2 in options1:
        print(line2)
        time.sleep(0.2)
    conv1=input("Please choose what you want to convert (typing first two letter will work!): ")
    conv1=conv1.upper()
    
    #conv2
    for line3 in options1:
        print(line3)
        time.sleep(0.2)
    conv2=input(f"Please select what is you want to convert {conv1} in: ")
    conv2=conv2.upper()
    
    #
    while True:
        try:
            value1=int(input(f"Please enter reading in {conv1}: "))
            break
        except:
            print("Numbers only!")
            continue
    converter(conv1,conv2,value1)
    
