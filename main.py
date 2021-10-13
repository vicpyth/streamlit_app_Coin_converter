import streamlit as st
from coin_converter import Coin_converter, currency_converter, coin_names, currency_symbol

list_coin_names = coin_names()
currency_sym = currency_symbol()

st.title("Welcome to the HTG to Coin converter")
st.write("""
## Currency I have:
""")


chosen_currency = st.selectbox("Currency Symbol", currency_sym)
st.write("""
## Amount:
""")
# amount = st.number_input("How much?")
amount = float(st.text_input("", "1"))
st.write("""
## Coin I Want:
""")
chosen_coins = st.selectbox("""Choose a Coins""", list_coin_names)
st.write("""
## Amount:
""")

#
# print((type(amount))
#
# chosen_coins = st.selectbox("""Choose a Coins""", list_coin_names)

currency_curr = currency_converter(from_=chosen_currency, to_="USD", quantity=amount, get_price=True,)
# print(chosen_currency)
# print(chosen_coins)
# print(currency_curr)
coin_con = Coin_converter(coin_name=chosen_coins, amount=currency_curr,)

# st.write(
#     """## Calculate
#     """
# )


if len(str(amount)) > 0:
    amount2 = float(st.text_input("", coin_con))
    # st.write(f"""## {amount} {chosen_currency} is ${currency_curr} USD
# """)

#     st.write(f"""## ${amount}{chosen_currency} is currently {coin_con}{chosen_coins}
#
# """)


