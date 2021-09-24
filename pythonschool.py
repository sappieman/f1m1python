while True:

    import datetime

x = datetime.datetime.now()

print(x)

print("Hello you!, ik ben python \n")
c = input("Wie ben jij?\n")
print(f"Hello {c}\n")

while True:
    if (input("do you want to repeat") == 'y'):
     continue
    else:
        break