"""
CareNest AI Adoption — Evidence Dashboard
Run with: streamlit run dashboard/app.py
"""

import json
from pathlib import Path

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "processed" / "dashboard_data.json"

st.set_page_config(page_title="CareNest AI Adoption — Evidence Dashboard", layout="wide")


@st.cache_data
def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


data = load_data()

st.title("CareNest AI Adoption — Evidence Dashboard")
st.caption(
    "A communication layer for the AI investment case. Every figure links back to "
    "`market_research.md`, `opportunities_risks.md`, `use_case_discovery.md` and "
    "`carenest_growth_strategy.md`. Hover any chart for sources."
)

page1, page2 = st.tabs(["CareNest Current Data", "Market & Sector Evidence"])

# ---------------------------------------------------------------------------
# Page 1 — CareNest current data
# ---------------------------------------------------------------------------
with page1:
    # Metric 3 — Caregiver turnover cost (stat cards)
    m3 = data["metric3_turnover_cost"]
    st.header(m3["title"])

    cols3 = st.columns(len(m3["cards"]))
    for col, card in zip(cols3, m3["cards"]):
        with col:
            st.metric(label=card["label"], value=card["value"])
            st.caption(card["context"])

    with st.expander("Sources"):
        for s in m3["sources"]:
            st.caption(f"- {s}")

    st.divider()

    # Metric 6 — CareNest vs sector scorecard
    m6 = data["metric6_scorecard"]
    st.header(m6["title"])

    for row in m6["rows"]:
        st.markdown(f"**{row['metric']}**")
        c1, c2, c3 = st.columns(3)
        c1.markdown(f"*CareNest*\n\n{row['carenest']}")
        c2.markdown(f"*Sector*\n\n{row['sector']}")
        c3.markdown(f"*Position*\n\n{row['position']}")
        st.caption(f"Source: {row['source']}")
        st.markdown("---")

# ---------------------------------------------------------------------------
# Page 2 — Market & sector evidence
# ---------------------------------------------------------------------------
with page2:
    # Metric 7 — Market growth headline KPIs
    st.header("Market Growth Headlines")
    kpi_cols = st.columns(len(data["metric7_kpis"]["cards"]))
    for col, card in zip(kpi_cols, data["metric7_kpis"]["cards"]):
        with col:
            st.metric(label=card["label"], value=card["value"])
            st.caption(card["context"])
            with st.expander("Source"):
                st.caption(card["source"])

    st.divider()

    # Metric 1 — Elderly population vs. caregiver supply gap (DE / UK / US)
    m1 = data["metric1_population_workforce_gap"]
    st.header(m1["title"])
    st.write(m1["subtitle"])

    years = [str(y) for y in m1["years"]]
    fig1 = make_subplots(specs=[[{"secondary_y": True}]])

    fig1.add_trace(
        go.Scatter(
            x=years,
            y=m1["elderly_population_millions"],
            name="Elderly population (M)",
            mode="lines+markers",
            line=dict(color="#d62728"),
        ),
        secondary_y=False,
    )
    fig1.add_trace(
        go.Scatter(
            x=years,
            y=m1["care_workers_millions"],
            name="Care workers (M)",
            mode="lines+markers",
            line=dict(color="#2ca02c", dash="dash"),
        ),
        secondary_y=False,
    )
    fig1.add_trace(
        go.Scatter(
            x=years,
            y=m1["unfilled_vacancies_thousands"],
            name="Unfilled vacancies (k)",
            mode="lines",
            line=dict(color="#1f77b4", dash="dot"),
        ),
        secondary_y=True,
    )

    fig1.update_yaxes(title_text="Millions", secondary_y=False)
    fig1.update_yaxes(title_text="Unfilled vacancies (thousands)", secondary_y=True)
    fig1.update_layout(height=420, legend=dict(orientation="h", yanchor="bottom", y=1.08))
    st.plotly_chart(fig1, use_container_width=True)

    st.caption(m1["note"])

    with st.expander("Sources"):
        for s in m1["sources"]:
            st.caption(f"- {s}")

    st.divider()

    # Metric 2 — AI adoption in elderly/home care, DE vs UK vs US
    m2 = data["metric2_ai_adoption"]
    st.header(m2["title"])
    st.write(m2["subtitle"])

    bars = m2["bars"]
    fig2 = go.Figure(
        go.Bar(
            x=[b["value"] for b in bars],
            y=[b["country"] for b in bars],
            orientation="h",
            text=[f"{b['value']}%" for b in bars],
            textposition="auto",
            marker_color=["#2ca02c", "#1f77b4", "#ff7f0e"],
            customdata=[b["metric_definition"] for b in bars],
            hovertemplate="%{y}: %{x}%<br>%{customdata}<extra></extra>",
        )
    )
    fig2.update_layout(
        xaxis_title="% (definitions vary by country — see note below)",
        height=320,
        yaxis=dict(autorange="reversed"),
    )
    st.plotly_chart(fig2, use_container_width=True)

    for b in bars:
        st.caption(f"**{b['country']}** ({b['value']}%): {b['metric_definition']} — *{b['source']}*")

    st.warning(m2["note"])

    st.divider()

    # Metric 5 — AI documentation time savings, evidence strength
    m5 = data["metric5_documentation_savings"]
    st.header(m5["title"])
    st.write(m5["subtitle"])

    bars5 = m5["bars"]
    fig5 = go.Figure(
        go.Bar(
            x=[b["value"] for b in bars5],
            y=[b["label"] for b in bars5],
            orientation="h",
            text=[f"{b['value']}%" for b in bars5],
            textposition="auto",
            marker_color=["#2ca02c", "#ffbb78", "#aec7e8"],
            customdata=[[b["evidence_tier"], b["detail"]] for b in bars5],
            hovertemplate="%{y}: %{x}%<br>%{customdata[0]}<br>%{customdata[1]}<extra></extra>",
        )
    )
    fig5.update_layout(xaxis_title="Documentation time reduction (%)", height=320, yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig5, use_container_width=True)

    for b in bars5:
        st.caption(f"**{b['label']}** ({b['value']}%) — {b['evidence_tier']}. {b['detail']}. *{b['source']}*")

    st.success(m5["anchor_note"])

    st.divider()

    # Metric 8 — Churn cost vs. AI investment cost
    m8 = data["metric8_cost_vs_churn"]
    st.header(m8["title"])
    st.write(m8["subtitle"])

    bars8 = m8["bars"]
    fig8 = go.Figure(
        go.Bar(
            x=[b["label"] for b in bars8],
            y=[b["value"] for b in bars8],
            text=[f"€{b['value']:,}" for b in bars8],
            textposition="outside",
            marker_color=["#d62728", "#aec7e8", "#9edae5"],
            hovertemplate="%{x}: €%{y:,}<extra></extra>",
        )
    )
    fig8.update_layout(yaxis_title="€ per year", height=380)
    st.plotly_chart(fig8, use_container_width=True)

    st.caption(m8["note"])

    with st.expander("Sources"):
        for s in m8["sources"]:
            st.caption(f"- {s}")
