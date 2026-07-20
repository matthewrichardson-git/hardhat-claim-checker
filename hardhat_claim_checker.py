import time
import streamlit as st

st.set_page_config(page_title="HardHat", page_icon="🪖", layout="wide")

# ============================================================
# HARDHAT
# Design direction: quiet, editorial, large type, few words.
# Architecture: state-driven navigation (real CTAs can navigate),
# reusable render functions, one source of truth for the checker logic.
# Assignment functionality (Claim Checker) is unchanged.
# ============================================================
BG = "#0A0A0C"
BORDER = "rgba(255,255,255,0.08)"
TEXT = "#F5F5F7"
MUTED = "#96989F"
FAINT = "#5F626B"
ACCENT = "#4A8CFF"
GOOD = "#34C77B"
WARN = "#F26D6D"

PAGES = ["Home", "About", "Why It Exists", "Purpose", "Claim Checker", "Success Stories"]

if "nav" not in st.session_state:
    st.session_state.nav = "Home"


def go(page):
    st.session_state.nav = page


# ---------- inline SVG icons (lucide-style strokes) ----------
def icon(name, color=ACCENT, size=20):
    paths = {
        "hardhat": '<path d="M2 18a1 1 0 0 0 1 1h18a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1H3a1 1 0 0 0-1 1v2z"/><path d="M10 10V5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v5"/><path d="M4 15v-3a6 6 0 0 1 6-6"/><path d="M14 6a6 6 0 0 1 6 6v3"/>',
        "clock": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
        "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
        "check": '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>',
        "alert": '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
        "clipboard": '<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1"/>',
        "briefcase": '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
        "trend": '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>',
    }
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
            f'stroke="{color}" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{paths[name]}</svg>')


st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* ---------- foundation ---------- */
.stApp {{ background: {BG}; color: {TEXT}; }}
html, body, [class*="css"] {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    -webkit-font-smoothing: antialiased;
}}
h1, h2, h3, h4 {{ color: {TEXT} !important; letter-spacing: -0.02em; }}
p, li, label {{ color: {TEXT}; }}
hr {{ border-color: {BORDER}; margin: 40px 0; }}
.block-container {{ padding-top: 5.25rem; max-width: 960px; }}
[data-testid="stHeader"] {{
    background: rgba(10,10,12,0.85);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
}}

/* ---------- motion ---------- */
@keyframes riseIn {{
    from {{ opacity: 0; transform: translateY(12px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}
.reveal {{ animation: riseIn 0.6s cubic-bezier(0.16,1,0.3,1) both; }}
/* scroll-driven reveal where the browser supports it (Chrome 115+) */
@supports (animation-timeline: view()) {{
    .reveal {{
        animation: riseIn linear both;
        animation-timeline: view();
        animation-range: entry 0% entry 40%;
    }}
}}
@media (prefers-reduced-motion: reduce) {{
    * {{ animation: none !important; transition: none !important; }}
}}

/* ---------- nav (state-driven radio styled as a nav bar) ---------- */
div[data-testid="stRadio"]:has(input[name*="nav"]) {{
    position: sticky; top: 4.25rem; z-index: 999;
}}
div[data-testid="stRadio"] [role="radiogroup"] {{
    background: rgba(16,16,19,0.92);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid {BORDER};
    border-radius: 12px;
    padding: 5px;
    gap: 2px;
    justify-content: center;
    flex-wrap: wrap;
}}
div[data-testid="stRadio"] [role="radiogroup"] label {{
    border-radius: 8px;
    padding: 7px 14px;
    margin: 0;
    color: {MUTED} !important;
    font-size: 14px;
    font-weight: 500;
    transition: color 0.15s ease, background 0.15s ease;
    cursor: pointer;
}}
div[data-testid="stRadio"] [role="radiogroup"] label:hover {{
    color: {TEXT} !important;
    background: rgba(255,255,255,0.04);
}}
div[data-testid="stRadio"] [role="radiogroup"] label:has(input:checked) {{
    color: {TEXT} !important;
    background: rgba(74,140,255,0.14);
}}
div[data-testid="stRadio"] [role="radiogroup"] label > div:first-child {{ display: none; }}
div[data-testid="stRadio"] [role="radiogroup"] label p {{ color: inherit !important; }}

/* ---------- editorial statements (homepage narrative) ---------- */
.stmt {{
    padding: 110px 8px;
    max-width: 760px;
    margin: 0 auto;
}}
.stmt.center {{ text-align: center; }}
.stmt .k {{
    font-size: 12px; font-weight: 600;
    letter-spacing: 0.16em; text-transform: uppercase;
    color: {FAINT}; margin-bottom: 18px;
}}
.stmt h2 {{
    font-size: 44px; font-weight: 700;
    line-height: 1.12; letter-spacing: -0.03em;
    margin: 0 0 18px;
}}
.stmt p {{
    font-size: 17px; color: {MUTED};
    line-height: 1.7; max-width: 560px; margin: 0;
}}
.stmt.center p {{ margin: 0 auto; }}
.stmt p b {{ color: {TEXT}; font-weight: 600; }}
.hero {{
    padding: 130px 8px 90px;
    text-align: center;
}}
.hero .mark {{ margin-bottom: 28px; }}
.hero h1 {{
    font-size: 64px; font-weight: 800;
    line-height: 1.04; letter-spacing: -0.04em;
    margin: 0 0 20px;
}}
.hero p {{
    font-size: 18px; color: {MUTED};
    max-width: 480px; margin: 0 auto; line-height: 1.65;
}}
@media (max-width: 640px) {{
    .hero h1 {{ font-size: 40px; }}
    .hero {{ padding: 72px 0 56px; }}
    .stmt {{ padding: 64px 0; }}
    .stmt h2 {{ font-size: 30px; }}
}}

/* quiet inline list used on the homepage */
.qlist {{ max-width: 560px; margin: 28px auto 0; text-align: left; }}
.qlist .row {{
    display: flex; gap: 16px; align-items: baseline;
    padding: 14px 0; border-bottom: 1px solid {BORDER};
}}
.qlist .row:last-child {{ border-bottom: none; }}
.qlist .n {{ color: {FAINT}; font-weight: 600; font-size: 14px; font-variant-numeric: tabular-nums; }}
.qlist .t {{ color: {TEXT}; font-size: 16px; }}
.qlist .t span {{ color: {MUTED}; }}

/* ---------- sections & cards (inner pages) ---------- */
.hh-section {{ padding: 44px 0 8px; }}
.hh-kicker {{
    font-size: 12px; font-weight: 600;
    letter-spacing: 0.14em; text-transform: uppercase;
    color: {ACCENT}; margin-bottom: 10px;
}}
.hh-h2 {{ font-size: 30px; font-weight: 700; letter-spacing: -0.025em; margin: 0 0 12px; }}
.hh-lede {{ font-size: 16px; color: {MUTED}; line-height: 1.7; max-width: 620px; }}
.hh-lede b {{ color: {TEXT}; }}

.hh-card {{
    background: rgba(255,255,255,0.025);
    border: 1px solid {BORDER};
    border-radius: 14px;
    padding: 22px 24px;
    margin: 8px 0 16px;
    transition: border-color 0.2s ease, background 0.2s ease;
    height: 100%;
}}
.hh-card:hover {{
    border-color: rgba(74,140,255,0.4);
    background: rgba(255,255,255,0.04);
}}
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
    min-height: 176px;
}}
.hh-pill {{
    display: inline-block;
    font-size: 11px; font-weight: 600;
    letter-spacing: 0.1em; text-transform: uppercase;
    border-radius: 6px; padding: 4px 10px; margin-bottom: 12px;
}}
.hh-pill.blue {{ color: {ACCENT}; border: 1px solid rgba(74,140,255,0.3); }}
.hh-pill.good {{ color: {GOOD}; border: 1px solid rgba(52,199,123,0.3); }}
.hh-pill.warn {{ color: {WARN}; border: 1px solid rgba(242,109,109,0.32); }}
.hh-pill.grey {{ color: {MUTED}; border: 1px solid {BORDER}; }}
.hh-rhead {{ display: flex; align-items: center; gap: 10px; margin: 0 0 8px; }}
.hh-rhead h3 {{ margin: 0; }}

/* ---------- timeline ---------- */
.hh-tl {{ border-left: 1px solid rgba(74,140,255,0.35); margin: 8px 0 8px 8px; padding-left: 26px; }}
.hh-tl .item {{ position: relative; padding-bottom: 28px; }}
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
    height: 5px; border-radius: 100px;
    background: rgba(255,255,255,0.08);
    overflow: hidden; margin: 12px 0 4px;
}}
.hh-bar .fill {{ height: 100%; border-radius: 100px; background: {ACCENT}; }}

/* ---------- form ---------- */
[data-testid="stForm"] {{
    background: rgba(255,255,255,0.025);
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
[data-baseweb="select"] > div:hover {{ border-color: rgba(74,140,255,0.45) !important; }}

/* ---------- expanders ---------- */
[data-testid="stExpander"] {{
    border: 1px solid {BORDER};
    border-radius: 12px;
    background: rgba(255,255,255,0.02);
    margin-bottom: 8px;
}}
[data-testid="stExpander"] summary:hover {{ color: {ACCENT} !important; }}

/* ---------- buttons ---------- */
.stButton>button, [data-testid="stForm"] button {{
    background: {TEXT};
    color: #0A0A0C;
    font-weight: 600; font-size: 15px; letter-spacing: -0.01em;
    border: none; padding: 12px 30px; border-radius: 100px;
    transition: transform 0.12s ease, box-shadow 0.2s ease, background 0.15s ease;
}}
.stButton>button:hover, [data-testid="stForm"] button:hover {{
    background: #FFFFFF;
    transform: translateY(-1px);
    box-shadow: 0 8px 24px rgba(255,255,255,0.12);
    color: #0A0A0C;
}}
.stButton>button:active, [data-testid="stForm"] button:active {{ transform: translateY(0); }}
.stButton>button:focus-visible, [data-testid="stForm"] button:focus-visible {{
    outline: 2px solid {ACCENT}; outline-offset: 3px;
}}

/* ---------- slider, captions, footer ---------- */
.stSlider [data-baseweb="slider"] div[role="slider"] {{
    background: {ACCENT}; box-shadow: 0 0 0 4px rgba(74,140,255,0.22);
}}
.stCaption, [data-testid="stCaptionContainer"] p {{ color: {FAINT} !important; font-size: 13px !important; }}
.hh-footer {{
    border-top: 1px solid {BORDER};
    margin-top: 64px; padding: 36px 8px 16px;
    text-align: center; color: {FAINT}; font-size: 13px; line-height: 2;
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
    st.markdown(f"""<div class="hh-card reveal">
    <span class="hh-pill {pill_class}">{pill_text}</span>
    <div class="hh-rhead">{icon(icon_name, icon_color)}<h3>{title}</h3></div>
    {body_html}</div>""", unsafe_allow_html=True)


def footer(extra=""):
    st.markdown(f"""
    <div class="hh-footer">
        <div class="logo">HardHat</div>
        {extra}
        <div>© 2026 HardHat · Built by Matthew Richardson · ENT 451, University of Tennessee</div>
        <div>Informational guidance only, not legal advice.</div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# NAVIGATION (state-driven, so buttons anywhere can navigate)
# ============================================================
nav = st.radio("Navigation", PAGES, horizontal=True, label_visibility="collapsed", key="nav")


# ============================================================
# HOME — a scrolled narrative, one idea per screen
# ============================================================
def page_home():
    st.markdown(f"""
    <div class="hero reveal">
        <div class="mark">{icon("hardhat", ACCENT, 40)}</div>
        <h1>You're already<br>covered.</h1>
        <p>Nearly every employer in America is required to carry workers' compensation. HardHat helps you use it.</p>
    </div>
    """, unsafe_allow_html=True)

    _, mid, _ = st.columns([2, 1, 2])
    with mid:
        st.button("Check your claim", on_click=go, args=("Claim Checker",), use_container_width=True)

    st.markdown("""
    <div class="stmt center reveal">
        <div class="k">The problem</div>
        <h2>The system assumes you already know the rules.</h2>
        <p>Notice windows as short as a few days. Paperwork written for insurers. Most injured workers don't miss out because they aren't covered. They miss out because nobody told them the clock was running.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="stmt center reveal">
        <div class="k">Why clarity matters</div>
        <h2>Knowing your rights changes the conversation.</h2>
        <p>With your employer. With the doctor. With yourself, at 11pm, wondering if reporting it will cause trouble. It won't. Comp is no-fault. Filing isn't suing anyone.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="stmt center reveal">
        <div class="k">How HardHat helps</div>
        <h2>Six questions. One readout.</h2>
        <div class="qlist">
            <div class="row"><div class="n">01</div><div class="t">Whether you likely have a claim <span>— in plain English</span></div></div>
            <div class="row"><div class="n">02</div><div class="t">The deadlines in your state <span>— before they pass</span></div></div>
            <div class="row"><div class="n">03</div><div class="t">Your next three steps <span>— and whether you need a lawyer</span></div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="stmt center reveal">
        <div class="k">Why trust it</div>
        <h2>Guidance, not lead generation.</h2>
        <p>No account. No cost. Your answers aren't sold to law firms. The default answer is <b>"you can handle this yourself"</b> — we escalate only when your situation genuinely calls for it.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="stmt center reveal">
        <h2>Two minutes.<br>Then you'll know.</h2>
    </div>
    """, unsafe_allow_html=True)

    _, mid2, _ = st.columns([2, 1, 2])
    with mid2:
        st.button("Open the Claim Checker", on_click=go, args=("Claim Checker",), use_container_width=True, key="cta2")

    footer("<div>Home · About · Why It Exists · Purpose · Claim Checker · Success Stories</div>")


# ============================================================
# ABOUT
# ============================================================
def page_about():
    st.markdown("""
    <div class="stmt reveal" style="padding: 72px 8px 40px;">
        <div class="k">About</div>
        <h2>Built for the people who build everything else.</h2>
        <p>HardHat exists so that every injured worker understands their rights, their deadlines, and their next step within minutes of getting hurt. Long term: the first stop after a workplace injury in all 50 states — guided claims for workers, compliance for the small employers who want to do right by them.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hh-section reveal">
        <div class="hh-kicker">The story</div>
    </div>
    <div class="hh-tl reveal">
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
            system and found the gap: coverage is nearly universal, but the process assumes you already know the rules.</p>
        </div>
        <div class="item">
            <div class="when">ENT 451 · New Venture Planning</div>
            <h4>HardHat is born</h4>
            <p>Customer discovery, market sizing, and competitive analysis turned the observation into a venture.
            The Claim Checker on this site is its first working product.</p>
        </div>
        <div class="item">
            <div class="when">Today</div>
            <h4>Pilot and iterate</h4>
            <p>The MVP is live and collecting real usage feedback. Every rating on a readout tests the core
            hypothesis: guided answers beat an hour of anxious Googling.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    footer()


# ============================================================
# WHY IT EXISTS
# ============================================================
def page_why():
    st.markdown("""
    <div class="stmt reveal" style="padding: 72px 8px 32px;">
        <div class="k">Why it exists</div>
        <h2>Coverage without comprehension is a broken promise.</h2>
        <p>Workers' compensation is mandatory, no-fault insurance. It exists precisely for the moment you get hurt on the job. But a right you don't understand — with deadlines you've never heard of — might as well not exist. HardHat exists to close that gap.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        card("warn", "The stakes", "clock", "Deadlines are brutal",
             "<p>Some states expect notice in days, not months. Missing the window can cost you the entire claim, no matter how legitimate the injury.</p>", WARN)
    with c2:
        card("blue", "The myth", "shield", "Filing is not suing",
             "<p>Comp is no-fault. You don't have to prove your employer did anything wrong, and reporting an injury is using coverage that already exists for you.</p>")

    st.markdown("""
    <div class="hh-section reveal">
        <div class="hh-kicker">Common questions</div>
    </div>
    """, unsafe_allow_html=True)
    with st.expander("Is this legal advice?"):
        st.write("No. HardHat provides general information about how workers' compensation works and what deadlines apply in your state. Complex situations deserve a real attorney, which is exactly what the readout will tell you when it applies.")
    with st.expander("What if I haven't reported my injury yet?"):
        st.write("Report it in writing as soon as possible. A text or email counts, and you should keep a copy. The readout will show you exactly where your state's clock stands.")
    with st.expander("What happens to my answers?"):
        st.write("Your answers generate your readout and an anonymous usefulness rating for the pilot. Nothing is stored against your name, and nothing is sold to law firms.")
    footer()


# ============================================================
# PURPOSE
# ============================================================
def page_purpose():
    st.markdown("""
    <div class="stmt reveal" style="padding: 72px 8px 32px;">
        <div class="k">Purpose</div>
        <h2>One problem, solved end to end.</h2>
    </div>
    """, unsafe_allow_html=True)

    p1, p2 = st.columns(2)
    with p1:
        card("blue", "Who it's for", "hardhat", "Blue-collar workers first",
             "<p>Construction, manufacturing, warehousing, landscaping: the industries where injuries are most common and legal help feels furthest away. Office workers are covered too — many don't know it.</p>")
    with p2:
        card("good", "What you get", "clipboard", "Readout, deadlines, action plan",
             "<p>In one pass: whether you likely have a valid claim, the notice and filing windows in your state, your next three steps, and an honest call on whether you need an attorney.</p>", GOOD)

    st.markdown("""
    <div class="stmt center reveal" style="padding: 56px 8px;">
        <h2>Trust is the product.</h2>
        <p>Most sites in this space exist to sell your contact info to law firms. HardHat's default answer is that you can handle it yourself.</p>
    </div>
    """, unsafe_allow_html=True)

    _, mid, _ = st.columns([2, 1, 2])
    with mid:
        st.button("Try the Claim Checker", on_click=go, args=("Claim Checker",), use_container_width=True)
    footer()


# ============================================================
# CLAIM CHECKER — the centerpiece (assignment logic unchanged)
# ============================================================
def page_checker():
    st.markdown("""
    <div class="stmt center reveal" style="padding: 64px 8px 24px;">
        <div class="k">Claim Checker</div>
        <h2>Get your readout.</h2>
        <p>Six questions. Instant, state-specific answers. Nothing stored against your name.</p>
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
        with st.spinner("Reading your state's rules..."):
            time.sleep(0.9)  # deliberate beat so the readout feels considered

        rules = STATE_RULES[state]

        st.markdown("---")
        st.header("Your readout")

        # ---- claim viability ----
        likely = True
        caveats = []
        if timing == "More than a year ago" and (rules["claim_years"] or 2) <= 1:
            likely = False
            caveats.append("Your filing window may already be closed, but exceptions exist. This is worth a free consult with an attorney.")
        if reported == "No, not yet":
            caveats.append("Not reporting yet doesn't kill your claim, but the clock is running. Report it in writing today.")
        if industry == "Office / other":
            caveats.append("Office injuries are absolutely covered too. Workers' comp isn't just for job sites.")

        # ---- readout confidence (transparent heuristic) ----
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

        st.markdown(f"""<div class="hh-card reveal">
        <span class="hh-pill blue">Readout confidence</span>
        <div class="hh-rhead">{icon("trend")}<h3>{confidence}%</h3></div>
        <div class="hh-bar"><div class="fill" style="width:{confidence}%;"></div></div>
        <p>How well your answers match the situations this readout is built for. Prompt written reporting,
        recent timing, and a covered state raise it; missing details lower it. It is <b>not</b> a prediction
        of your claim's outcome.</p></div>""", unsafe_allow_html=True)

        # ---- deadlines ----
        card("blue", state, "clock", "Deadlines in your state", f"<p>{rules['note']}</p>")

        # ---- next 3 steps ----
        steps = []
        if reported != "Yes, in writing":
            steps.append("Report the injury to your employer in writing (text or email counts, keep a copy). Do this first, today.")
        steps.append("See a doctor and tell them clearly it's a work injury, so it enters the medical record that way. Your employer or their insurer may direct you to an approved provider.")
        steps.append("Write down what happened while it's fresh: date, time, place, witnesses, what you were doing. Photos help.")
        if len(steps) < 3:
            steps.append("Keep every document: medical bills, work restrictions, pay stubs showing missed time.")

        steps_html = "".join([f"<p><b>{i+1}.</b> {s}</p>" for i, s in enumerate(steps[:3])])
        card("blue", "Action plan", "clipboard", "Your next 3 steps", steps_html)

        # ---- attorney trigger ----
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
        st.slider("Rate this readout", 1, 5, 4)
        st.caption("In the pilot, this rating plus completion data tests whether guided readouts beat a Google search. Thanks for helping us find out.")


# ============================================================
# SUCCESS STORIES — honest: pilot in progress, no invented claims
# ============================================================
def page_stories():
    st.markdown("""
    <div class="stmt reveal" style="padding: 72px 8px 32px;">
        <div class="k">Success stories</div>
        <h2>This page is earned, not written.</h2>
        <p>HardHat is in its pilot phase. Rather than invent testimonials, we're leaving this space open for the real ones. As pilot users complete readouts and report back, verified outcomes will appear here with their permission.</p>
    </div>
    """, unsafe_allow_html=True)

    g1, g2 = st.columns(2)
    ghosts = [
        (g1, "hardhat", "Your story could be here", "Used the Claim Checker and it helped? We'd like to hear how it went."),
        (g1, "clock", "Deadline saved", "Reserved for the first pilot user whose notice window was still open because they checked in time."),
        (g2, "check", "First accepted claim", "Reserved for the first pilot user who reported, filed, and had their claim accepted after a readout."),
        (g2, "briefcase", "Right call on representation", "Reserved for the first pilot user whose readout correctly flagged that their situation needed an attorney."),
    ]
    for col, ic, title, body in ghosts:
        with col:
            st.markdown(f"""<div class="hh-card ghost reveal">
            <div>{icon(ic, MUTED, 26)}</div>
            <h4 style="margin-top:12px;">{title}</h4>
            <p>{body}</p>
            <span class="hh-pill grey" style="margin: 8px auto 0;">Coming soon</span>
            </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="stmt center reveal" style="padding: 48px 8px;">
        <h2>Help write this page.</h2>
        <p>Run the Claim Checker, rate your readout, and if it moved your situation forward, tell us.</p>
    </div>
    """, unsafe_allow_html=True)

    _, mid, _ = st.columns([2, 1, 2])
    with mid:
        st.button("Run the Claim Checker", on_click=go, args=("Claim Checker",), use_container_width=True)
    footer()


# ============================================================
# ROUTER
# ============================================================
if nav == "Home":
    page_home()
elif nav == "About":
    page_about()
elif nav == "Why It Exists":
    page_why()
elif nav == "Purpose":
    page_purpose()
elif nav == "Claim Checker":
    page_checker()
    footer()
elif nav == "Success Stories":
    page_stories()
