picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for row in picture:
    computer_picture = ""
    for column in row:
        if column == 1:
           computer_picture += "🚬"
           continue
        computer_picture += " "

    print(computer_picture)

for row in picture:
    computer_picture = ""
    for column in row:
        if column == 1:
            print("🎧", end="")
            continue
        print(" ", end="")

    print(computer_picture)


print(0,0,0,1,0,0,0)
print(0,0,1,1,1,0,0)
print(0,1,1,1,1,1,0)
print(1,1,1,1,1,1,1)