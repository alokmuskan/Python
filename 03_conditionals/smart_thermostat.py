device_status = "online"
temperature = 35

if device_status == "online":
    if temperature > 35:
        print(f"High temperature alert!")
    else:
        print(f"Temperature is Normal")
else:
    print(f"Device is offline")