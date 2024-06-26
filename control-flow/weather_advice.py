weather = input("What's the weather like today? (sunny/rainy/cold): ")

if weather == 'sunny':
    WearThis = "Wear a t-shirt and sunglasses."
elif weather == 'cold':
    WearThis = "Make sure to wear a warm coat and a scarf."
else:
    WearThis = "Don’t forget your umbrella and a raincoat."

print(WearThis)