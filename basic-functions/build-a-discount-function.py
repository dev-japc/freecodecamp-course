def apply_discount(price, discount):
    if not isinstance(price,(int, float)):
        return 'The price should be a number'
    if not isinstance(discount,(int, float)):
        return 'The discount should be a number'
    if price <= 0:
        return 'The price should be greater than 0'
    if discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'
    discount_amount = price * (discount)/100
    result = price - discount_amount
    return result

if __name__ == '__main__':
    print('20% discount on $100: $', apply_discount(100,20))
    print('60% discount on $100: $', apply_discount(100,60))
