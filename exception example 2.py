while True:
    try:
        answer = float(input("How many hours did you work? "))
        payrate = float(input("What is your payrate?"))
        print("Your total pay is:",answer*payrate)
        break

    except ValueError as err:
        #pass
        print("there was an error:",err)
