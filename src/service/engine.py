from src.dao import Session
from src.service.operation import DBOperation
import threading
import logging


class Engine(threading.Thread):
    def __init__(self):
        self.session = Session()
        self.db_operation = DBOperation(self.session)
        threading.Thread.__init__(self, target=self.operation)

    def operation(self):
        while True:
            action = input("Input action:")
            if action.upper() == "INSERT":
                documents = [x for x in input("provide documents:").split(",")]
                self.db_operation.insert_document(documents)
            elif action.upper() == "SEARCH":
                keywords = ["I", "am"]
                operation = "not"
                result = self.db_operation.search_document(keywords, operation)
                print(result)
            else:
                logging.error("Invalid action provided!")
    
    def initialize(self):
        # Starting the operation method in a separate thread
        engine_thread = threading.Thread(target=self.operation, daemon=True)
        engine_thread.start()

class EngineController:
    def __init__(self):
        engine = Engine()
        engine.start()
        engine.join()