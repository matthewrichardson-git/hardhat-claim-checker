import streamlit as st

st.set_page_config(page_title="HardHat Claim Checker", page_icon="🪖", layout="centered")

NAVY = "#1B2A4A"
ORANGE = "#F5A623"

st.markdown(f"""
<style>
    .stApp {{ background-color: #F4F6F9; }}
    h1, h2, h3 {{ color: {NAVY}; }}
    .hh-banner {{
        background: {NAVY}; padding: 22px 26px; border-radius: 12px; margin-bottom: 18px;
    }}
    .hh-banner h1 {{ color: white; margin: 0; font-size: 30px; }}
    .hh-banner p {{ color: {ORANGE}; margin: 4px 0 0 0; font-weight: 600; }}
    .hh-result {{
        background: white; border-left: 6px solid {ORANGE}; padding: 18px 22px;
        border-radius: 8px; margin: 10px 0; box-shadow: 0 1px 4px rgba(0,0,0,0.08);
    }}
    .stButton>button {{
        background: {ORANGE}; color: {NAVY}; font-weight: 700; border: none;
        padding: 10px 26px; border-radius: 8px;
    }}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hh-banner">
    <h1>🪖 HardHat Claim Checker</h1>
    <p>Workers' comp, made clear. Answer 6 quick questions.</p>
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
        st.markdown(f"""<div class="hh-result"><h3>✅ You likely have a valid claim</h3>
        <p>Nearly every employer in {state if state != 'Other / not listed' else 'the U.S.'} is required to carry workers' compensation coverage.
        An injury that happened at work or because of work is generally covered, including {injury.lower().split('(')[0].strip()} injuries.
        You do NOT have to prove your employer did anything wrong. Comp is no-fault.</p></div>""", unsafe_allow_html=True)
    else:
        st.markdown("""<div class="hh-result"><h3>⚠️ Your window may be closing or closed</h3>
        <p>Based on the timing you selected, the standard filing deadline may have passed. There are exceptions (late discovery, employer misconduct, ongoing benefits), so don't assume it's over. Talk to someone.</p></div>""", unsafe_allow_html=True)

    # ---- 2. Deadlines ----
    st.markdown(f"""<div class="hh-result"><h3>⏰ Deadlines in your state</h3>
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
    st.markdown(f"""<div class="hh-result"><h3>👉 Your next 3 steps</h3>{steps_html}</div>""", unsafe_allow_html=True)

    # ---- 4. Attorney trigger ----
    complex_flags = {"My claim was denied", "I think I'm being punished for reporting", "The injury looks permanent"}
    if status in complex_flags or not likely:
        st.markdown("""<div class="hh-result" style="border-left-color:#C0392B;"><h3>⚖️ Talk to an attorney. Seriously.</h3>
        <p>Your situation shows the signals (denial, retaliation, permanent injury, or deadline risk) where workers who get representation
        do meaningfully better. Workers' comp attorneys work on contingency: free consult, no fee unless you recover.
        In the full HardHat product, this is where we'd match you with a vetted attorney in your state.</p></div>""", unsafe_allow_html=True)
    else:
        st.markdown("""<div class="hh-result"><h3>💪 You can likely handle this stage yourself</h3>
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
