from ..utils.meta import upbit_qs


class Assets:
    """
    자산
    """

    @staticmethod
    @upbit_qs
    def accounts():
        """
        내가 보유한 자산 리스트를 보여줍니다.
        https://docs.upbit.com/reference#%EC%A0%84%EC%B2%B4-%EA%B3%84%EC%A2%8C-%EC%A1%B0%ED%9A%8C
        """
        return {
            'method': 'get',
            'path': '/v1/accounts',
        }


class Orders:
    """
    주문
    """

    @staticmethod
    @upbit_qs
    def chance(market: str):
        """
        마켓별 주문 가능 정보를 확인한다.
        https://docs.upbit.com/reference#%EC%A3%BC%EB%AC%B8-%EA%B0%80%EB%8A%A5-%EC%A0%95%EB%B3%B4

        :param market: 'KRW-ETH'
        """
        return {
            'method': 'get',
            'path': '/v1/orders/chance',
        }

    @staticmethod
    @upbit_qs
    def order(uuid: str = None, identifier: str = None):
        """
        주문 UUID 를 통해 개별 주문건을 조회한다.
        https://docs.upbit.com/reference#%EA%B0%9C%EB%B3%84-%EC%A3%BC%EB%AC%B8-%EC%A1%B0%ED%9A%8C

        :param uuid: 주문 UUID
        :param identifier: 조회용 사용자 지정 값
        """
        return {
            'method': 'get',
            'path': '/v1/order',
        }

    @staticmethod
    @upbit_qs
    def orders(market: str = None, state: str = None, states: list = None, uuids: list = None, identifiers: list = None,
               kind: str = None, page: int = None, limit: int = None, order_by: str = None):
        """
        주문 리스트를 조회한다.
        https://docs.upbit.com/reference#%EC%A3%BC%EB%AC%B8-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%A1%B0%ED%9A%8C

        :param market: Market ID
        :param state: 주문 상태
            {'state': 'done'}
        :param states: 주문 상태 목록
        :param uuids: 주문 UUID의 목록
            [
                '9ca023a5-851b-4fec-9f0a-48cd83c2eaae',
                #...
            ]
        :param identifiers: 주문 identifier의 목록
        :param kind: 주문 유형
        :param page: 요청 페이지
        :param limit: 요청 개수 (1 ~ 100)
        :param order_by: 정렬
        """
        return {
            'method': 'get',
            'path': '/v1/order',
        }

    @staticmethod
    @upbit_qs
    def del_order(uuid: str = None, identifier: str = None):
        """
        주문 UUID를 통해 해당 주문에 대한 취소 접수를 한다.
        https://docs.upbit.com/reference#%EC%A3%BC%EB%AC%B8-%EC%B7%A8%EC%86%8C

        :param uuid: 주문 UUID
            { 'uuid': 'cdd92199-2897-4e14-9448-f923320408ad' }
        :param identifier: 조회용 사용자 지정값
        """
        return {
            'method': 'delete',
            'path': '/v1/order',
        }

    @staticmethod
    @upbit_qs
    def post_order(market: str, side: str, volume: str, price: str, ord_type: str, identifier: str = None):
        """
        주문 요청을 한다.
        https://docs.upbit.com/reference#%EC%A3%BC%EB%AC%B8%ED%95%98%EA%B8%B0

        :param market: Market ID
        :param side: 주문 종류
        :param volume: 주문 수량
        :param price: 유닛당 주문 가격
        :param ord_type 주문 타입
        :param identifier 조회용 사용자 지정 값
        """
        return {
            'method': 'post',
            'path': '/v1/orders',
        }


class Withdraws:
    @staticmethod
    def orders(currency: str = None, state: str = None, uuids: list = None, txids: list = None, limit: int = None,
               page: int = None, order_by: str = None):
        """
        주문 리스트를 조회한다.
        https://docs.upbit.com/reference#%EC%A3%BC%EB%AC%B8-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%A1%B0%ED%9A%8C

        :param currency: Currency 코드
        :param state: 출금 상태
            {'state': 'done'}
        :param uuids: 출금 UUID의 목록
            [
                '9ca023a5-851b-4fec-9f0a-48cd83c2eaae',
                #...
            ]
        :param txids: 출금 TXID의 목록
        :param limit: 갯수 제한
        :param page:
        :param order_by: 정렬
        """
        return {
            'method': 'get',
            'path': '/v1/withdraws'
        }
