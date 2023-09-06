from engine import Engine

def main():
    hra = Engine()
    
    while not hra.dohrano:
        player_input = input("Zadej index možného tahu: ")
        hra.tah_zadani(player_input)


if __name__ == "__main__":
    main()