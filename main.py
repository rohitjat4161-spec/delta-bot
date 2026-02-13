from delta_rest_client import DeltaRestClient, OrderType
import os
# ========= LOGIN =========


delta_client = DeltaRestClient(
    base_url='https://cdn-ind.testnet.deltaex.org',
    api_key=os.environ.get("DELTA_KEY"),
    api_secret=os.environ.get("DELTA_SECRET")
)

PRODUCT_ID = 84   # your BTC product


# ========= CORE FUNCTION =========
def execute_trade(side, size=1):

    side = side.lower()

    print(f"\n⚡ Executing {side.upper()} trade...")

    # ✅ correct method
    position = delta_client.get_position(product_id=PRODUCT_ID)

    current_size = float(position.get("size", 0))

    print("Current position size:", current_size)

    # Close opposite
    if side == "buy" and current_size < 0:
        print("Closing SHORT first...")
        delta_client.place_order(
            product_id=PRODUCT_ID,
            size=abs(current_size),
            side='buy',
            order_type=OrderType.MARKET
        )

    elif side == "sell" and current_size > 0:
        print("Closing LONG first...")
        delta_client.place_order(
            product_id=PRODUCT_ID,
            size=abs(current_size),
            side='sell',
            order_type=OrderType.MARKET
        )

    # Open new trade
    print("Opening new position...")
    response = delta_client.place_order(
        product_id=PRODUCT_ID,
        size=size,
        side=side,
        order_type=OrderType.MARKET
    )

    print("Order Response:", response)
