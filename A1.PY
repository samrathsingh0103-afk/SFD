total_points = 0

laps = int(input("Enter the number of laps: "))

for lap in range(1, laps + 1):
    points = int(input("Enter points for lap " + str(lap) + ": "))
    total_points = total_points + points

    print("Lap", lap, "Points:", points)
    print("Running Total:", total_points)

print("\nFinal Total Points:", total_points)
