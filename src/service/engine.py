from src.dao import Session
from src.service import DBOperation, InputController
import threading
import logging

class Engine(threading.Thread):
    def __init__(self):
        super().__init__(target=self.operation)
        self.session = Session()
        self.db_operation = DBOperation(self.session)
        self._kill = threading.Event()
        self.input = InputController()

    def operation(self):
        print("Engine started!")
        while not self._kill.is_set():
            try:
                action = input("Input action: ")
                if action.upper() == "INSERT":
                    self.db_operation.insert_document(self.input.input(action))
                elif action.upper() == "SEARCH":
                    result = self.db_operation.search_document(*self.input.input(action))
                    print(result)
                elif action.upper() == "CLOSE":
                    print("Closing database!\nEngine Stopped!")
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

