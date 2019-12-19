import textgame, constants

def main():
    newgame = textgame.Game()

    newgame.intro()

    while not newgame.done:
        newgame.update()
    

if __name__ == "__main__":
    main()