import streamlit as st

st.set_page_config(page_title="HardHat Claim Checker", page_icon="🪖", layout="centered")

# ---------------- DESIGN TOKENS ----------------
# "Site Diagnostics Terminal" — industrial-futurist, safety-orange on deep graphite
INK = "#0A0F1E"        # page base
PANEL = "#111A30"      # card surface
PANEL_2 = "#0E1628"    # inset surface
LINE = "#22304F"       # hairline borders
ORANGE = "#FF8A00"     # signal / brand
ORANGE_DIM = "#B35F00"
TEXT = "#E8ECF4"
MUTED = "#8A94AD"
RED = "#FF4D4D"
GREEN = "#3DDC97"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

/* ---------- base ---------- */
.stApp {{
    background:
        radial-gradient(1100px 500px at 50% -10%, rgba(255,138,0,0.07), transparent 60%),
        linear-gradient(180deg, #0B1122 0%, {INK} 40%);
    color: {TEXT};
}}
html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}
h1, h2, h3 {{
    font-family: 'Chakra Petch', sans-serif !important;
    color: {TEXT} !important;
    letter-spacing: 0.02em;
}}
p, li, label {{ color: {TEXT}; }}
hr {{ border-color: {LINE}; }}

/* ---------- banner ---------- */
.hh-banner {{
    position: relative;
    background: linear-gradient(135deg, {PANEL} 0%, {PANEL_2} 100%);
    border: 1px solid {LINE};
    border-top: 2px solid {ORANGE};
    border-radius: 14px;
    padding: 30px 32px 26px;
    margin-bottom: 22px;
    overflow: hidden;
}}
.hh-banner::after {{
    content: "";
    position: absolute; inset: 0;
    background: linear-gradient(90deg, transparent, rgba(255,138,0,0.10), transparent);
    transform: translateX(-100%);
    animation: hh-sweep 5s ease-in-out infinite;
    pointer-events: none;
}}
@keyframes hh-sweep {{
    0%   {{ transform: translateX(-100%); }}
    45%  {{ transform: translateX(100%); }}
    100% {{ transform: translateX(100%); }}
}}
@media (prefers-reduced-motion: reduce) {{
    .hh-banner::after {{ animation: none; }}
}}
.hh-eyebrow {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.22em;
    color: {ORANGE};
    text-transform: uppercase;
    margin: 0 0 8px 0;
}}
.hh-banner h1 {{
    color: {TEXT} !important;
    margin: 0;
    font-size: 34px;
    font-weight: 700;
    line-height: 1.1;
}}
.hh-banner .hh-sub {{
    color: {MUTED};
    margin: 10px 0 0 0;
    font-size: 15px;
}}
.hh-banner .hh-sub b {{ color: {TEXT}; }}

/* ---------- readout cards (signature element) ---------- */
.hh-result {{
    position: relative;
    background: {PANEL};
    border: 1px solid {LINE};
    border-radius: 10px;
    padding: 20px 24px 18px;
    margin: 14px 0;
}}
.hh-result::before {{
    /* corner bracket, top-left */
    content: "";
    position: absolute; top: -1px; left: -1px;
    width: 22px; height: 22px;
    border-top: 2px solid {ORANGE};
    border-left: 2px solid {ORANGE};
    border-top-left-radius: 10px;
}}
.hh-result::after {{
    /* corner bracket, bottom-right */
    content: "";
    position: absolute; bottom: -1px; right: -1px;
    width: 22px; height: 22px;
    border-bottom: 2px solid {ORANGE};
    border-right: 2px solid {ORANGE};
    border-bottom-right-radius: 10px;
}}
.hh-result.hh-alert::before, .hh-result.hh-alert::after {{ border-color: {RED}; }}
.hh-result.hh-ok::before, .hh-result.hh-ok::after {{ border-color: {GREEN}; }}
.hh-tag {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 10.5px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: {MUTED};
    margin: 0 0 6px 0;
}}
.hh-tag span {{ color: {ORANGE}; }}
.hh-result.hh-alert .hh-tag span {{ color: {RED}; }}
.hh-result.hh-ok .hh-tag span {{ color: {GREEN}; }}
.hh-result h3 {{
    margin: 0 0 8px 0;
    font-size: 19px;
}}
.hh-result p {{ color: {MUTED}; margin: 6px 0; line-height: 1.55; }}
.hh-result p b {{ color: {TEXT}; }}

/* ---------- form ---------- */
[data-testid="stForm"] {{
    background: {PANEL_2};
    border: 1px solid {LINE};
    border-radius: 14px;
    padding: 26px 26px 20px;
}}
.stSelectbox label, .stRadio label, .stSlider label {{
    color: {MUTED} !important;
    font-weight: 500;
}}
[data-baseweb="select"] > div {{
    background: {PANEL} !important;
    border-color: {LINE} !important;
    color: {TEXT} !important;
}}
.stRadio [role="radiogroup"] label {{ color: {TEXT} !important; }}

/* ---------- buttons ---------- */
.stButton>button, [data-testid="stForm"] button {{
    background: linear-gradient(180deg, {ORANGE}, {ORANGE_DIM});
    color: {INK};
    font-family: 'Chakra Petch', sans-serif;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    border: none;
    padding: 12px 30px;
    border-radius: 8px;
    box-shadow: 0 0 18px rgba(255,138,0,0.35);
    transition: box-shadow 0.2s ease, transform 0.1s ease;
}}
.stButton>button:hover, [data-testid="stForm"] button:hover {{
    box-shadow: 0 0 28px rgba(255,138,0,0.55);
    transform: translateY(-1px);
    color: {INK};
}}
.stButton>button:focus-visible {{
    outline: 2px solid {TEXT};
    outline-offset: 2px;
}}

/* ---------- misc ---------- */
.stCaption, [data-testid="stCaptionContainer"] p {{ color: {MUTED} !important; }}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hh-banner">
    <p class="hh-eyebrow">HardHat // Claim Diagnostics</p>
    <h1>🪖 HardHat Claim Checker</h1>
    <p class="hh-sub">Workers' comp, made clear. <b>Answer 6 quick questions</b> and get your readout.</p>
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
        st.markdown(f"""<div class="hh-result hh-ok">
        <p class="hh-tag">Status // <span>Claim viability</span></p>
        <h3>✅ You likely have a valid claim</h3>
        <p>Nearly every employer in {state if state != 'Other / not listed' else 'the U.S.'} is required to carry workers' compensation coverage.
        An injury that happened at work or because of work is generally covered, including {injury.lower().split('(')[0].strip()} injuries.
        You do <b>NOT</b> have to prove your employer did anything wrong. Comp is no-fault.</p></div>""", unsafe_allow_html=True)
    else:
        st.markdown("""<div class="hh-result hh-alert">
        <p class="hh-tag">Status // <span>Claim viability</span></p>
        <h3>⚠️ Your window may be closing or closed</h3>
        <p>Based on the timing you selected, the standard filing deadline may have passed. There are exceptions (late discovery, employer misconduct, ongoing benefits), so don't assume it's over. Talk to someone.</p></div>""", unsafe_allow_html=True)

    # ---- 2. Deadlines ----
    st.markdown(f"""<div class="hh-result">
    <p class="hh-tag">Timeline // <span>{state}</span></p>
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
    st.markdown(f"""<div class="hh-result">
    <p class="hh-tag">Action plan // <span>Next 72 hours</span></p>
    <h3>👉 Your next 3 steps</h3>{steps_html}</div>""", unsafe_allow_html=True)

    # ---- 4. Attorney trigger ----
    complex_flags = {"My claim was denied", "I think I'm being punished for reporting", "The injury looks permanent"}
    if status in complex_flags or not likely:
        st.markdown("""<div class="hh-result hh-alert">
        <p class="hh-tag">Escalation // <span>Representation advised</span></p>
        <h3>⚖️ Talk to an attorney. Seriously.</h3>
        <p>Your situation shows the signals (denial, retaliation, permanent injury, or deadline risk) where workers who get representation
        do meaningfully better. Workers' comp attorneys work on contingency: free consult, no fee unless you recover.
        In the full HardHat product, this is where we'd match you with a vetted attorney in your state.</p></div>""", unsafe_allow_html=True)
    else:
        st.markdown("""<div class="hh-result hh-ok">
        <p class="hh-tag">Escalation // <span>Not needed yet</span></p>
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
