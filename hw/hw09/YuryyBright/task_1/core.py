import random

MAX_ATTEMPTS = 10

class GuessGame:
    def __init__(self):
        self.secret = random.randint(1, 100)
        self.attempts = 0
        self.over = False
        self.win = False
        self.message = "👋 Guess a number between 1 and 100"

    def guess(self, number: int) -> None:
        if self.over:
            return

        self.attempts += 1

        if number == self.secret:
            self.win = True
            self.over = True
            self.message = random.choice([
                "🎉 You win! Free internet for 5 seconds!",
                "🧠 Big brain moment!",
                "🚀 NASA called. They want their guesser back!",
                "🤯 You guessed it! You're now legally a wizard.",
                "🍕 Pizza is on the way! (not really)"
            ])
        elif self.attempts >= MAX_ATTEMPTS:
            self.over = True
            self.message = f"💀 Out of tries. It was {self.secret}!"
        elif number < self.secret:
            self.message = f"🔼 Too low! Tries left: {MAX_ATTEMPTS - self.attempts}"
        else:
            self.message = f"🔽 Too high! Tries left: {MAX_ATTEMPTS - self.attempts}"

    def reset(self):
        self.__init__()
