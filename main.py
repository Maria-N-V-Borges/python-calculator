from calculator import calculator
from math_game import jogar

def main():
    while True: 
        print("\n=== MAIN MENU ===")
        print("1 - Calculator")
        print("2 - Multiplication Challenge")
        print("0 - Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            calculator()

        elif choice == "2":
            jogar()

        elif choice == "0":
            print("Closing program...")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()