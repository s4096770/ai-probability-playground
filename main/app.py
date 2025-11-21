import streamlit as st
import pandas as pd
from simulate import (
    simulate_coin_flips,
    simulate_dice_rolls,
    simulate_threat_scenarios,
)
from visuals import (
    plot_frequency_bar_chart,
    plot_threat_risk_bar,
)

st.set_page_config(
    page_title="Probabilistic Risk Assessment Engine",
    layout="wide",
)


def show_header():
    st.title("📊 Probabilistic Risk Assessment Engine")
    st.caption(
        "Model and visualise uncertainty for random events and basic cyber risk scenarios."
    )


def sidebar_controls():
    st.sidebar.header("⚙️ Configuration")
    mode = st.sidebar.radio(
        "Module",
        ["Random Event Simulation", "Threat Risk Assessment"],
    )
    return mode


def random_event_layout():
    st.subheader("🎲 Random Event Simulation")

    col_left, col_right = st.columns([2, 3])

    with col_left:
        st.markdown("### 🧪 Experiment Settings")
        sim_type = st.selectbox("Simulation type", ["Coin flips", "Dice rolls"])
        n_trials = st.slider(
            "Number of trials",
            min_value=10,
            max_value=10_000,
            value=1_000,
            step=10,
        )

        run = st.button("Run Simulation")

    if not run:
        st.info("Configure your experiment and click **Run Simulation**.")
        return

    if sim_type == "Coin flips":
        results_df, summary = simulate_coin_flips(n_trials)
        title = f"Coin flip outcomes over {n_trials:,} trials"
        theoretical = {"Heads": 0.5, "Tails": 0.5}
    else:
        results_df, summary = simulate_dice_rolls(n_trials)
        title = f"Dice roll outcomes over {n_trials:,} trials"
        theoretical = {str(face): 1 / 6 for face in range(1, 7)}

    with col_right:
        st.markdown("### 📈 Outcome Distribution")
        fig = plot_frequency_bar_chart(
            results_df["outcome"],
            results_df["relative_frequency"],
            theoretical_probs=theoretical,
            title=title,
        )
        st.pyplot(fig, clear_figure=True)

    st.markdown("### 📋 Summary Statistics")
    st.dataframe(results_df, use_container_width=True)

    st.markdown("#### 🔍 Key Metrics")
    metric_cols = st.columns(len(summary))
    for col, (label, value) in zip(metric_cols, summary.items()):
        col.metric(label, value)


def threat_risk_layout():
    st.subheader("🛡️ Threat Risk Assessment")

    col_left, col_right = st.columns([2, 3])

    with col_left:
        st.markdown("### ⚠️ Scenario Inputs")

        base_attack_prob = st.slider(
            "Base attack probability",
            min_value=0.0,
            max_value=1.0,
            value=0.2,
            step=0.01,
        )

        defence_strength = st.slider(
            "Defence strength (0 = none, 1 = very strong)",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            step=0.05,
        )

        n_scenarios = st.slider(
            "Number of simulated scenarios",
            min_value=100,
            max_value=50_000,
            value=5_000,
            step=100,
        )

        run = st.button("Run Risk Simulation")

    if not run:
        st.info("Adjust the scenario parameters and click **Run Risk Simulation**.")
        return

    scenarios_df, summary = simulate_threat_scenarios(
        base_attack_prob,
        defence_strength,
        n_scenarios,
    )

    with col_right:
        st.markdown("### 📉 Risk Summary")
        fig = plot_threat_risk_bar(
            summary["Adjusted attack probability"],
            title="Estimated probability of a successful attack",
        )
        st.pyplot(fig, clear_figure=True)

    st.markdown("### 📄 Scenario Outcomes (sample)")
    st.dataframe(scenarios_df.head(20), use_container_width=True)

    st.markdown("#### 🔐 Key Metrics")
    metric_cols = st.columns(len(summary))
    for col, (label, value) in zip(metric_cols, summary.items()):
        col.metric(label, value)


def main():
    show_header()
    mode = sidebar_controls()

    if mode == "Random Event Simulation":
        random_event_layout()
    else:
        threat_risk_layout()


if __name__ == "__main__":
    main()
