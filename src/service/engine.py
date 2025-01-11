from src.dao import Session
from src.service.operation import DBOperation
import threading
import logging

class Engine(threading.Thread):
    def __init__(self):
        self.session = Session()
        self.db_operation = DBOperation(self.session)
        self._kill = threading.Event()
        super().__init__(target=self.operation)

    def operation(self):
        while not self._kill.is_set():
            try:
                action = input("Input action: ")
                if action.upper() == "INSERT":
                    documents = [x for x in input("provide documents:").split(",")]
                    self.db_operation.insert_document(documents)
                elif action.upper() == "SEARCH":
                    keywords = ["I", "am"]
                    operation = "not"
                    result = self.db_operation.search_document(keywords, operation)
                    print(result)
                elif action.upper() == "CLOSE":
                    print("Closing database!")
                    self._kill.set()  # Signal the thread to exit
                else:
                    logging.error("Invalid action provided!")
            except Exception as e:
                logging.error(f"Error: {e}")

    def stop(self):
        self._kill.set()

class EngineController:
    def __init__(self):
        self.engine = Engine()
        self.engine.start()

    def stop_engine(self):
        self.engine.stop()
        self.engine.join()  # Wait for the thread to exit