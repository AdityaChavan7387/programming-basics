# Write a function to convert USD to INR. The function should take the amount in USD as input and return the equivalent amount in INR. Assume the conversion rate is 1 USD = 75 INR.

def convert_usd_to_inr(usd_amount):
    conversion_rate = 85  # 1 USD = 75 INR
    inr_amount = usd_amount * conversion_rate
    return inr_amount
# Example usage:
usd_amount = int(input("Enter the amount in USD: "))
inr_amount = convert_usd_to_inr(usd_amount)
print(f"{usd_amount} USD is equal to {inr_amount} INR.")    

