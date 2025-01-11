from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Search:
    def __init__(self, session):
        self.session = session

    def search(self, keywords, strategy: str) -> List[int]:
        if strategy.upper() == "AND":
            return StrategyAND().search_operation(self.session, keywords)
        elif strategy.upper() == "OR":
            return StrategyOR().search_operation(self.session, keywords)
        elif strategy.upper() == "NOT":
            return StrategyNOT().search_operation(self.session, keywords)
        else:
            raise ValueError(f"Invalid strategy: {strategy}")

class Strategy(ABC):
    @abstractmethod
    def search_operation(self, session, keywords) -> List[int]:
        pass

class StrategyAND(Strategy):
    def search_operation(self, session, keywords) -> List[int]:
        _ids, result = [], []
        for keyword in keywords:
            if keyword in session.index_data:
                _ids.append(set(session.index_data[keyword]))
        if _ids: result = list(set.intersection(*_ids))
        return result

class StrategyOR(Strategy):
    def search_operation(self, session, keywords) -> List[int]:
        _ids, result = set(), []
        for keyword in keywords:
            if keyword in session.index_data:
                _ids.update(session.index_data.get(keyword))
        result = list(_ids)
        return result

class StrategyNOT(Strategy):
    def search_operation(self, session, keywords) -> List[int]:
        _ids, result = set(), set(dict(session.document_data).keys())
        for keyword in keywords:
            if keyword in session.index_data:
                _ids.update(session.index_data[keyword])
        result = list(result.difference(_ids))
        return result


# class StrategyAND(Strategy):
#     def search_operation(self, session, keywords) -> List[int]:
#         _ids = [set(session.index_data.get(keyword, [])) for keyword in keywords]
#         return list(set.intersection(*_ids))
#
# class StrategyOR(Strategy):
#     def search_operation(self, session, keywords) -> List[int]:
#         _ids = [session.index_data.get(keyword, []) for keyword in keywords]
#         return list(set().union(*_ids))
#
# class StrategyNOT(Strategy):
#     def search_operation(self, session, keywords) -> List[int]:
#         document_keys = set(session.document_data.keys())
#         excluded_keys = set().union(*[session.index_data.get(keyword, []) for keyword in keywords])
#         return list(document_keys - excluded_keys)