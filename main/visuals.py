import matplotlib.pyplot as plt
import numpy as np


def plot_frequency_bar_chart(outcomes, relative_frequencies, theoretical_probs=None, title=None):
    outcomes = list(outcomes)
    rel_freqs = np.array(relative_frequencies, dtype=float)
    x = np.arange(len(outcomes))

    fig, ax = plt.subplots()
    ax.bar(x, rel_freqs, label="Observed")

    if theoretical_probs:
        theo = [theoretical_probs.get(str(o), 0) for o in outcomes]
        ax.plot(x, theo, marker="o", linestyle="--", label="Theoretical")

    ax.set_xticks(x)
    ax.set_xticklabels(outcomes)
    ax.set_ylabel("Relative Frequency")

    if title:
        ax.set_title(title)

    ax.legend()
    fig.tight_layout()
    return fig


def plot_threat_risk_bar(adjusted_attack_prob, title=None):
    safe_prob = 1 - adjusted_attack_prob

    fig, ax = plt.subplots()
    ax.bar(["Successful Attack", "Attack Blocked"], [adjusted_attack_prob, safe_prob])
    ax.set_ylim(0, 1)
    ax.set_ylabel("Probability")

    if title:
        ax.set_title(title)

    for i, value in enumerate([adjusted_attack_prob, safe_prob]):
        ax.text(i, value + 0.02, f"{value:.2f}", ha="center")

    fig.tight_layout()
    return fig
