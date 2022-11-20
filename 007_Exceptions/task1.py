while True:
    try:
     time=input("Time: ")
     stime=[int(i)for i in time.split(":")]
    except(ValueError):
        print("Wrong")
    else:
        break
if stime[0]>18 and stime[0]<=24 or stime[0]>=0 and stime[0]<6:
    raise TypeError("I dont see sun")
else:
    print(((stime[0]-6)*1518)+stime[1]*0.25)