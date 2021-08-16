while True:
    print('do somthing. infinite loop.')
    break

i = 0
while i < 50:
    i += 1
    print('do somthing 50. without infinite loop.')
    break
i = 0
dots = ""
while i < 50:
    i += 1
    dots += "."
    print(dots)
else:
    print("job done.")


while True:
    user_response = input("cmd>/: ")

    if user_response.lower() == "exit":
        print("exit code 0")
        break
    else:
        print(f"user response is:{user_response}")