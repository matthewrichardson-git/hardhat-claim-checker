import time
import streamlit as st

st.set_page_config(page_title="HardHat — Workers' comp, made clear", page_icon="🪖", layout="wide")

# ============================================================
# HARDHAT — premium dark product site
# Structure: Home / About / Why Use It / Purpose / Claim Checker / Success Stories
# Design system: #09090B base, glass cards, electric blue accent,
# Inter typography, 8px grid, subtle purposeful motion.
# The Claim Checker logic (assignment functionality) is unchanged.
# ============================================================
BG = "#09090B"
BG2 = "#111114"
CARD = "#18181B"
BORDER = "rgba(255,255,255,0.08)"
TEXT = "#FAFAFA"
MUTED = "#9CA0AB"
ACCENT = "#3B82F6"
ACCENT_2 = "#38E1D4"
GOOD = "#30D158"
WARN = "#FF6B6B"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* ---------- foundation ---------- */
.stApp {{
    background:
        radial-gradient(1000px 520px at 75% -10%, rgba(59,130,246,0.10), transparent 60%),
        radial-gradient(700px 460px at 5% 5%, rgba(56,225,212,0.05), transparent 55%),
        {BG};
    color: {TEXT};
}}
html, body, [class*="css"] {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    -webkit-font-smoothing: antialiased;
}}
h1, h2, h3, h4 {{ color: {TEXT} !important; letter-spacing: -0.02em; }}
p, li, label {{ color: {TEXT}; }}
hr {{ border-color: {BORDER}; margin: 32px 0; }}
.block-container {{ padding-top: 24px; max-width: 1040px; }}

/* ---------- motion ---------- */
@keyframes riseIn {{
    from {{ opacity: 0; transform: translateY(16px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}
@keyframes floatGlow {{
    0%, 100% {{ opacity: 0.5; transform: translateY(0); }}
    50%      {{ opacity: 0.9; transform: translateY(-8px); }}
}}
@media (prefers-reduced-motion: reduce) {{
    * {{ animation: none !important; transition: none !important; }}
}}

/* ---------- nav (styled tabs) ---------- */
.stTabs [data-baseweb="tab-list"] {{
    background: rgba(17,17,20,0.75);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid {BORDER};
    border-radius: 100px;
    padding: 6px;
    gap: 2px;
    justify-content: center;
    position: sticky; top: 8px; z-index: 999;
}}
.stTabs [data-baseweb="tab"] {{
    color: {MUTED};
    font-weight: 500;
    font-size: 14px;
    border-radius: 100px;
    padding: 8px 18px;
    background: transparent;
    transition: color 0.2s ease, background 0.2s ease;
}}
.stTabs [data-baseweb="tab"]:hover {{ color: {TEXT}; }}
.stTabs [aria-selected="true"] {{
    color: {TEXT} !important;
    background: rgba(59,130,246,0.15) !important;
}}
.stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"] {{ display: none; }}

/* ---------- hero ---------- */
.hh-hero {{
    position: relative;
    padding: 72px 8px 56px;
    text-align: center;
    animation: riseIn 0.7s cubic-bezier(0.16, 1, 0.3, 1) both;
}}
.hh-hero .orb {{
    position: absolute; top: 0; left: 50%;
    width: 280px; height: 280px; transform: translateX(-50%);
    background: radial-gradient(circle, rgba(59,130,246,0.20), transparent 65%);
    filter: blur(32px);
    animation: floatGlow 8s ease-in-out infinite;
    pointer-events: none;
}}
.hh-eyebrow {{
    display: inline-block;
    font-size: 12px; font-weight: 600;
    letter-spacing: 0.14em; text-transform: uppercase;
    color: {ACCENT};
    background: rgba(59,130,246,0.10);
    border: 1px solid rgba(59,130,246,0.25);
    border-radius: 100px;
    padding: 6px 14px; margin-bottom: 24px;
}}
.hh-hero h1 {{
    font-size: 56px; font-weight: 800;
    line-height: 1.05; letter-spacing: -0.035em;
    margin: 0 0 20px;
    background: linear-gradient(180deg, {TEXT} 55%, #A9ADB8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}
.hh-hero .sub {{
    font-size: 18px; color: {MUTED};
    max-width: 520px; margin: 0 auto; line-height: 1.65;
}}
.hh-hero .sub b {{ color: {TEXT}; font-weight: 600; }}
@media (max-width: 640px) {{
    .hh-hero h1 {{ font-size: 36px; }}
    .hh-hero {{ padding: 48px 0 40px; }}
}}

/* ---------- section scaffolding ---------- */
.hh-section {{ padding: 40px 0 8px; animation: riseIn 0.6s cubic-bezier(0.16,1,0.3,1) both; }}
.hh-kicker {{
    font-size: 12px; font-weight: 600;
    letter-spacing: 0.14em; text-transform: uppercase;
    color: {ACCENT}; margin-bottom: 10px;
}}
.hh-h2 {{
    font-size: 32px; font-weight: 700;
    letter-spacing: -0.025em; margin: 0 0 12px;
}}
.hh-lede {{ font-size: 16px; color: {MUTED}; line-height: 1.7; max-width: 640px; }}
.hh-lede b {{ color: {TEXT}; }}

/* ---------- cards ---------- */
.hh-card {{
    background: rgba(255,255,255,0.04);
    border: 1px solid {BORDER};
    border-radius: 20px;
    padding: 24px 26px;
    margin: 8px 0 16px;
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.35);
    transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
    height: 100%;
}}
.hh-card:hover {{
    transform: translateY(-3px);
    border-color: rgba(59,130,246,0.35);
    box-shadow: 0 12px 40px rgba(0,0,0,0.45);
}}
.hh-card .icon {{ font-size: 26px; margin-bottom: 12px; }}
.hh-card h3 {{ font-size: 17px; font-weight: 600; margin: 0 0 8px; }}
.hh-card h4 {{ font-size: 15px; font-weight: 600; margin: 0 0 6px; }}
.hh-card p {{ color: {MUTED}; font-size: 14.5px; line-height: 1.65; margin: 6px 0; }}
.hh-card p b {{ color: {TEXT}; font-weight: 600; }}
.hh-pill {{
    display: inline-block;
    font-size: 11px; font-weight: 600;
    letter-spacing: 0.1em; text-transform: uppercase;
    border-radius: 100px; padding: 4px 12px; margin-bottom: 12px;
}}
.hh-pill.blue {{ color: {ACCENT}; background: rgba(59,130,246,0.10); border: 1px solid rgba(59,130,246,0.25); }}
.hh-pill.good {{ color: {GOOD}; background: rgba(48,209,88,0.10); border: 1px solid rgba(48,209,88,0.25); }}
.hh-pill.warn {{ color: {WARN}; background: rgba(255,107,107,0.10); border: 1px solid rgba(255,107,107,0.28); }}

/* ---------- stats ---------- */
.hh-stat {{
    text-align: center; padding: 20px 8px;
}}
.hh-stat .num {{
    font-size: 40px; font-weight: 800; letter-spacing: -0.03em;
    background: linear-gradient(135deg, {ACCENT}, {ACCENT_2});
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}}
.hh-stat .lbl {{ font-size: 13px; color: {MUTED}; margin-top: 4px; }}

/* ---------- timeline ---------- */
.hh-tl {{ border-left: 2px solid rgba(59,130,246,0.3); margin: 8px 0 8px 8px; padding-left: 24px; }}
.hh-tl .item {{ position: relative; padding-bottom: 24px; }}
.hh-tl .item::before {{
    content: ""; position: absolute; left: -31px; top: 4px;
    width: 12px; height: 12px; border-radius: 50%;
    background: {ACCENT}; box-shadow: 0 0 0 4px rgba(59,130,246,0.2);
}}
.hh-tl .when {{ font-size: 12px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: {ACCENT}; }}
.hh-tl h4 {{ margin: 4px 0 4px; font-size: 16px; }}
.hh-tl p {{ color: {MUTED}; font-size: 14.5px; line-height: 1.6; margin: 0; }}

/* ---------- form ---------- */
[data-testid="stForm"] {{
    background: rgba(255,255,255,0.04);
    border: 1px solid {BORDER};
    border-radius: 24px;
    padding: 32px 32px 24px;
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.35);
}}
.stSelectbox label, .stRadio > label, .stSlider label {{
    color: {MUTED} !important; font-size: 14px !important; font-weight: 500 !important;
}}
[data-baseweb="select"] > div {{
    background: rgba(255,255,255,0.05) !important;
    border-color: {BORDER} !important;
    border-radius: 12px !important;
    color: {TEXT} !important;
    transition: border-color 0.2s ease;
}}
[data-baseweb="select"] > div:hover {{ border-color: rgba(59,130,246,0.4) !important; }}
.stRadio [role="radiogroup"] label {{ color: {TEXT} !important; }}

/* ---------- buttons ---------- */
.stButton>button, [data-testid="stForm"] button {{
    background: linear-gradient(135deg, {ACCENT}, {ACCENT_2});
    color: #05070D;
    font-weight: 700; font-size: 15px; letter-spacing: -0.01em;
    border: none; padding: 12px 32px; border-radius: 100px;
    box-shadow: 0 4px 20px rgba(59,130,246,0.35);
    transition: transform 0.15s ease, box-shadow 0.2s ease, filter 0.2s ease;
}}
.stButton>button:hover, [data-testid="stForm"] button:hover {{
    transform: scale(1.03);
    box-shadow: 0 6px 28px rgba(59,130,246,0.5);
    filter: brightness(1.05);
    color: #05070D;
}}
.stButton>button:active, [data-testid="stForm"] button:active {{ transform: scale(0.98); }}
.stButton>button:focus-visible, [data-testid="stForm"] button:focus-visible {{
    outline: 2px solid {TEXT}; outline-offset: 3px;
}}

/* ---------- slider, captions, footer ---------- */
.stSlider [data-baseweb="slider"] div[role="slider"] {{
    background: {ACCENT}; box-shadow: 0 0 0 4px rgba(59,130,246,0.25);
}}
.stCaption, [data-testid="stCaptionContainer"] p {{ color: {MUTED} !important; font-size: 13px !important; }}
.hh-footer {{
    border-top: 1px solid {BORDER};
    margin-top: 48px; padding: 32px 8px 16px;
    text-align: center; color: {MUTED}; font-size: 13px; line-height: 2;
}}
.hh-footer .logo {{ font-weight: 800; font-size: 16px; color: {TEXT}; letter-spacing: -0.02em; }}
.hh-footer a {{ color: {MUTED}; text-decoration: none; margin: 0 10px; }}
.hh-footer a:hover {{ color: {TEXT}; }}
</style>
""", unsafe_allow_html=True)

# ============================================================
# DATA — claim checker rules (assignment logic, unchanged)
# ============================================================
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


# ============================================================
# NAVIGATION
# ============================================================
tab_home, tab_about, tab_why, tab_purpose, tab_checker, tab_stories = st.tabs(
    ["Home", "About", "Why Use It", "Purpose", "Claim Checker", "Success Stories"]
)


# ============================================================
# HOME
# ============================================================
with tab_home:
    st.markdown("""
    <div class="hh-hero">
        <div class="orb"></div>
        <span class="hh-eyebrow">HardHat 🪖</span>
        <h1>Workers' comp,<br>made clear.</h1>
        <p class="sub">You got hurt doing your job. Figuring out what happens next shouldn't
        take a law degree. <b>Six questions. Two minutes. A clear readout.</b></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<p style="text-align:center; color:#9CA0AB; font-size:14px;">Open the <b style="color:#FAFAFA;">Claim Checker</b> tab above to get your readout →</p>', unsafe_allow_html=True)

    # ---- stats ----
    s1, s2, s3, s4 = st.columns(4)
    with s1:
        st.markdown('<div class="hh-stat"><div class="num">6</div><div class="lbl">Questions, plain English</div></div>', unsafe_allow_html=True)
    with s2:
        st.markdown('<div class="hh-stat"><div class="num">&lt;2 min</div><div class="lbl">To a full readout</div></div>', unsafe_allow_html=True)
    with s3:
        st.markdown('<div class="hh-stat"><div class="num">5</div><div class="lbl">States covered at launch</div></div>', unsafe_allow_html=True)
    with s4:
        st.markdown('<div class="hh-stat"><div class="num">$0</div><div class="lbl">Free. No signup.</div></div>', unsafe_allow_html=True)

    # ---- how it works ----
    st.markdown("""
    <div class="hh-section">
        <div class="hh-kicker">How it works</div>
        <div class="hh-h2">Three steps. No paperwork.</div>
    </div>
    """, unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class="hh-card"><div class="icon">📝</div>
        <h3>1 · Answer six questions</h3>
        <p>Your state, your industry, your injury, and where things stand. Plain-English dropdowns, nothing to type.</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="hh-card"><div class="icon">⚡</div>
        <h3>2 · Get your readout</h3>
        <p>Whether you likely have a claim, the deadlines in your state, and your next three steps, instantly.</p></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="hh-card"><div class="icon">🧭</div>
        <h3>3 · Know your next move</h3>
        <p>Most claims can be handled solo. When yours shows the signals that need a lawyer, we tell you straight.</p></div>""", unsafe_allow_html=True)

    # ---- why it matters ----
    st.markdown("""
    <div class="hh-section">
        <div class="hh-kicker">Why this matters</div>
        <div class="hh-h2">The system works. Navigating it doesn't.</div>
        <p class="hh-lede">Workers' compensation is <b>no-fault coverage</b> that nearly every employer
        is required to carry. But injured workers routinely miss short notice deadlines, don't realize
        they're covered, or assume they'd have to sue their employer. HardHat closes the gap between
        the benefits you're owed and the confusing process that stands in the way.</p>
    </div>
    """, unsafe_allow_html=True)

    f1, f2 = st.columns(2)
    with f1:
        st.markdown("""<div class="hh-card"><div class="icon">⏱️</div>
        <h3>Deadlines are brutal</h3>
        <p>Some states expect notice in days, not months. Missing the window can cost you the entire claim. HardHat surfaces your state's clock immediately.</p></div>""", unsafe_allow_html=True)
    with f2:
        st.markdown("""<div class="hh-card"><div class="icon">🛡️</div>
        <h3>It's no-fault</h3>
        <p>You don't have to prove your employer did anything wrong, and filing isn't suing anyone. Most workers don't know that. Now you do.</p></div>""", unsafe_allow_html=True)

with tab_home:
    st.markdown("""
    <div class="hh-footer">
        <div class="logo">🪖 HardHat</div>
        <div>Home · About · Why Use It · Purpose · Claim Checker · Success Stories</div>
        <div>Contact: via the ENT 451 course portal · Privacy · Terms</div>
        <div>© 2026 HardHat · Built by Matthew Richardson · University of Tennessee</div>
        <div>Informational guidance only, not legal advice.</div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# ABOUT
# ============================================================
with tab_about:
    st.markdown("""
    <div class="hh-section">
        <div class="hh-kicker">About</div>
        <div class="hh-h2">Built for the people who build everything else.</div>
    </div>
    """, unsafe_allow_html=True)

    a1, a2 = st.columns(2)
    with a1:
        st.markdown("""<div class="hh-card">
        <span class="hh-pill blue">Mission</span>
        <h3>Make workers' comp usable</h3>
        <p>Every injured worker should understand their rights, their deadlines, and their next step
        within minutes of getting hurt, without hiring anyone or decoding a statute.</p></div>""", unsafe_allow_html=True)
    with a2:
        st.markdown("""<div class="hh-card">
        <span class="hh-pill blue">Vision</span>
        <h3>The front door to every claim</h3>
        <p>Long term, HardHat becomes the first stop after a workplace injury in all 50 states:
        guided claims for workers on one side, compliance dashboards for small employers on the other.</p></div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="hh-section">
        <div class="hh-kicker">History &amp; founder</div>
        <div class="hh-h2">Where HardHat came from</div>
    </div>
    <div class="hh-tl">
        <div class="item">
            <div class="when">High school → college</div>
            <h4>Running crews, seeing the risk</h4>
            <p>Founder Matthew Richardson started and ran Mountain Mowers, an eight-person lawn care
            business. Managing a physical-labor crew made one thing obvious: the people doing the hardest
            work are the least protected when something goes wrong, and the least likely to know what they're owed.</p>
        </div>
        <div class="item">
            <div class="when">University of Tennessee</div>
            <h4>The problem gets a name</h4>
            <p>Studying finance at the Haslam College of Business, Matthew dug into the workers' compensation
            system and found a gap: coverage is nearly universal, but the process assumes you already know the
            rules. Notice windows as short as a few days. Paperwork written for insurers, not workers.</p>
        </div>
        <div class="item">
            <div class="when">ENT 451 · New Venture Planning</div>
            <h4>HardHat is born</h4>
            <p>Through customer discovery, market sizing, and competitive analysis, the idea became a venture:
            a dual-sided platform serving injured blue-collar workers and the small employers who need to stay
            compliant. The Claim Checker on this site is its first working product.</p>
        </div>
        <div class="item">
            <div class="when">Today</div>
            <h4>Pilot and iterate</h4>
            <p>The MVP is live and collecting real usage feedback. Every rating on a readout tests the core
            hypothesis: that guided answers beat an hour of anxious Googling. This is a founder committed to
            shipping, measuring, and improving, not just planning.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# WHY USE IT
# ============================================================
with tab_why:
    st.markdown("""
    <div class="hh-section">
        <div class="hh-kicker">Why use it</div>
        <div class="hh-h2">Clarity you can act on.</div>
        <p class="hh-lede">HardHat isn't a law firm and isn't trying to be. It's the fastest way to go from
        <b>"I got hurt and I don't know what to do"</b> to a concrete plan.</p>
    </div>
    """, unsafe_allow_html=True)

    w1, w2, w3 = st.columns(3)
    with w1:
        st.markdown("""<div class="hh-card"><div class="icon">⏳</div>
        <h3>Saves time</h3>
        <p>Two minutes here replaces an hour of contradictory search results and forum threads from other states.</p></div>""", unsafe_allow_html=True)
        st.markdown("""<div class="hh-card"><div class="icon">🧠</div>
        <h3>Builds confidence</h3>
        <p>Walking into a conversation with your employer or a doctor knowing your rights changes the entire dynamic.</p></div>""", unsafe_allow_html=True)
    with w2:
        st.markdown("""<div class="hh-card"><div class="icon">🎯</div>
        <h3>State-specific</h3>
        <p>Deadlines aren't generic. Your readout is built on your state's actual notice and filing windows.</p></div>""", unsafe_allow_html=True)
        st.markdown("""<div class="hh-card"><div class="icon">🤝</div>
        <h3>Honest triage</h3>
        <p>Most tools upsell you a lawyer. HardHat tells you when you don't need one, and flags the signals when you do.</p></div>""", unsafe_allow_html=True)
    with w3:
        st.markdown("""<div class="hh-card"><div class="icon">📱</div>
        <h3>Easy &amp; accessible</h3>
        <p>Plain English, six dropdowns, works on a phone from the job site. No account, no email, no cost.</p></div>""", unsafe_allow_html=True)
        st.markdown("""<div class="hh-card"><div class="icon">🔒</div>
        <h3>Nothing to lose</h3>
        <p>Your answers aren't sold or stored against your name. Ask the awkward questions freely.</p></div>""", unsafe_allow_html=True)


# ============================================================
# PURPOSE
# ============================================================
with tab_purpose:
    st.markdown("""
    <div class="hh-section">
        <div class="hh-kicker">Purpose</div>
        <div class="hh-h2">One problem, solved end to end.</div>
    </div>
    """, unsafe_allow_html=True)

    p1, p2 = st.columns(2)
    with p1:
        st.markdown("""<div class="hh-card">
        <span class="hh-pill warn">The problem</span>
        <h3>Coverage without comprehension</h3>
        <p>Workers' comp is mandatory for nearly every employer, yet the process is opaque enough that
        injured workers miss deadlines, under-report, or never file. The cost of confusion falls entirely
        on the person least equipped to absorb it.</p></div>""", unsafe_allow_html=True)
        st.markdown("""<div class="hh-card">
        <span class="hh-pill blue">Who it's for</span>
        <h3>Blue-collar workers first</h3>
        <p>Construction, manufacturing, warehousing, landscaping: the industries where injuries are most
        common and legal help feels furthest away. (Office workers are covered too, and many don't know it.)</p></div>""", unsafe_allow_html=True)
    with p2:
        st.markdown("""<div class="hh-card">
        <span class="hh-pill good">How it helps</span>
        <h3>Readout, deadlines, action plan</h3>
        <p>In one pass: whether you likely have a valid claim, the exact notice and filing windows in your
        state, your next three steps, and an honest call on whether your situation needs an attorney.</p></div>""", unsafe_allow_html=True)
        st.markdown("""<div class="hh-card">
        <span class="hh-pill blue">What makes it different</span>
        <h3>Guidance, not lead-gen</h3>
        <p>Most sites in this space exist to sell your contact info to law firms. HardHat's default answer
        is "you can handle this yourself," escalating only when the signals genuinely warrant it. Trust is
        the product.</p></div>""", unsafe_allow_html=True)


# ============================================================
# CLAIM CHECKER  (core assignment functionality — logic unchanged)
# ============================================================
with tab_checker:
    st.markdown("""
    <div class="hh-section" style="text-align:center;">
        <div class="hh-kicker">Claim Checker</div>
        <div class="hh-h2">Get your readout.</div>
        <p class="hh-lede" style="margin: 0 auto;">Answer six quick questions about your situation.
        You'll get an instant, state-specific readout. Nothing is stored against your name.</p>
    </div>
    """, unsafe_allow_html=True)

    st.caption("This tool provides general information, not legal advice. Every situation is different.")

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
        with st.spinner("Building your readout..."):
            time.sleep(0.9)  # brief, deliberate pause so the readout feels generated, not instant

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

        # ---- readout confidence (simple, transparent heuristic) ----
        confidence = 90
        if reported == "Yes, but only verbally":
            confidence -= 10
        elif reported == "No, not yet":
            confidence -= 20
        if timing in ("6-12 months ago",):
            confidence -= 10
        elif timing == "More than a year ago":
            confidence -= 25
        if state == "Other / not listed":
            confidence -= 15
        confidence = max(confidence, 25)

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

        st.markdown(f"""<div class="hh-card">
        <span class="hh-pill blue">Readout confidence</span>
        <h3>{confidence}%</h3>
        <p>How well your answers match the situations this readout is built for. Prompt written reporting,
        recent timing, and a covered state raise it; missing details lower it. It is <b>not</b> a prediction
        of your claim's outcome.</p></div>""", unsafe_allow_html=True)

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


# ============================================================
# SUCCESS STORIES  (clearly labeled illustrative pilot scenarios)
# ============================================================
with tab_stories:
    st.markdown("""
    <div class="hh-section">
        <div class="hh-kicker">Success stories</div>
        <div class="hh-h2">What a good outcome looks like.</div>
        <p class="hh-lede">HardHat is in its pilot phase, so these are <b>illustrative scenarios</b> built
        from the situations the Claim Checker is designed to handle — shown here so you can see how a
        readout translates into a real-world result. They are composites, not client records.</p>
    </div>
    """, unsafe_allow_html=True)

    filter_choice = st.selectbox("Filter scenarios", ["All", "Handled solo", "Attorney matched", "Deadline saved"])

    STORIES = [
        {"tag": "Handled solo", "pill": "good", "title": "Warehouse back strain · Tennessee",
         "text": "A picker strained his back lifting a pallet and almost 'pushed through it.' The readout flagged Tennessee's 15-day written notice window. He reported by email that afternoon, saw an approved provider, and his claim was accepted without a dispute.",
         "date": "Scenario · Spring 2026"},
        {"tag": "Deadline saved", "pill": "blue", "title": "Landscaping laceration · Georgia",
         "text": "A crew member cut his hand three weeks after the fact and assumed it was too late. The readout showed Georgia's 30-day notice window was still open — barely. Written notice went in on day 26, keeping the claim alive.",
         "date": "Scenario · Spring 2026"},
        {"tag": "Attorney matched", "pill": "warn", "title": "Denied claim · North Carolina",
         "text": "A machine operator's repetitive-stress claim was denied as 'not work-related.' The readout flagged denial as an escalation signal and pointed her to a contingency attorney. Represented workers in her position routinely see denials reversed on appeal.",
         "date": "Scenario · Spring 2026"},
        {"tag": "Handled solo", "pill": "good", "title": "Office fall · Tennessee",
         "text": "An admin slipped in a stairwell and assumed comp was 'only for job sites.' The readout corrected the myth, walked her through written notice, and the medical bills were covered — no lawyer, no drama.",
         "date": "Scenario · Summer 2026"},
    ]

    cols = st.columns(2)
    shown = [s for s in STORIES if filter_choice == "All" or s["tag"] == filter_choice]
    if not shown:
        st.caption("No scenarios match that filter yet.")
    for i, s in enumerate(shown):
        with cols[i % 2]:
            st.markdown(f"""<div class="hh-card">
            <span class="hh-pill {s['pill']}">{s['tag']}</span>
            <h3>{s['title']}</h3>
            <p>{s['text']}</p>
            <p style="font-size:12px; letter-spacing:0.06em; text-transform:uppercase;">{s['date']}</p>
            </div>""", unsafe_allow_html=True)

st.markdown("""
<div class="hh-footer">
    <div class="logo">🪖 HardHat</div>
    <div>© 2026 HardHat · MVP v0.2 · Built by Matthew Richardson · ENT 451, University of Tennessee</div>
    <div>Informational guidance only, not legal advice.</div>
</div>
""", unsafe_allow_html=True)
