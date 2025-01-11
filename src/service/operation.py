from src.dao import DocumentDao, IndexDao, Search

class DBOperation:
    def __init__(self, session):
        self.document_dao = DocumentDao(session)
        self.index_dao = IndexDao(session)
        self.search = Search(session)

    def insert_document(self, documents):
        for document in documents:
            self.document_dao.insert(document)

    def search_document(self, keywords, strategy):
        if not keywords:
            return []
        keywords = [x.lower() for x in keywords]
        return self.search.search(keywords, strategy)
