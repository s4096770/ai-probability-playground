import numpy as np
import pandas as pd

def roll_dice(n=100):
    """Simulate n rolls of a 6-sided die."""
    return pd.Series(np.random.randint(1, 7, size=n))

def flip_coin(n=100):
    """Simulate n flips of a fair coin (1=heads, 0=tails)."""
    return np.random.choice([0, 1], size=n)
