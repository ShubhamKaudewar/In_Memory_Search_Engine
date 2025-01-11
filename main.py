from src.service.engine import EngineController

def main():
    controller = EngineController()
    try:
        controller.engine.join()  # Main thread waits for Engine
    except KeyboardInterrupt:
        controller.stop_engine()
        print("Engine stopped.")

if __name__ == "__main__":
    main()

# {
#     "1": "I am a developer",
#     "2": "I am Indian",
#     "3": "I am an Indian developer",
#     "4": "Raj is not Indian developer"
# }
# I am a developer,I am Indian,I am an Indian developer,Raj is not Indian developer