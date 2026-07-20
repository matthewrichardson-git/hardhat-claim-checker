import time
import streamlit as st

st.set_page_config(page_title="HardHat — Workers' comp, made clear", page_icon="🪖", layout="wide")

# ============================================================
# HARDHAT — product site
# Pages: Home / About / Why Use It / Purpose / Claim Checker / Success Stories
# Claim Checker logic (assignment functionality) is unchanged.
# ============================================================
BG = "#09090B"
BORDER = "rgba(255,255,255,0.09)"
TEXT = "#FAFAFA"
MUTED = "#9BA0AC"
ACCENT = "#3B82F6"
GOOD = "#30D158"
WARN = "#FF6B6B"


# ---------- inline SVG icon set (lucide-style strokes, no emojis) ----------
def icon(name, color=ACCENT, size=22):
    paths = {
        "hardhat": '<path d="M2 18a1 1 0 0 0 1 1h18a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1H3a1 1 0 0 0-1 1v2z"/><path d="M10 10V5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v5"/><path d="M4 15v-3a6 6 0 0 1 6-6"/><path d="M14 6a6 6 0 0 1 6 6v3"/>',
        "clock": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
        "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
        "zap": '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>',
        "check": '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>',
        "alert": '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
        "clipboard": '<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1"/>',
        "compass": '<circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/>',
        "target": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
        "lock": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
        "phone": '<rect x="5" y="2" width="14" height="20" rx="2"/><line x1="12" y1="18" x2="12.01" y2="18"/>',
        "users": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
        "briefcase": '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
        "trend": '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>',
        "pin": '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
        "arrow": '<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>',
    }
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
            f'stroke="{color}" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{paths[name]}</svg>')


st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* ---------- foundation ---------- */
.stApp {{
    background:
        radial-gradient(900px 480px at 70% -14%, rgba(59,130,246,0.07), transparent 60%),
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

/* push content below Streamlit's fixed header so the nav is fully visible */
.block-container {{ padding-top: 5.5rem; max-width: 1040px; }}
[data-testid="stHeader"] {{
    background: rgba(9,9,11,0.85);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
}}

/* ---------- motion ---------- */
@keyframes riseIn {{
    from {{ opacity: 0; transform: translateY(14px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}
@media (prefers-reduced-motion: reduce) {{
    * {{ animation: none !important; transition: none !important; }}
}}

/* ---------- nav (styled tabs) ---------- */
.stTabs [data-baseweb="tab-list"] {{
    background: rgba(17,17,20,0.92);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid {BORDER};
    border-radius: 12px;
    padding: 6px;
    gap: 2px;
    justify-content: center;
    position: sticky;
    top: 4.25rem;              /* sits below Streamlit's header, never clipped */
    z-index: 999;
    margin-bottom: 8px;
}}
.stTabs [data-baseweb="tab"] {{
    color: {MUTED};
    font-weight: 500;
    font-size: 14px;
    border-radius: 8px;
    padding: 8px 16px;
    background: transparent;
    transition: color 0.15s ease, background 0.15s ease;
}}
.stTabs [data-baseweb="tab"]:hover {{ color: {TEXT}; background: rgba(255,255,255,0.04); }}
.stTabs [aria-selected="true"] {{
    color: {TEXT} !important;
    background: rgba(59,130,246,0.14) !important;
}}
.stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"] {{ display: none; }}

/* ---------- hero ---------- */
.hh-hero {{
    padding: 64px 8px 48px;
    text-align: center;
    animation: riseIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) both;
}}
.hh-hero .mark {{ margin-bottom: 20px; }}
.hh-eyebrow {{
    display: inline-block;
    font-size: 12px; font-weight: 600;
    letter-spacing: 0.14em; text-transform: uppercase;
    color: {ACCENT};
    border: 1px solid rgba(59,130,246,0.3);
    border-radius: 6px;
    padding: 5px 12px; margin-bottom: 22px;
}}
.hh-hero h1 {{
    font-size: 54px; font-weight: 800;
    line-height: 1.06; letter-spacing: -0.035em;
    margin: 0 0 18px;
}}
.hh-hero .sub {{
    font-size: 17px; color: {MUTED};
    max-width: 520px; margin: 0 auto; line-height: 1.65;
}}
.hh-hero .sub b {{ color: {TEXT}; font-weight: 600; }}
@media (max-width: 640px) {{
    .hh-hero h1 {{ font-size: 34px; }}
    .hh-hero {{ padding: 40px 0 32px; }}
}}

/* ---------- sections ---------- */
.hh-section {{ padding: 36px 0 8px; animation: riseIn 0.55s cubic-bezier(0.16,1,0.3,1) both; }}
.hh-kicker {{
    font-size: 12px; font-weight: 600;
    letter-spacing: 0.14em; text-transform: uppercase;
    color: {ACCENT}; margin-bottom: 10px;
}}
.hh-h2 {{ font-size: 30px; font-weight: 700; letter-spacing: -0.025em; margin: 0 0 12px; }}
.hh-lede {{ font-size: 16px; color: {MUTED}; line-height: 1.7; max-width: 640px; }}
.hh-lede b {{ color: {TEXT}; }}

/* ---------- cards ---------- */
.hh-card {{
    background: rgba(255,255,255,0.03);
    border: 1px solid {BORDER};
    border-radius: 14px;
    padding: 22px 24px;
    margin: 8px 0 16px;
    transition: transform 0.2s ease, border-color 0.2s ease, background 0.2s ease;
    height: 100%;
}}
.hh-card:hover {{
    transform: translateY(-2px);
    border-color: rgba(59,130,246,0.4);
    background: rgba(255,255,255,0.045);
}}
.hh-card .icon {{ margin-bottom: 14px; }}
.hh-card h3 {{ font-size: 17px; font-weight: 600; margin: 0 0 8px; }}
.hh-card h4 {{ font-size: 15px; font-weight: 600; margin: 0 0 6px; }}
.hh-card p {{ color: {MUTED}; font-size: 14.5px; line-height: 1.65; margin: 6px 0; }}
.hh-card p b {{ color: {TEXT}; font-weight: 600; }}
.hh-card.ghost {{
    border-style: dashed;
    border-color: rgba(255,255,255,0.14);
    background: transparent;
    text-align: center;
    display: flex; flex-direction: column; justify-content: center;
    min-height: 180px;
}}
.hh-card.ghost:hover {{ border-color: rgba(59,130,246,0.4); transform: none; }}
.hh-pill {{
    display: inline-block;
    font-size: 11px; font-weight: 600;
    letter-spacing: 0.1em; text-transform: uppercase;
    border-radius: 6px; padding: 4px 10px; margin-bottom: 12px;
}}
.hh-pill.blue {{ color: {ACCENT}; border: 1px solid rgba(59,130,246,0.3); }}
.hh-pill.good {{ color: {GOOD}; border: 1px solid rgba(48,209,88,0.3); }}
.hh-pill.warn {{ color: {WARN}; border: 1px solid rgba(255,107,107,0.32); }}
.hh-pill.grey {{ color: {MUTED}; border: 1px solid {BORDER}; }}

/* result card headers: icon + title on one line */
.hh-rhead {{ display: flex; align-items: center; gap: 10px; margin: 0 0 8px; }}
.hh-rhead h3 {{ margin: 0; }}

/* ---------- steps ---------- */
.hh-step {{ display: flex; gap: 16px; padding: 8px 0 20px; }}
.hh-step .n {{
    flex: none;
    width: 34px; height: 34px;
    border: 1px solid rgba(59,130,246,0.4);
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-weight: 700; font-size: 14px; color: {ACCENT};
    font-variant-numeric: tabular-nums;
}}
.hh-step h4 {{ margin: 4px 0 4px; font-size: 16px; }}
.hh-step p {{ color: {MUTED}; font-size: 14.5px; line-height: 1.6; margin: 0; }}

/* ---------- stats ---------- */
.hh-stat {{
    text-align: center; padding: 22px 8px;
    border: 1px solid {BORDER}; border-radius: 14px;
    background: rgba(255,255,255,0.02);
    transition: border-color 0.2s ease;
}}
.hh-stat:hover {{ border-color: rgba(59,130,246,0.35); }}
.hh-stat .num {{
    font-size: 36px; font-weight: 800; letter-spacing: -0.03em;
    color: {TEXT}; font-variant-numeric: tabular-nums;
}}
.hh-stat .lbl {{ font-size: 13px; color: {MUTED}; margin-top: 4px; }}

/* ---------- timeline ---------- */
.hh-tl {{ border-left: 1px solid rgba(59,130,246,0.35); margin: 8px 0 8px 8px; padding-left: 26px; }}
.hh-tl .item {{ position: relative; padding-bottom: 26px; }}
.hh-tl .item::before {{
    content: ""; position: absolute; left: -31px; top: 5px;
    width: 9px; height: 9px; border-radius: 50%;
    background: {BG}; border: 2px solid {ACCENT};
}}
.hh-tl .when {{ font-size: 12px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: {ACCENT}; }}
.hh-tl h4 {{ margin: 4px 0 4px; font-size: 16px; }}
.hh-tl p {{ color: {MUTED}; font-size: 14.5px; line-height: 1.6; margin: 0; }}

/* ---------- confidence bar ---------- */
.hh-bar {{
    height: 6px; border-radius: 100px;
    background: rgba(255,255,255,0.08);
    overflow: hidden; margin: 12px 0 4px;
}}
.hh-bar .fill {{
    height: 100%; border-radius: 100px;
    background: {ACCENT};
    transition: width 0.8s cubic-bezier(0.16,1,0.3,1);
}}

/* ---------- form ---------- */
[data-testid="stForm"] {{
    background: rgba(255,255,255,0.03);
    border: 1px solid {BORDER};
    border-radius: 16px;
    padding: 32px 32px 24px;
}}
.stSelectbox label, .stRadio > label, .stSlider label {{
    color: {MUTED} !important; font-size: 14px !important; font-weight: 500 !important;
}}
[data-baseweb="select"] > div {{
    background: rgba(255,255,255,0.04) !important;
    border-color: {BORDER} !important;
    border-radius: 10px !important;
    color: {TEXT} !important;
    transition: border-color 0.15s ease;
}}
[data-baseweb="select"] > div:hover {{ border-color: rgba(59,130,246,0.45) !important; }}
.stRadio [role="radiogroup"] label {{ color: {TEXT} !important; }}

/* ---------- expanders ---------- */
[data-testid="stExpander"] {{
    border: 1px solid {BORDER};
    border-radius: 12px;
    background: rgba(255,255,255,0.02);
    margin-bottom: 8px;
}}
[data-testid="stExpander"] summary {{ font-weight: 500; }}
[data-testid="stExpander"] summary:hover {{ color: {ACCENT} !important; }}

/* ---------- buttons ---------- */
.stButton>button, [data-testid="stForm"] button {{
    background: {ACCENT};
    color: #FFFFFF;
    font-weight: 600; font-size: 15px; letter-spacing: -0.01em;
    border: none; padding: 11px 28px; border-radius: 10px;
    transition: background 0.15s ease, transform 0.1s ease, box-shadow 0.2s ease;
}}
.stButton>button:hover, [data-testid="stForm"] button:hover {{
    background: #2F6FE0;
    transform: translateY(-1px);
    box-shadow: 0 6px 20px rgba(59,130,246,0.3);
    color: #FFFFFF;
}}
.stButton>button:active, [data-testid="stForm"] button:active {{ transform: translateY(0); }}
.stButton>button:focus-visible, [data-testid="stForm"] button:focus-visible {{
    outline: 2px solid {TEXT}; outline-offset: 3px;
}}

/* ---------- slider, captions, footer ---------- */
.stSlider [data-baseweb="slider"] div[role="slider"] {{
    background: {ACCENT}; box-shadow: 0 0 0 4px rgba(59,130,246,0.22);
}}
.stCaption, [data-testid="stCaptionContainer"] p {{ color: {MUTED} !important; font-size: 13px !important; }}
.hh-footer {{
    border-top: 1px solid {BORDER};
    margin-top: 48px; padding: 32px 8px 16px;
    text-align: center; color: {MUTED}; font-size: 13px; line-height: 2;
}}
.hh-footer .logo {{ font-weight: 700; font-size: 15px; color: {TEXT}; letter-spacing: -0.02em; }}
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


def card(pill_class, pill_text, icon_name, title, body_html, icon_color=ACCENT):
    st.markdown(f"""<div class="hh-card">
    <span class="hh-pill {pill_class}">{pill_text}</span>
    <div class="hh-rhead">{icon(icon_name, icon_color)}<h3>{title}</h3></div>
    {body_html}</div>""", unsafe_allow_html=True)


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
    st.markdown(f"""
    <div class="hh-hero">
        <div class="mark">{icon("hardhat", ACCENT, 40)}</div>
        <div><span class="hh-eyebrow">HardHat</span></div>
        <h1>Workers' comp,<br>made clear.</h1>
        <p class="sub">You got hurt doing your job. Figuring out what happens next shouldn't
        take a law degree. <b>Six questions. Two minutes. A clear readout.</b></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f'<p style="text-align:center; color:{MUTED}; font-size:14px;">Open the <b style="color:{TEXT};">Claim Checker</b> tab above to get your readout</p>', unsafe_allow_html=True)

    # ---- stats ----
    s1, s2, s3, s4 = st.columns(4)
    for col, num, lbl in [
        (s1, "6", "Questions, plain English"),
        (s2, "&lt;2 min", "To a full readout"),
        (s3, "5", "States covered at launch"),
        (s4, "$0", "Free. No signup."),
    ]:
        with col:
            st.markdown(f'<div class="hh-stat"><div class="num">{num}</div><div class="lbl">{lbl}</div></div>', unsafe_allow_html=True)

    # ---- how it works (a true sequence, so numbered) ----
    st.markdown("""
    <div class="hh-section">
        <div class="hh-kicker">How it works</div>
        <div class="hh-h2">Three steps. No paperwork.</div>
    </div>
    """, unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class="hh-step"><div class="n">1</div><div>
        <h4>Answer six questions</h4>
        <p>Your state, your industry, your injury, and where things stand. Plain-English dropdowns, nothing to type.</p></div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="hh-step"><div class="n">2</div><div>
        <h4>Get your readout</h4>
        <p>Whether you likely have a claim, the deadlines in your state, and your next three steps, instantly.</p></div></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="hh-step"><div class="n">3</div><div>
        <h4>Know your next move</h4>
        <p>Most claims can be handled solo. When yours shows the signals that need a lawyer, we tell you straight.</p></div></div>""", unsafe_allow_html=True)

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
        st.markdown(f"""<div class="hh-card"><div class="icon">{icon("clock")}</div>
        <h3>Deadlines are brutal</h3>
        <p>Some states expect notice in days, not months. Missing the window can cost you the entire claim. HardHat surfaces your state's clock immediately.</p></div>""", unsafe_allow_html=True)
    with f2:
        st.markdown(f"""<div class="hh-card"><div class="icon">{icon("shield")}</div>
        <h3>It's no-fault</h3>
        <p>You don't have to prove your employer did anything wrong, and filing isn't suing anyone. Most workers don't know that. Now you do.</p></div>""", unsafe_allow_html=True)

    # ---- FAQ (interactive) ----
    st.markdown("""
    <div class="hh-section">
        <div class="hh-kicker">Common questions</div>
        <div class="hh-h2">Before you ask.</div>
    </div>
    """, unsafe_allow_html=True)
    with st.expander("Is this legal advice?"):
        st.write("No. HardHat provides general information about how workers' compensation works and what deadlines apply in your state. Every situation is different, and complex situations deserve a real attorney, which is exactly what the readout will tell you when it applies.")
    with st.expander("Do I have to sue my employer to get workers' comp?"):
        st.write("No, and this is the biggest myth in the system. Workers' comp is no-fault insurance your employer is already required to carry. Filing a claim is using coverage that exists for you, not taking anyone to court.")
    with st.expander("What if I haven't reported my injury yet?"):
        st.write("Report it in writing as soon as possible. A text or email counts, and you should keep a copy. Notice windows in some states are as short as a few days, and the readout will show you exactly where your state's clock stands.")
    with st.expander("What happens to my answers?"):
        st.write("Your answers generate your readout and an anonymous usefulness rating for the pilot. Nothing is stored against your name, and nothing is sold to law firms.")

    st.markdown(f"""
    <div class="hh-footer">
        <div class="logo">HardHat</div>
        <div>Home · About · Why Use It · Purpose · Claim Checker · Success Stories</div>
        <div>Contact via the ENT 451 course portal · Privacy · Terms</div>
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
            <div class="when">High school to college</div>
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

    benefits = [
        ("clock", "Saves time", "Two minutes here replaces an hour of contradictory search results and forum threads from other states."),
        ("target", "State-specific", "Deadlines aren't generic. Your readout is built on your state's actual notice and filing windows."),
        ("phone", "Easy and accessible", "Plain English, six dropdowns, works on a phone from the job site. No account, no email, no cost."),
        ("trend", "Builds confidence", "Walking into a conversation with your employer or a doctor knowing your rights changes the entire dynamic."),
        ("users", "Honest triage", "Most tools upsell you a lawyer. HardHat tells you when you don't need one, and flags the signals when you do."),
        ("lock", "Nothing to lose", "Your answers aren't sold or stored against your name. Ask the awkward questions freely."),
    ]
    cols = st.columns(3)
    for i, (ic, title, body) in enumerate(benefits):
        with cols[i % 3]:
            st.markdown(f"""<div class="hh-card"><div class="icon">{icon(ic)}</div>
            <h3>{title}</h3><p>{body}</p></div>""", unsafe_allow_html=True)


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
        card("warn", "The problem", "alert", "Coverage without comprehension",
             "<p>Workers' comp is mandatory for nearly every employer, yet the process is opaque enough that injured workers miss deadlines, under-report, or never file. The cost of confusion falls entirely on the person least equipped to absorb it.</p>", WARN)
        card("blue", "Who it's for", "users", "Blue-collar workers first",
             "<p>Construction, manufacturing, warehousing, landscaping: the industries where injuries are most common and legal help feels furthest away. (Office workers are covered too, and many don't know it.)</p>")
    with p2:
        card("good", "How it helps", "compass", "Readout, deadlines, action plan",
             "<p>In one pass: whether you likely have a valid claim, the exact notice and filing windows in your state, your next three steps, and an honest call on whether your situation needs an attorney.</p>", GOOD)
        card("blue", "What makes it different", "shield", "Guidance, not lead-gen",
             "<p>Most sites in this space exist to sell your contact info to law firms. HardHat's default answer is \"you can handle this yourself,\" escalating only when the signals genuinely warrant it. Trust is the product.</p>")


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

        submitted = st.form_submit_button("Check my situation")

    if submitted:
        with st.spinner("Building your readout..."):
            time.sleep(0.9)  # deliberate beat so the readout feels generated

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
        if timing == "6-12 months ago":
            confidence -= 10
        elif timing == "More than a year ago":
            confidence -= 25
        if state == "Other / not listed":
            confidence -= 15
        confidence = max(confidence, 25)

        if likely:
            card("good", "Claim viability", "check", "You likely have a valid claim",
                 f"<p>Nearly every employer in {state if state != 'Other / not listed' else 'the U.S.'} is required to carry workers' compensation coverage. "
                 f"An injury that happened at work or because of work is generally covered, including {injury.lower().split('(')[0].strip()} injuries. "
                 f"You do <b>NOT</b> have to prove your employer did anything wrong. Comp is no-fault.</p>", GOOD)
        else:
            card("warn", "Claim viability", "alert", "Your window may be closing or closed",
                 "<p>Based on the timing you selected, the standard filing deadline may have passed. There are exceptions (late discovery, employer misconduct, ongoing benefits), so don't assume it's over. Talk to someone.</p>", WARN)

        st.markdown(f"""<div class="hh-card">
        <span class="hh-pill blue">Readout confidence</span>
        <div class="hh-rhead">{icon("trend")}<h3>{confidence}%</h3></div>
        <div class="hh-bar"><div class="fill" style="width:{confidence}%;"></div></div>
        <p>How well your answers match the situations this readout is built for. Prompt written reporting,
        recent timing, and a covered state raise it; missing details lower it. It is <b>not</b> a prediction
        of your claim's outcome.</p></div>""", unsafe_allow_html=True)

        # ---- 2. Deadlines ----
        card("blue", state, "clock", "Deadlines in your state", f"<p>{rules['note']}</p>")

        # ---- 3. Next 3 steps ----
        steps = []
        if reported != "Yes, in writing":
            steps.append("Report the injury to your employer in writing (text or email counts, keep a copy). Do this first, today.")
        steps.append("See a doctor and tell them clearly it's a work injury, so it enters the medical record that way. Your employer or their insurer may direct you to an approved provider.")
        steps.append("Write down what happened while it's fresh: date, time, place, witnesses, what you were doing. Photos help.")
        if len(steps) < 3:
            steps.append("Keep every document: medical bills, work restrictions, pay stubs showing missed time.")

        steps_html = "".join([f"<p><b>{i+1}.</b> {s}</p>" for i, s in enumerate(steps[:3])])
        card("blue", "Action plan", "clipboard", "Your next 3 steps", steps_html)

        # ---- 4. Attorney trigger ----
        complex_flags = {"My claim was denied", "I think I'm being punished for reporting", "The injury looks permanent"}
        if status in complex_flags or not likely:
            card("warn", "Representation advised", "briefcase", "Talk to an attorney. Seriously.",
                 "<p>Your situation shows the signals (denial, retaliation, permanent injury, or deadline risk) where workers who get representation "
                 "do meaningfully better. Workers' comp attorneys work on contingency: free consult, no fee unless you recover. "
                 "In the full HardHat product, this is where we'd match you with a vetted attorney in your state.</p>", WARN)
        else:
            card("good", "You've got this", "shield", "You can likely handle this stage yourself",
                 "<p>Straightforward, reported, recent claims usually don't need a lawyer. If your claim gets denied, payments stop, "
                 "or your employer pushes back, that's when to get one. HardHat will be here for that moment.</p>", GOOD)

        if caveats:
            st.markdown("**Worth knowing:**")
            for c in caveats:
                st.markdown(f"- {c}")

        st.markdown("---")
        st.subheader("Was this useful?")
        rating = st.slider("Rate this readout", 1, 5, 4)
        st.caption("In the pilot, this rating plus completion data tests whether guided readouts beat a Google search. Thanks for helping us find out.")


# ============================================================
# SUCCESS STORIES  (honest: pilot in progress, no invented claims)
# ============================================================
with tab_stories:
    st.markdown("""
    <div class="hh-section">
        <div class="hh-kicker">Success stories</div>
        <div class="hh-h2">This page is earned, not written.</div>
        <p class="hh-lede">HardHat is in its pilot phase. Rather than invent testimonials, we're leaving this
        space open for the real ones. As pilot users complete readouts and report back, verified outcomes
        will appear here with their permission.</p>
    </div>
    """, unsafe_allow_html=True)

    g1, g2 = st.columns(2)
    with g1:
        st.markdown(f"""<div class="hh-card ghost">
        <div>{icon("hardhat", MUTED, 28)}</div>
        <h4 style="margin-top:12px;">Your story could be here</h4>
        <p>Used the Claim Checker and it helped? We'd like to hear how it went.</p>
        <span class="hh-pill grey" style="margin: 8px auto 0;">Coming soon</span>
        </div>""", unsafe_allow_html=True)
        st.markdown(f"""<div class="hh-card ghost">
        <div>{icon("clock", MUTED, 28)}</div>
        <h4 style="margin-top:12px;">Deadline saved</h4>
        <p>Reserved for the first pilot user whose notice window was still open because they checked in time.</p>
        <span class="hh-pill grey" style="margin: 8px auto 0;">Coming soon</span>
        </div>""", unsafe_allow_html=True)
    with g2:
        st.markdown(f"""<div class="hh-card ghost">
        <div>{icon("check", MUTED, 28)}</div>
        <h4 style="margin-top:12px;">First accepted claim</h4>
        <p>Reserved for the first pilot user who reported, filed, and had their claim accepted after a readout.</p>
        <span class="hh-pill grey" style="margin: 8px auto 0;">Coming soon</span>
        </div>""", unsafe_allow_html=True)
        st.markdown(f"""<div class="hh-card ghost">
        <div>{icon("briefcase", MUTED, 28)}</div>
        <h4 style="margin-top:12px;">Right call on representation</h4>
        <p>Reserved for the first pilot user whose readout correctly flagged that their situation needed an attorney.</p>
        <span class="hh-pill grey" style="margin: 8px auto 0;">Coming soon</span>
        </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="hh-section">
        <div class="hh-kicker">In the meantime</div>
        <div class="hh-h2">Help write this page.</div>
        <p class="hh-lede">Run the Claim Checker, rate your readout, and if it moved your situation forward,
        tell us. The pilot's entire purpose is finding out whether guided answers beat an hour of Googling,
        and this page is where the evidence will live.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="hh-footer">
    <div class="logo">HardHat</div>
    <div>© 2026 HardHat · MVP v0.3 · Built by Matthew Richardson · ENT 451, University of Tennessee</div>
    <div>Informational guidance only, not legal advice.</div>
</div>
""", unsafe_allow_html=True)
