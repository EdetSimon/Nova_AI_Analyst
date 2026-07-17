from datetime import datetime

class Logger:

        @staticmethod
        def line():
            print("=" * 55)

        @staticmethod
        def info(message):
            print(f"[INFO] {message}")

        @staticmethod
        def success(message):
            print(f"[SUCCESS] {message}")

        @staticmethod
        def warning(message):
            print(f"[WARNING] {message}")

        @staticmethod
        def error(message):
            print(f"[ERROR] {message}")

        @staticmethod
        def startup():
            Logger.line()

            print("🚀 NOVA AI ANALYST")

            Logger.line()

            print("AI-Powered Business Intelligence Assistant")

            print()

            print(f"Startup Time : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

            Logger.line()