weather = input("What's the weather like today? ")

if weather == "sunny":
    WearThis = "Wear a t-shirt and sunglasses."
elif weather == "cold":
    WearThis = "Don’t forget your umbrella and a raincoat."
else:
    WearThis = "Make sure to wear a warm coat and a scarf."

print(WearThis)