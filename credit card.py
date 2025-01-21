def card_validate(card):
    # defines if that's American Express, MasterCard or Visa card
    mastercardlist = ["51", "52", "53", "54", "55"]
    if len(card) == 15:
        return "American Express"
    elif len(card) == 16 and card[0] == "4":
        return "Visa"
    elif len(card) == 13 or (len(card) == 16 and card[0:2] not in mastercardlist):
        return  "MasterCard"
    else:
        return False


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

    if card_validate(card):
        print("Sorry, we don't support cards of your credit card company yet!")
    else:
        if luth_check % 10 != 0:
            print(f"Your {card_validate(card)} credit card number is invalid.")
        else:
            print(f"Your {card_validate(card)} credit card number is valid, proceed to payment.")

if __name__ == "__main__":
    main()
