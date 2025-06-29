from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date


card_client_input = str(input("Enter card numder (str):"))
print(get_mask_card_number(card_client_input))


score_client_input = str(input("Enter score numder (str):"))
print(get_mask_account(score_client_input))


date_input = str(input("Enter date (str):"))
print(get_date(date_input))