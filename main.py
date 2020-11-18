import requests


while True:
    l=input('English(E/e)/Romana(R/r)').lower()
    if l=='e' or l=='r':
        break
    elif l!='e' or l!='r':
        print('Error:Unknown language/Ati introdus o limba necunoscuta...')
        print('Doriti sa iesiti sau incercati din nou?')
        retry=str(input('Exit(E/e)/Retry(R/r)').lower())
        if retry=='e':
            exit()

while True:
    if l=='e':
        def dom():
            print('Write the domain of the site tou want to obtain HTML and CSS("https://domen"):', end='')
        def save():
            print('Write in a file.txt(F/f)/Write in terminal(T/t):',end='')
        def end():
            print("That's all. Do yu want to exit(E/e) or to repeat(R/r)?",end='')
    elif l=='r':
        def dom():
            print('Introduceti adresa site-ului a carui HTML si CSS cod doriti sa extrageti("https://domen"):', end='')
        def save():
            print('Scrie rezultatul in file.txt(F/f)/Afiseaja rezultatul in terminal(T/t):',end='')
        def end():
            print('Gata. Doriti sa iesiti din program(E/e) sau sa mai extrageti codul dintr-un site(R/r)?',end='')

    dom()

    i=str(input())
    r = requests.get(i).text

    save()
    k=str(input().lower())

    if k=='t':
        print(r)
    elif k=='f':
        i=i.replace('/','|')
        my_file=open(f'{i}.txt',"w+")
        my_file.write(r)

    end()
    end=str(input().lower())

    if end=='e':
        exit()
