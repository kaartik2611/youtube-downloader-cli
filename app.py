import pafy
link = input("Enter Link of The YT Video: ")
try:
    data = pafy.new(link).streams[0].download()
    print("Your Video is downloaded 🎉")
except ValueError:
    print("PLease Enter an appropriate Link 🙂")
