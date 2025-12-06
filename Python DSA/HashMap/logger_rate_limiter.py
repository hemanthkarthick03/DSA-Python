"""
LOGGER RATE LIMITER - Easy
Design logger that limits message printing
"""

class Logger:
    def __init__(self):
        self.log = {}
    def should_print_message(self, timestamp, message):
        if message not in self.log or timestamp - self.log[message] >= 10:
            self.log[message] = timestamp
            return True
        return False


if __name__ == "__main__":
    print("✅ Logger Rate Limiter")
