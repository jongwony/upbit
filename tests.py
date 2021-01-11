from upbit.api.exchange import Assets, Orders


def test_asset():
    assets = Assets()
    assert assets.accounts()[0]['unit_currency'] == 'KRW'


def test_orders_chance():
    orders = Orders()
    assert orders.chance(market='KRW-ETH')['market']['id'] == 'KRW-ETH'


def test_order():
    # orders = Orders()
    # assert orders.order(uuid='9ca023a5-851b-4fec-9f0a-48cd83c2eaae')['uuid'] == '9ca023a5-851b-4fec-9f0a-48cd83c2eaae'
    pass
