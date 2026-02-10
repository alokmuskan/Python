seat_type = input("Enter seat type (sleeper\AC\general\luxury)").lower()

match seat_type :
    case "sleeper":
        print(f"Sleeper, No Ac")
    case "ac":
        print(f"AC comfortable ride")
    case "general":
        print(f"General cheapest option")
    case "luxury":
        print(f"Luxury seat with food")
    case _:
        print(f"Invalid seat type. Select from options given")