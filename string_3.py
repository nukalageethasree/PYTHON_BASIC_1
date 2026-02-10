while True :
    name=input("\n enter your name:")
    if not  name.isalpha():
        print("invalid name,sorry you cannot proceed")
        break
    else:
        pan_card_number=input("\n enter your pan card number:")
        if not  pan_card_number.isalnum():
            print("\n invalid pan card number,sorry you cannot proceed")
            break
        print(f"Please check, {name}, your PAN card number is: {pan_card_number}")
    
    break

