class Challenge:
    def __init__(self, challenge_id, description):
        self.challenge_id = challenge_id
        self.description = description
        self.status = "dostupná"  # Výchozí stav výzvy

    def __str__(self):
        return f"Výzva {self.challenge_id}: {self.description} ({self.status})"