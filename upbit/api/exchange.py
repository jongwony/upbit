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


class Withdraw:
    """
    출금
    """

    @staticmethod
    @upbit_qs
    def withdraws(currency: str = None, state: str = None, uuids: list = None, txids: list = None, limit: int = None,
                  page: int = None, order_by: str = None):
        """
        출금 리스트를 조회한다.
        https://docs.upbit.com/reference#%EC%A0%84%EC%B2%B4-%EC%B6%9C%EA%B8%88-%EC%A1%B0%ED%9A%8C

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

    @staticmethod
    @upbit_qs
    def withdraw(uuid: str = None, txid: str = None, currency: str = None):
        """
        출금 UUID를 통해 개별 출금 정보를 조회한다.
        https://docs.upbit.com/reference#%EA%B0%9C%EB%B3%84-%EC%B6%9C%EA%B8%88-%EC%A1%B0%ED%9A%8C

        :param uuid: 출금 UUID
        :param txid: 출금 TXID
        :param currency: Currency 코드
        """
        return {
            'method': 'get',
            'path': '/v1/withdraw'
        }

    @staticmethod
    @upbit_qs
    def chance(currency: str):
        """
        해당 통화의 가능한 출금 정보를 확인한다.
        https://docs.upbit.com/reference#%EC%B6%9C%EA%B8%88-%EA%B0%80%EB%8A%A5-%EC%A0%95%EB%B3%B4

        :param currency: Currency 코드 (BTC ...)
        """
        return {
            'method': 'get',
            'path': '/v1/withdraws/chance'
        }

    @staticmethod
    @upbit_qs
    def withdraws_coin(currency: str, amount: str, address: str,
                       secondary_address: str = None, transaction_type: str = None):
        """
        코인 출금을 요청한다.
        https://docs.upbit.com/reference#%EC%BD%94%EC%9D%B8-%EC%B6%9C%EA%B8%88%ED%95%98%EA%B8%B0

        :param currency: Currency 코드 (BTC ...)
        :param amount: 출금 코인 수량
        :param address: 출금 지갑 주소
        :param secondary_address: 2차 출금주소 (필요한 코인에 한해서)
        :param transaction_type: 출금 유형
        """
        return {
            'method': 'post',
            'path': '/v1/withdraws/coin',
        }

    @staticmethod
    @upbit_qs
    def withdraws_krw(amount: str):
        """
        원화 출금을 요청한다. 등록된 출금 계좌로 출금된다.
        https://docs.upbit.com/reference#%EC%9B%90%ED%99%94-%EC%B6%9C%EA%B8%88%ED%95%98%EA%B8%B0

        :param amount: 출금 원화 수량
        """
        return {
            'method': 'post',
            'path': '/v1/withdraws/krw',
        }


class Deposits:
    """
    입금
    """

    @staticmethod
    @upbit_qs
    def deposits(currency: str = None, state: str = None, uuids: list = None, txids: list = None,
                 limit: int = None, page: int = None, order_by: str = None):
        """
        https://docs.upbit.com/reference#%EC%9E%85%EA%B8%88-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%A1%B0%ED%9A%8C

        :param currency: Currency 코드
        :param state: 입금 상태
        :param uuids: 입금 UUID의 목록
        :param txids: 입금 TXID의 목록
        :param limit: 페이지당 개수
        :param page: 페이지 번호
        :param order_by: 정렬 방식
        """
        return {
            'method': 'get',
            'path': '/v1/deposits',
        }

    @staticmethod
    @upbit_qs
    def deposit(uuid: str = None, txid: str = None, currency: str = None):
        """
        https://docs.upbit.com/reference#%EA%B0%9C%EB%B3%84-%EC%9E%85%EA%B8%88-%EC%A1%B0%ED%9A%8C

        :param uuid: 개별 입금의 UUID
        :param txid: 개별 입금의 TXID
        :param currency: Currency 코드
        """
        return {
            'method': 'get',
            'path': '/v1/deposit',
        }

    @staticmethod
    @upbit_qs
    def generate_coin_address(currency: str):
        """
        입금 주소 생성을 요청한다.
        https://docs.upbit.com/reference#%EC%9E%85%EA%B8%88-%EC%A3%BC%EC%86%8C-%EC%83%9D%EC%84%B1-%EC%9A%94%EC%B2%AD

        :param currency: Currency 코드
        """
        return {
            'method': 'post',
            'path': '/v1/deposits/generate_coin_address',
        }

    @staticmethod
    @upbit_qs
    def coin_addresses():
        """
        내가 보유한 자산 리스트를 보여줍니다.
        https://docs.upbit.com/reference#%EC%A0%84%EC%B2%B4-%EC%9E%85%EA%B8%88-%EC%A3%BC%EC%86%8C-%EC%A1%B0%ED%9A%8C
        """
        return {
            'method': 'get',
            'path': '/v1/deposits/coin_addresses',
        }

    @staticmethod
    @upbit_qs
    def coin_address(currency: str):
        """
        https://docs.upbit.com/reference#%EA%B0%9C%EB%B3%84-%EC%9E%85%EA%B8%88-%EC%A4%8F-%EC%A1%B0%ED%9A%8C

        :param currency: Currency symbol
        """
        return {
            'method': 'get',
            'path': '/v1/deposits/coin_address',
        }


class Status:
    """
    서비스 정보
    """

    @staticmethod
    @upbit_qs
    def wallet():
        """
        입출금 현황 및 블록 상태를 조회합니다.
        https://docs.upbit.com/reference#%EC%9E%85%EC%B6%9C%EA%B8%88-%ED%98%84%ED%99%A9
        """
        return {
            'method': 'get',
            'path': '/v1/status/wallet'
        }

    @staticmethod
    @upbit_qs
    def api_keys():
        """
        API 키 목록 및 만료 일자를 조회합니다.
        https://docs.upbit.com/reference#open-api-%ED%82%A4-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%A1%B0%ED%9A%8C
        """
        return {
            'method': 'get',
            'path': '/v1/api_keys'
        }
