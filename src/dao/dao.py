import logging
from src.util import DateUtil, CryptoUtil
from typing import List


class DBDao:
    def __init__(self, session):
        self.session = session
        self.document_data = session.document_data
        self.index_data = session.index_data
        self.phrase_data = session.phrase_data

class PhraseDao(DBDao):
    def __init__(self, session):
        super().__init__(session)
        self.date_util = DateUtil()
        self.crypto_util = CryptoUtil()

    def _is_duplicate(self, document_hash: str) -> bool:
        return document_hash in self.phrase_data

    def insert(self, document: str) -> tuple[bool, int]:
        document_hash = self.crypto_util.md5_hash(document)
        if self._is_duplicate(document_hash):
            logging.info("phrase already exist in database")
            return False, 0

        phrase_id = self.date_util.delayed_time
        self.phrase_data[document_hash] = phrase_id
        return True, phrase_id

class DocumentDao(DBDao):
    def __init__(self, session):
        super().__init__(session)
        self.phrase_dao = PhraseDao(session)
        self.index_dao = IndexDao(session)
        self.crypto_util = CryptoUtil()

    def insert(self, document: str) -> None:
        status, phrase_id = self.phrase_dao.insert(document)
        if not status:
            return

        self.document_data[phrase_id] = document

        # Update Index graph
        keywords = document.lower().split(" ")
        self.index_dao.update(keywords, phrase_id)

class IndexDao(DBDao):
    def __init__(self, session):
        super().__init__(session)

    def update(self, keywords: List[str], document_id: int) -> None:
        for keyword in keywords:
            self.index_data[keyword][1].append(document_id)
