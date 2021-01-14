if __name__ == '__main__':

    from classs import *

    url = ArrayStack()
    while True:
        print('Menu:\n')
        print('1.Go to a new web.\t2.Go back to the last web\t')
        print('3.Print the last web\t4.Look up all the web before\t')
        print('5.Break')
        choose = int(input())
        if choose == 1:
            url.openWeb(input())
        elif choose == 2:
            url.backWeb()
        elif choose == 3:
            print(url.lastWebName())
        elif choose == '4':
            print(url)
        else:
            break
