picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

def get_emoji(emoji_name):
    emoji_dict = {
        "cigrate": "🚬",
        "headphones": "🎧"
    }
    return emoji_dict.get(emoji_name)

def print_image(picture, emoji_value):
    for row in picture:
        computer_picture = ""
        for column in row:
            if column == 1:
                computer_picture += emoji_value
                continue
            computer_picture += " "
        print(computer_picture)

def run(picture, emoji_name):
    emoji_value = get_emoji(emoji_name)
    print_image(picture, emoji_value)

run(picture, "cigrate")
run(picture, "headphones")

print(0,0,0,1,0,0,0)
print(0,0,1,1,1,0,0)
print(0,1,1,1,1,1,0)
print(1,1,1,1,1,1,1)