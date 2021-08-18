# Keyword arguments
def log(log, name):
    print(f"{name} is printting {log}")

log(name="Bar", log="Hello")

def log2(log="Bye", name="Function"):
    print(f"{name} is printting {log}")

log2()