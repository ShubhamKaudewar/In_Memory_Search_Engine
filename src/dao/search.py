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

# FIXME: Think for logic to add basic ranking algorithm
class StrategyAND(Strategy):
    def search_operation(self, session, keywords) -> List[int]:
        _ids = [set(session.index_data.get(keyword, [])) for keyword in keywords]
        return list(set.intersection(*_ids))

class StrategyOR(Strategy):
    def search_operation(self, session, keywords) -> List[int]:
        _ids = [session.index_data.get(keyword, []) for keyword in keywords]
        return list(set().union(*_ids))

class StrategyNOT(Strategy):
    def search_operation(self, session, keywords) -> List[int]:
        document_keys = set(session.document_data.keys())
        excluded_keys = set().union(*[session.index_data.get(keyword, []) for keyword in keywords])
        return list(document_keys - excluded_keys)