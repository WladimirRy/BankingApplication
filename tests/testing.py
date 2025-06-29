from src.masks import get_mask_account, get_mask_card_number

card_client_input = str(input("Enter card numder (str):"))
print(get_mask_card_number(card_client_input))


score_client_input = str(input("Enter score numder (str):"))
print(get_mask_account(score_client_input))
