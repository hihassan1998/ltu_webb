class Player:
    def __init__(self, name):
        self.name = name
        self.used_rules = []
        self.used_rules_scores = {}

    def add_score(self, rule_name, score):
        """Add score to this player for the given rule."""
        if rule_name not in self.used_rules:
            self.used_rules.append(rule_name)
            self.used_rules_scores[rule_name] = score

    def has_used_rule(self, rule_name):
        """Check if this player has already used the given rule."""
        return rule_name in self.used_rules

    def total_score(self):
        """Calculate the total score for this player."""
        return sum(self.used_rules_scores.values())

    def to_dict(self):
        """Convert Player object to a dictionary."""
        return {
            'name': self.name,
            'used_rules': self.used_rules,
            'used_rules_scores': self.used_rules_scores
        }

    @staticmethod
    def from_dict(data):
        """Create a Player object from a dictionary."""
        player = Player(data['name'])
        player.used_rules = data['used_rules']
        player.used_rules_scores = data['used_rules_scores']
        return player
