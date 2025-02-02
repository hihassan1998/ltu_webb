from src.die import Die


class Hand:
    def __init__(self, dice_values=None):
        self.dice = []
        
        if dice_values is None:
            for _ in range(5):
                self.dice.append(Die())
        else:
            for value in dice_values:
                self.dice.append(Die(value))
        

    def roll(self, indexes=None):

        if indexes is None:
            for die in self.dice:
                die.roll()
                
        # Print the dice values after the roll
        print("Dice values after rolling:")
        for die in self.dice:
            print(f"{die.get_name()} (Value: {die.get_value()})")
        

    def __str__(self):
        die_strings = []
        
        for die in self.dice:
            die_strings.append(str(die))
        return ", ".join(die_strings)