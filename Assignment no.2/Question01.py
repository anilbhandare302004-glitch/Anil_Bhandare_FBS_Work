#Convert the time entered in hh,min and sec into seconds.
hours = int (input("Enter a hours :"))
miniute = int(input("Enter a miniute:"))
seconds = int (input("Enter a seconds:"))

total_seconds = hours * 3600 + miniute * 60 + seconds
print("There are total time in seconds is :",total_seconds)