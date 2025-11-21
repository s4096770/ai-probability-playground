import numpy as np
import pandas as pd


def _relative_frequencies(counts):
    total = counts.sum()
    return counts / total if total > 0 else np.zeros_like(counts)


def simulate_coin_flips(n_trials):
    outcomes = np.random.choice(["Heads", "Tails"], size=n_trials)
    unique, counts = np.unique(outcomes, return_counts=True)

    df = pd.DataFrame({
        "outcome": unique,
        "count": counts,
        "relative_frequency": _relative_frequencies(counts),
    }).sort_values("outcome")

    summary = {
        "Total trials": f"{n_trials:,}",
        "Heads frequency": f"{df.loc[df['outcome'] == 'Heads', 'relative_frequency'].iloc[0]:.3f}",
        "Tails frequency": f"{df.loc[df['outcome'] == 'Tails', 'relative_frequency'].iloc[0]:.3f}",
    }

    return df.reset_index(drop=True), summary


def simulate_dice_rolls(n_trials):
    outcomes = np.random.randint(1, 7, size=n_trials)
    unique, counts = np.unique(outcomes, return_counts=True)

    df = pd.DataFrame({
        "outcome": unique.astype(str),
        "count": counts,
        "relative_frequency": _relative_frequencies(counts),
    }).sort_values("outcome")

    summary = {
        "Total rolls": f"{n_trials:,}",
        "Most frequent face": df.sort_values("relative_frequency", ascending=False)["outcome"].iloc[0],
        "Max relative frequency": f"{df['relative_frequency'].max():.3f}",
    }

    return df.reset_index(drop=True), summary


def simulate_threat_scenarios(base_attack_prob, defence_strength, n_scenarios):
    adjusted_prob = base_attack_prob * (1 - defence_strength)
    adjusted_prob = max(0.0, min(1.0, adjusted_prob))

    attacks = np.random.rand(n_scenarios) < adjusted_prob

    scenarios_df = pd.DataFrame({
        "scenario_id": np.arange(1, n_scenarios + 1),
        "attack_successful": attacks
    })

    success_rate = attacks.mean()

    summary = {
        "Simulated scenarios": f"{n_scenarios:,}",
        "Adjusted attack probability": round(adjusted_prob, 3),
        "Observed success rate": round(success_rate, 3),
        "Successful attacks": int(attacks.sum()),
        "Blocked attacks": int((~attacks).sum()),
    }

    return scenarios_df, summary
