def main():
    card = "".join(str(input("Please, enter your credit card number: ")).split())
    # reads input and removes every whitespace in it
    card_reversed = card[::-1]  # card number string written backwards
    luth_check = 0  # variable to check its mod 10
    for i, v in enumerate(card_reversed):
        if i % 2 == 0:
            luth_check += int(v)
        else:
            to_add = (int(v) * 2 // 10) + (int(v) * 2 % 10)
            luth_check += to_add
    if luth_check % 10 != 0:
        print("Your credit card number is invalid")
    else:
        print("Your credit card number is valid, proceed to payment")

if __name__ == "__main__":
    main()
