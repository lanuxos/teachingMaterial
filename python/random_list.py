import random

def get_names():
    print("Enter names separated by commas (e.g. Alice,Bob,Charlie):")
    input_str = input("Names: ")
    names = [name.strip() for name in input_str.split(',') if name.strip()]
    return names

def pick_winner(names):
    return random.choice(names)

def main():
    names = get_names()
    if not names:
        print("No valid names entered.")
        return

    winner = pick_winner(names)
    print(f"🎉 The winner is: {winner} 🎉")

if __name__ == "__main__":
    main()
