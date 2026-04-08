#Convert distant given in feet and inches into meter and centimeter.
feet = float(input("Enter feet: "))
inches = float(input("Enter inches: "))

total_meters = feet * 0.3048 + inches * 0.0254

meters = int(total_meters)               
centimeters = (total_meters - meters) * 100  

print("Distance in meters:", meters)
print("Distance in centimeters:", round(centimeters, 2))