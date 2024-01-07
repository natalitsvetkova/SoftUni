square_meters_for_greening = float(input())
price = square_meters_for_greening * 7.61
discount = price * 0.18
final_sum = price - discount
print(f"The final price is: {final_sum} lv.")
print(f"The discount is: {discount} lv.")