#!/usr/bin/env python3
import random
"""
Contains the Die class.
"""
class Die:
    MIN_ROLL_VALUE = 1
    MAX_ROLL_VALUE = 6
    
    def __init__(self, value=None):
        if value is None:
            self.value = random.randint(self.MIN_ROLL_VALUE, self.MAX_ROLL_VALUE)
        elif value > self.MAX_ROLL_VALUE:
            self.value = self.MAX_ROLL_VALUE
        elif value < self.MIN_ROLL_VALUE:
            self.value = self.MIN_ROLL_VALUE
        else:
            self.value = value
        self.roll_values = [self.value]
        
    def get_name(self):
        names = ["one", "two", "three", "four", "five", "six"]
        return names[self.value - 1]

    def get_value(self):
        return self.value

    def roll(self):
        self.value = random.randint(self.MIN_ROLL_VALUE, self.MAX_ROLL_VALUE)
        # print(f"Rolled a die: {self.get_name()} (Value: {self.get_value()})")
        # self.roll_values.append(self.value)
        # print(f"Die rolled to values: {self.roll_values}")
    
    
    def __str__(self):
        return str(self.value)