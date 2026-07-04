while True:
    userinput=input(">").lower();
    
    if(userinput == "start"):
        print("Car Started -- Ready to go");
    elif(userinput == "stop"):
        print("Stopped the Car");
    elif(userinput=="help"):
        print("start - to start the car\n" + "stop - to stop the car\n" +"quit - to exist");
    elif(userinput=="quit"):
        break;
    else:
        print("i dont understand the command");
