def main():
    infile = open('clients.txt', 'r')
    

    a = 1
    for line in infile:
        print(f"{a}. {line.rstrip()}")
        a += 1

main()