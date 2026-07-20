import streamlit as st

st.set_page_config(page_title="HardHat Claim Checker", page_icon="🪖", layout="centered")

# ============================================================
# DESIGN SYSTEM — "HardHat, by way of Cupertino"
# Rich black base, glass surfaces, one electric-blue accent,
# Inter typography, 8px spacing grid, purposeful motion.
# All assignment functionality preserved exactly.
# ============================================================
BG = "#09090B"          # rich black
SURFACE = "rgba(255,255,255,0.04)"   # glass card
BORDER = "rgba(255,255,255,0.08)"
TEXT = "#FAFAFA"
MUTED = "#9CA0AB"
ACCENT = "#4D9FFF"      # electric blue
ACCENT_2 = "#38E1D4"    # cyan (gradient partner, used sparingly)
GOOD = "#30D158"
WARN = "#FF6B6B"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* ---------- foundation ---------- */
.stApp {{
    background:
        radial-gradient(900px 480px at 80% -10%, rgba(77,159,255,0.10), transparent 60%),
        radial-gradient(700px 420px at 0% 10%, rgba(56,225,212,0.06), transparent 55%),
        {BG};
    color: {TEXT};
}}
html, body, [class*="css"] {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    -webkit-font-smoothing: antialiased;
}}
h1, h2, h3 {{ color: {TEXT} !important; letter-spacing: -0.02em; }}
h2 {{ font-weight: 700; font-size: 28px; margin-top: 8px; }}
h3 {{ font-weight: 600; }}
p, li, label {{ color: {TEXT}; }}
hr {{ border-color: {BORDER}; margin: 32px 0; }}
.block-container {{ padding-top: 48px; max-width: 720px; }}

/* ---------- motion ---------- */
@keyframes riseIn {{
    from {{ opacity: 0; transform: translateY(16px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}
@keyframes floatGlow {{
    0%, 100% {{ opacity: 0.55; transform: translateY(0); }}
    50%      {{ opacity: 0.9;  transform: translateY(-6px); }}
}}
@media (prefers-reduced-motion: reduce) {{
    * {{ animation: none !important; transition: none !important; }}
}}

/* ---------- hero ---------- */
.hh-hero {{
    position: relative;
    padding: 56px 8px 40px;
    text-align: center;
    animation: riseIn 0.7s cubic-bezier(0.16, 1, 0.3, 1) both;
}}
.hh-hero .orb {{
    position: absolute; top: -8px; left: 50%;
    width: 220px; height: 220px; transform: translateX(-50%);
    background: radial-gradient(circle, rgba(77,159,255,0.22), transparent 65%);
    filter: blur(28px);
    animation: floatGlow 7s ease-in-out infinite;
    pointer-events: none;
}}
.hh-eyebrow {{
    display: inline-block;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: {ACCENT};
    background: rgba(77,159,255,0.10);
    border: 1px solid rgba(77,159,255,0.25);
    border-radius: 100px;
    padding: 6px 14px;
    margin-bottom: 20px;
}}
.hh-hero h1 {{
    font-size: 46px;
    font-weight: 800;
    line-height: 1.08;
    letter-spacing: -0.03em;
    margin: 0 0 16px;
    background: linear-gradient(180deg, {TEXT} 60%, #B9BDC7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}
.hh-hero .sub {{
    font-size: 17px;
    color: {MUTED};
    max-width: 460px;
    margin: 0 auto;
    line-height: 1.6;
}}
.hh-hero .sub b {{ color: {TEXT}; font-weight: 600; }}
@media (max-width: 640px) {{
    .hh-hero h1 {{ font-size: 34px; }}
    .hh-hero {{ padding: 40px 0 32px; }}
}}

/* ---------- glass cards ---------- */
.hh-card {{
    background: {SURFACE};
    border: 1px solid {BORDER};
    border-radius: 20px;
    padding: 24px 28px;
    margin: 16px 0;
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.35);
    animation: riseIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) both;
    transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
}}
.hh-card:hover {{
    transform: translateY(-3px);
    border-color: rgba(77,159,255,0.35);
    box-shadow: 0 12px 40px rgba(0,0,0,0.45);
}}
.hh-card:nth-of-type(2) {{ animation-delay: 0.08s; }}
.hh-card:nth-of-type(3) {{ animation-delay: 0.16s; }}
.hh-card:nth-of-type(4) {{ animation-delay: 0.24s; }}
.hh-card h3 {{
    font-size: 19px;
    margin: 0 0 10px;
}}
.hh-card p {{
    color: {MUTED};
    font-size: 15px;
    line-height: 1.65;
    margin: 8px 0;
}}
.hh-card p b {{ color: {TEXT}; font-weight: 600; }}
.hh-pill {{
    display: inline-block;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    border-radius: 100px;
    padding: 4px 12px;
    margin-bottom: 12px;
}}
.hh-pill.blue  {{ color: {ACCENT}; background: rgba(77,159,255,0.10); border: 1px solid rgba(77,159,255,0.25); }}
.hh-pill.good  {{ color: {GOOD};   background: rgba(48,209,88,0.10);  border: 1px solid rgba(48,209,88,0.25); }}
.hh-pill.warn  {{ color: {WARN};   background: rgba(255,107,107,0.10); border: 1px solid rgba(255,107,107,0.28); }}

/* ---------- form ---------- */
[data-testid="stForm"] {{
    background: {SURFACE};
    border: 1px solid {BORDER};
    border-radius: 24px;
    padding: 32px 32px 24px;
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.35);
    animation: riseIn 0.7s 0.1s cubic-bezier(0.16, 1, 0.3, 1) both;
}}
[data-testid="stForm"] h3 {{
    font-size: 22px;
    letter-spacing: -0.02em;
}}
.stSelectbox label, .stRadio > label, .stSlider label {{
    color: {MUTED} !important;
    font-size: 14px !important;
    font-weight: 500 !important;
}}
[data-baseweb="select"] > div {{
    background: rgba(255,255,255,0.05) !important;
    border-color: {BORDER} !important;
    border-radius: 12px !important;
    color: {TEXT} !important;
    transition: border-color 0.2s ease;
}}
[data-baseweb="select"] > div:hover {{ border-color: rgba(77,159,255,0.4) !important; }}
.stRadio [role="radiogroup"] label {{ color: {TEXT} !important; }}

/* ---------- buttons ---------- */
.stButton>button, [data-testid="stForm"] button {{
    background: linear-gradient(135deg, {ACCENT}, {ACCENT_2});
    color: #05070D;
    font-family: 'Inter', sans-serif;
    font-weight: 700;
    font-size: 15px;
    letter-spacing: -0.01em;
    border: none;
    padding: 12px 32px;
    border-radius: 100px;
    box-shadow: 0 4px 20px rgba(77,159,255,0.35);
    transition: transform 0.15s ease, box-shadow 0.2s ease, filter 0.2s ease;
}}
.stButton>button:hover, [data-testid="stForm"] button:hover {{
    transform: scale(1.03);
    box-shadow: 0 6px 28px rgba(77,159,255,0.5);
    filter: brightness(1.05);
    color: #05070D;
}}
.stButton>button:active, [data-testid="stForm"] button:active {{ transform: scale(0.98); }}
.stButton>button:focus-visible, [data-testid="stForm"] button:focus-visible {{
    outline: 2px solid {TEXT};
    outline-offset: 3px;
}}

/* ---------- slider + captions ---------- */
.stSlider [data-baseweb="slider"] div[role="slider"] {{
    background: {ACCENT};
    box-shadow: 0 0 0 4px rgba(77,159,255,0.25);
}}
.stCaption, [data-testid="stCaptionContainer"] p {{
    color: {MUTED} !important;
    font-size: 13px !important;
}}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("""
<div class="hh-hero">
    <div class="orb"></div>
    <span class="hh-eyebrow">HardHat 🪖 Claim Checker</span>
    <h1>Workers' comp,<br>made clear.</h1>
    <p class="sub">Six quick questions. One clear readout on your claim, your deadlines, and your next move. <b>No jargon, no runaround.</b></p>
</div>
""", unsafe_allow_html=True)

st.caption("This tool provides general information, not legal advice. Every situation is different.")

# ---------------- STATE DEADLINE DATA (seed: TN + neighbors) ----------------
STATE_RULES = {
    "Tennessee": {"notice_days": 15, "claim_years": 1,
                  "note": "Tennessee requires written notice to your employer within 15 days of the injury. A claim petition generally must be filed within 1 year."},
    "Georgia": {"notice_days": 30, "claim_years": 1,
                "note": "Georgia requires notice to your employer within 30 days. A claim generally must be filed within 1 year of the accident."},
    "North Carolina": {"notice_days": 30, "claim_years": 2,
                       "note": "North Carolina requires written notice within 30 days. A claim generally must be filed within 2 years."},
    "South Carolina": {"notice_days": 90, "claim_years": 2,
                       "note": "South Carolina requires notice within 90 days. A claim generally must be filed within 2 years."},
    "Alabama": {"notice_days": 5, "claim_years": 2,
                "note": "Alabama expects notice quickly (within days, 90 at the outside). A claim generally must be filed within 2 years."},
    "Other / not listed": {"notice_days": None, "claim_years": None,
                           "note": "Deadlines vary by state. Report your injury in writing as soon as possible; many states allow as few as 15-30 days."},
}

with st.form("wizard"):
    st.subheader("Your situation")

    state = st.selectbox("1. What state do you work in?", list(STATE_RULES.keys()))
    industry = st.selectbox("2. What industry do you work in?",
        ["Construction / trades", "Manufacturing", "Warehousing / logistics", "Landscaping / outdoor services", "Other physical work", "Office / other"])
    injury = st.selectbox("3. What kind of injury?",
        ["Sprain / strain (back, shoulder, knee, etc.)", "Cut / laceration", "Broken bone",
         "Repetitive stress (developed over time)", "Head injury / concussion", "Illness from work exposure", "Other"])
    reported = st.radio("4. Did you report the injury to your employer?",
        ["Yes, in writing", "Yes, but only verbally", "No, not yet"])
    timing = st.selectbox("5. How long ago did the injury happen?",
        ["Within the last week", "1-4 weeks ago", "1-6 months ago", "6-12 months ago", "More than a year ago"])
    status = st.selectbox("6. What best describes your situation right now?",
        ["Still working, pushing through it", "On light duty", "Off work, no pay coming in",
         "My claim was denied", "I think I'm being punished for reporting", "The injury looks permanent"])

    submitted = st.form_submit_button("Check my situation →")

if submitted:
    rules = STATE_RULES[state]

    st.markdown("---")
    st.header("Your readout")

    # ---- 1. Do you likely have a claim? ----
    likely = True
    caveats = []
    if timing == "More than a year ago" and (rules["claim_years"] or 2) <= 1:
        likely = False
        caveats.append("Your filing window may already be closed, but exceptions exist. This is worth a free consult with an attorney.")
    if reported == "No, not yet":
        caveats.append("Not reporting yet doesn't kill your claim, but the clock is running. Report it in writing today.")
    if industry == "Office / other":
        caveats.append("Office injuries are absolutely covered too. Workers' comp isn't just for job sites.")

    if likely:
        st.markdown(f"""<div class="hh-card">
        <span class="hh-pill good">Claim viability</span>
        <h3>✅ You likely have a valid claim</h3>
        <p>Nearly every employer in {state if state != 'Other / not listed' else 'the U.S.'} is required to carry workers' compensation coverage.
        An injury that happened at work or because of work is generally covered, including {injury.lower().split('(')[0].strip()} injuries.
        You do <b>NOT</b> have to prove your employer did anything wrong. Comp is no-fault.</p></div>""", unsafe_allow_html=True)
    else:
        st.markdown("""<div class="hh-card">
        <span class="hh-pill warn">Claim viability</span>
        <h3>⚠️ Your window may be closing or closed</h3>
        <p>Based on the timing you selected, the standard filing deadline may have passed. There are exceptions (late discovery, employer misconduct, ongoing benefits), so don't assume it's over. Talk to someone.</p></div>""", unsafe_allow_html=True)

    # ---- 2. Deadlines ----
    st.markdown(f"""<div class="hh-card">
    <span class="hh-pill blue">{state}</span>
    <h3>⏰ Deadlines in your state</h3>
    <p>{rules['note']}</p></div>""", unsafe_allow_html=True)

    # ---- 3. Next 3 steps ----
    steps = []
    if reported != "Yes, in writing":
        steps.append("Report the injury to your employer in writing (text or email counts, keep a copy). Do this first, today.")
    steps.append("See a doctor and tell them clearly it's a work injury, so it enters the medical record that way. Your employer or their insurer may direct you to an approved provider.")
    steps.append("Write down what happened while it's fresh: date, time, place, witnesses, what you were doing. Photos help.")
    if len(steps) < 3:
        steps.append("Keep every document: medical bills, work restrictions, pay stubs showing missed time.")

    steps_html = "".join([f"<p><b>{i+1}.</b> {s}</p>" for i, s in enumerate(steps[:3])])
    st.markdown(f"""<div class="hh-card">
    <span class="hh-pill blue">Action plan</span>
    <h3>👉 Your next 3 steps</h3>{steps_html}</div>""", unsafe_allow_html=True)

    # ---- 4. Attorney trigger ----
    complex_flags = {"My claim was denied", "I think I'm being punished for reporting", "The injury looks permanent"}
    if status in complex_flags or not likely:
        st.markdown("""<div class="hh-card">
        <span class="hh-pill warn">Representation advised</span>
        <h3>⚖️ Talk to an attorney. Seriously.</h3>
        <p>Your situation shows the signals (denial, retaliation, permanent injury, or deadline risk) where workers who get representation
        do meaningfully better. Workers' comp attorneys work on contingency: free consult, no fee unless you recover.
        In the full HardHat product, this is where we'd match you with a vetted attorney in your state.</p></div>""", unsafe_allow_html=True)
    else:
        st.markdown("""<div class="hh-card">
        <span class="hh-pill good">You've got this</span>
        <h3>💪 You can likely handle this stage yourself</h3>
        <p>Straightforward, reported, recent claims usually don't need a lawyer. If your claim gets denied, payments stop,
        or your employer pushes back, that's when to get one. HardHat will be here for that moment.</p></div>""", unsafe_allow_html=True)

    if caveats:
        st.markdown("**Worth knowing:**")
        for c in caveats:
            st.markdown(f"- {c}")

    st.markdown("---")
    st.subheader("Was this useful?")
    rating = st.slider("Rate this readout", 1, 5, 4)
    st.caption("In the pilot, this rating plus completion data tests whether guided readouts beat a Google search. Thanks for helping us find out.")

st.markdown("---")
st.caption("HardHat MVP v0.1 • Built by Matthew Richardson • ENT 451, University of Tennessee • Informational guidance only, not legal advice.")
