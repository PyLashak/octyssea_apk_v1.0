class User:
    def __init__(self, user_id, name, password):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.score = 0
        self.completed_challenges = []
        self.current_challenge = None

    def complete_challenge(self):
        """
        Počítanie score na základe dokončenia score.

        """
        if self.current_challenge is not None:
            self.score += 1
            self.completed_challenges.append(self.current_challenge)
            self.current_challenge = None