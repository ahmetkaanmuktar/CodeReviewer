def calc(a,b):
    return a+b

def main():
    print(calc(10, 20))
    # This is a bad variable name
    x = "hello" 
    if x == "hello":
        print("World")
    
    items = [1,2,3]
    # Inefficient loop
    for i in range(len(items)):
        print(items[i])

if __name__ == "__main__":
    main()
