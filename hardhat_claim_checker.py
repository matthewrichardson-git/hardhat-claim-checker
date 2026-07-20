import time
import streamlit as st

st.set_page_config(page_title="HardHat", page_icon="🪖", layout="wide")

# ============================================================
# HARDHAT — editorial edition
# Atmosphere: quiet, warm, publication-like. Serif display type,
# chaptered storytelling, museum whitespace, one restrained accent.
# Architecture: state-driven navigation, page functions, one router.
# Claim Checker logic (assignment functionality) is unchanged.
# ============================================================
PAPER = "#F7F5F1"      # warm off-white
CARD = "#FFFFFF"       # paper white for readout blocks
INK = "#161512"        # deep warm charcoal
MUTED = "#6E6A62"      # warm gray
FAINT = "#A5A199"      # lighter warm gray
RULE = "#DDD8CF"       # hairline
ACCENT = "#96442E"     # oxide — worn steel, quiet authority
GOOD = "#4F6B4A"       # moss
WARN = "#96442E"       # same oxide family; urgency through words, not color noise

PAGES = ["Home", "About", "Why It Exists", "Purpose", "Claim Checker", "Success Stories"]

if "nav" not in st.session_state:
    st.session_state.nav = "Home"


def go(page):
    st.session_state.nav = page


st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Sans:wght@400;500;600&display=swap');

/* ---------- foundation ---------- */
.stApp {{ background: {PAPER}; color: {INK}; }}
html, body, [class*="css"] {{
    font-family: 'IBM Plex Sans', -apple-system, sans-serif;
    -webkit-font-smoothing: antialiased;
}}
h1, h2, h3, h4 {{ color: {INK} !important; }}
p, li, label, span {{ color: {INK}; }}
hr {{ border-color: {RULE}; margin: 48px 0; }}
.block-container {{ padding-top: 5.25rem; max-width: 860px; }}
[data-testid="stHeader"] {{
    background: rgba(247,245,241,0.88);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
}}

/* ---------- motion ---------- */
@keyframes fadeUp {{
    from {{ opacity: 0; transform: translateY(14px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}
.reveal {{ animation: fadeUp 0.8s cubic-bezier(0.22,1,0.36,1) both; }}
@supports (animation-timeline: view()) {{
    .reveal {{
        animation: fadeUp linear both;
        animation-timeline: view();
        animation-range: entry 0% entry 45%;
    }}
}}
@media (prefers-reduced-motion: reduce) {{
    * {{ animation: none !important; transition: none !important; }}
}}

/* ---------- nav ---------- */
div[data-testid="stRadio"]:has(input[name*="nav"]) {{
    position: sticky; top: 4.1rem; z-index: 999;
    background: rgba(247,245,241,0.94);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-bottom: 1px solid {RULE};
    padding: 6px 0 0;
}}
div[data-testid="stRadio"] [role="radiogroup"] {{
    justify-content: center;
    gap: 6px;
    flex-wrap: wrap;
}}
div[data-testid="stRadio"] [role="radiogroup"] label {{
    padding: 8px 12px 10px;
    margin: 0;
    color: {MUTED} !important;
    font-size: 12px;
    font-weight: 500;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    border-bottom: 1px solid transparent;
    transition: color 0.2s ease, border-color 0.2s ease;
    cursor: pointer;
}}
div[data-testid="stRadio"] [role="radiogroup"] label:hover {{ color: {INK} !important; }}
div[data-testid="stRadio"] [role="radiogroup"] label:has(input:checked) {{
    color: {INK} !important;
    border-bottom: 1px solid {INK};
}}
div[data-testid="stRadio"] [role="radiogroup"] label > div:first-child {{ display: none; }}
div[data-testid="stRadio"] [role="radiogroup"] label p {{ color: inherit !important; letter-spacing: inherit; }}

/* ---------- editorial typography ---------- */
.serif, .chapter h2, .hero h1, .pull {{
    font-family: 'Cormorant Garamond', Georgia, serif;
}}
.hero {{
    padding: 150px 8px 110px;
    text-align: center;
}}
.hero .wordmark {{
    font-size: 13px; font-weight: 600;
    letter-spacing: 0.3em; text-transform: uppercase;
    color: {ACCENT}; margin-bottom: 34px;
}}
.hero h1 {{
    font-size: 76px; font-weight: 500;
    line-height: 1.06; letter-spacing: -0.01em;
    margin: 0 0 26px;
}}
.hero p {{
    font-size: 17px; color: {MUTED};
    max-width: 440px; margin: 0 auto; line-height: 1.75;
}}
.chapter {{
    padding: 120px 8px;
    max-width: 640px; margin: 0 auto;
    border-top: 1px solid {RULE};
}}
.chapter.first {{ border-top: none; }}
.chapter .no {{
    font-size: 12px; font-weight: 500;
    letter-spacing: 0.22em; text-transform: uppercase;
    color: {FAINT}; margin-bottom: 22px;
}}
.chapter .no span {{ color: {ACCENT}; }}
.chapter h2 {{
    font-size: 46px; font-weight: 500;
    line-height: 1.15; letter-spacing: -0.005em;
    margin: 0 0 22px;
}}
.chapter p {{
    font-size: 16.5px; color: {MUTED};
    line-height: 1.85; margin: 0 0 14px;
}}
.chapter p b {{ color: {INK}; font-weight: 600; }}
.chapter em {{ font-style: italic; }}
.pull {{
    font-size: 26px; font-style: italic; font-weight: 400;
    line-height: 1.5; color: {INK};
    border-left: 2px solid {ACCENT};
    padding-left: 24px; margin: 30px 0;
}}
@media (max-width: 640px) {{
    .hero h1 {{ font-size: 46px; }}
    .hero {{ padding: 80px 0 60px; }}
    .chapter {{ padding: 72px 0; }}
    .chapter h2 {{ font-size: 32px; }}
}}

/* ---------- inner-page headers ---------- */
.pagehead {{
    padding: 88px 8px 40px;
    max-width: 640px; margin: 0 auto;
}}
.pagehead .k {{
    font-size: 12px; font-weight: 500;
    letter-spacing: 0.22em; text-transform: uppercase;
    color: {ACCENT}; margin-bottom: 18px;
}}
.pagehead h2 {{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 48px; font-weight: 500;
    line-height: 1.12; margin: 0 0 20px;
}}
.pagehead p {{ font-size: 16.5px; color: {MUTED}; line-height: 1.8; margin: 0; }}

/* ---------- readout blocks ---------- */
.blk {{
    background: {CARD};
    border: 1px solid {RULE};
    border-radius: 4px;
    padding: 30px 34px;
    margin: 18px auto;
    max-width: 640px;
}}
.blk .label {{
    font-size: 11px; font-weight: 600;
    letter-spacing: 0.18em; text-transform: uppercase;
    margin-bottom: 12px;
}}
.blk .label.blue {{ color: {ACCENT}; }}
.blk .label.good {{ color: {GOOD}; }}
.blk .label.warn {{ color: {WARN}; }}
.blk .label.grey {{ color: {FAINT}; }}
.blk h3 {{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 27px; font-weight: 600;
    margin: 0 0 10px; line-height: 1.25;
}}
.blk p {{ color: {MUTED}; font-size: 15px; line-height: 1.8; margin: 8px 0; }}
.blk p b {{ color: {INK}; font-weight: 600; }}

/* editorial ledger rows (success stories, lists) */
.ledger {{ max-width: 640px; margin: 0 auto; }}
.ledger .entry {{
    border-top: 1px solid {RULE};
    padding: 34px 4px;
}}
.ledger .entry:last-child {{ border-bottom: 1px solid {RULE}; }}
.ledger .meta {{
    font-size: 11px; font-weight: 600;
    letter-spacing: 0.18em; text-transform: uppercase;
    color: {FAINT}; margin-bottom: 10px;
}}
.ledger h3 {{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 26px; font-weight: 600; margin: 0 0 8px;
}}
.ledger p {{ color: {MUTED}; font-size: 15px; line-height: 1.8; margin: 0; font-style: italic; }}

/* ---------- confidence bar ---------- */
.bar {{
    height: 3px; background: {RULE};
    overflow: hidden; margin: 14px 0 6px;
}}
.bar .fill {{ height: 100%; background: {INK}; }}

/* ---------- form ---------- */
[data-testid="stForm"] {{
    background: {CARD};
    border: 1px solid {RULE};
    border-radius: 4px;
    padding: 36px 36px 26px;
    max-width: 640px;
    margin: 0 auto;
}}
[data-testid="stForm"] h3 {{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 28px; font-weight: 600;
}}
.stSelectbox label, .stRadio > label, .stSlider label {{
    color: {MUTED} !important; font-size: 13px !important; font-weight: 500 !important;
    letter-spacing: 0.02em;
}}
[data-baseweb="select"] > div {{
    background: {PAPER} !important;
    border-color: {RULE} !important;
    border-radius: 3px !important;
    color: {INK} !important;
}}
[data-baseweb="select"] > div:hover {{ border-color: {INK} !important; }}
[data-baseweb="select"] * {{ color: {INK} !important; }}
div[data-baseweb="popover"] ul {{ background: {CARD} !important; }}
div[data-baseweb="popover"] li {{ color: {INK} !important; }}
div[data-baseweb="popover"] li:hover {{ background: {PAPER} !important; }}
.stRadio [role="radiogroup"] label {{ color: {INK} !important; }}

/* ---------- expanders ---------- */
[data-testid="stExpander"] {{
    border: none;
    border-top: 1px solid {RULE};
    border-radius: 0;
    background: transparent;
    max-width: 640px;
    margin: 0 auto;
}}
[data-testid="stExpander"] summary {{ font-weight: 500; color: {INK}; }}
[data-testid="stExpander"] summary:hover {{ color: {ACCENT} !important; }}

/* ---------- buttons ---------- */
.stButton>button, [data-testid="stForm"] button {{
    background: transparent;
    color: {INK};
    font-family: 'IBM Plex Sans', sans-serif;
    font-weight: 500; font-size: 13px;
    letter-spacing: 0.16em; text-transform: uppercase;
    border: 1px solid {INK};
    border-radius: 0;
    padding: 13px 34px;
    transition: background 0.25s ease, color 0.25s ease;
}}
.stButton>button:hover, [data-testid="stForm"] button:hover {{
    background: {INK};
    color: {PAPER};
    border-color: {INK};
}}
.stButton>button:focus-visible, [data-testid="stForm"] button:focus-visible {{
    outline: 2px solid {ACCENT}; outline-offset: 3px;
}}

/* ---------- slider, captions, footer ---------- */
.stSlider [data-baseweb="slider"] div[role="slider"] {{
    background: {INK}; box-shadow: 0 0 0 4px rgba(22,21,18,0.12);
}}
.stCaption, [data-testid="stCaptionContainer"] p {{
    color: {FAINT} !important; font-size: 12.5px !important;
    text-align: center;
}}
.footer {{
    border-top: 1px solid {RULE};
    margin-top: 90px; padding: 44px 8px 20px;
    text-align: center; color: {FAINT}; font-size: 12px;
    letter-spacing: 0.06em; line-height: 2.2;
}}
.footer .logo {{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-weight: 600; font-size: 20px; color: {INK};
    letter-spacing: 0.02em;
}}
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


def blk(label_class, label_text, title, body_html):
    st.markdown(f"""<div class="blk reveal">
    <div class="label {label_class}">{label_text}</div>
    <h3>{title}</h3>
    {body_html}</div>""", unsafe_allow_html=True)


def footer():
    st.markdown("""
    <div class="footer">
        <div class="logo">HardHat</div>
        <div>Home · About · Why It Exists · Purpose · Claim Checker · Success Stories</div>
        <div>© 2026 HardHat · Built by Matthew Richardson · ENT 451, University of Tennessee</div>
        <div>Informational guidance only, not legal advice.</div>
    </div>
    """, unsafe_allow_html=True)


def centered_button(label, target, key=None):
    _, mid, _ = st.columns([2, 1.4, 2])
    with mid:
        st.button(label, on_click=go, args=(target,), use_container_width=True, key=key)


# ============================================================
# NAVIGATION
# ============================================================
nav = st.radio("Navigation", PAGES, horizontal=True, label_visibility="collapsed", key="nav")


# ============================================================
# HOME — chapters, like a small publication
# ============================================================
def page_home():
    st.markdown("""
    <div class="hero reveal">
        <div class="wordmark">HardHat</div>
        <h1>Know where<br>you stand.</h1>
        <p>Clarity for the moments after a workplace injury — when it matters most.</p>
    </div>
    """, unsafe_allow_html=True)

    centered_button("Begin", "Claim Checker")

    st.markdown("""
    <div class="chapter first reveal">
        <div class="no"><span>01</span> — The uncertainty</div>
        <h2>The hardest part isn't the injury.</h2>
        <p>It's the hour after. Do I say something? Will it cause trouble? Can I afford the doctor?
        Almost every worker in America is covered by workers' compensation. Almost no one is taught how it works.</p>
    </div>

    <div class="chapter reveal">
        <div class="no"><span>02</span> — The cost of confusion</div>
        <h2>Silence has a deadline.</h2>
        <p>Some states expect written notice within days. Wait too long — out of politeness, out of toughness,
        out of not knowing — and a legitimate claim can quietly expire. The system doesn't punish dishonesty
        so much as it punishes hesitation.</p>
    </div>

    <div class="chapter reveal">
        <div class="no"><span>03</span> — The need for clarity</div>
        <h2>Knowing changes everything.</h2>
        <p>Workers' compensation is <b>no-fault</b>. Filing is not suing. Reporting is not betraying anyone.</p>
        <div class="pull">A worker who knows their rights has a different conversation — with their employer, with the doctor, with themselves.</div>
    </div>

    <div class="chapter reveal">
        <div class="no"><span>04</span> — The role of HardHat</div>
        <h2>A quiet guide, not a law firm.</h2>
        <p>HardHat asks six questions and returns one clear readout: whether you likely have a claim,
        the deadlines in your state, and your next three steps. When a situation genuinely calls for an
        attorney, it says so. Otherwise, it tells you the truth most services won't — <em>you can handle this yourself.</em></p>
    </div>

    <div class="chapter reveal">
        <div class="no"><span>05</span> — The Claim Checker</div>
        <h2>Two minutes. Then you'll know.</h2>
        <p>No account. No cost. Nothing stored against your name.</p>
    </div>
    """, unsafe_allow_html=True)

    centered_button("Check your claim", "Claim Checker", key="cta2")

    st.markdown("""
    <div class="chapter reveal">
        <div class="no"><span>06</span> — The stories</div>
        <h2>A page we intend to earn.</h2>
        <p>HardHat is in its pilot. Rather than invent testimonials, we've reserved the Success Stories
        page for verified outcomes from real users, published with their permission, as they happen.</p>
    </div>

    <div class="chapter reveal">
        <div class="no"><span>07</span> — The founder</div>
        <h2>Written by someone who ran a crew.</h2>
        <p>HardHat began with Mountain Mowers, an eight-person lawn care business its founder started in
        high school — and the realization that the people doing the hardest work are the least likely to
        know what they're owed. The full story is on the About page.</p>
    </div>
    """, unsafe_allow_html=True)

    footer()


# ============================================================
# ABOUT — a narrative, not a résumé
# ============================================================
def page_about():
    st.markdown("""
    <div class="pagehead reveal">
        <div class="k">About</div>
        <h2>Built for the people who build everything else.</h2>
        <p>HardHat exists so that every injured worker understands their rights, their deadlines,
        and their next step within minutes of getting hurt — without hiring anyone, and without
        decoding a statute.</p>
    </div>

    <div class="chapter first reveal" style="padding-top: 24px;">
        <div class="no"><span>I</span> — Where it began</div>
        <h2>A lawn crew in Tennessee.</h2>
        <p>Before university, founder Matthew Richardson started Mountain Mowers, a lawn care business
        that grew to eight people. Running a physical-labor crew teaches you things a classroom can't:
        that injuries are a matter of when, not if — and that the people doing the hardest work rarely
        know what protection they carry.</p>
    </div>

    <div class="chapter reveal">
        <div class="no"><span>II</span> — The problem gets a name</div>
        <h2>Coverage without comprehension.</h2>
        <p>Studying finance at the University of Tennessee's Haslam College of Business, Matthew examined
        the workers' compensation system and found its central flaw. Coverage is nearly universal.
        Understanding is not. Notice windows can be a few days long. The paperwork is written for insurers.</p>
        <div class="pull">A right you don't understand might as well not exist.</div>
    </div>

    <div class="chapter reveal">
        <div class="no"><span>III</span> — The venture</div>
        <h2>HardHat is born.</h2>
        <p>Through ENT 451 — customer discovery, market sizing, competitive analysis — the observation
        became a venture: guidance for injured workers on one side, compliance for the small employers
        who want to do right by them on the other. The Claim Checker on this site is its first working product.</p>
    </div>

    <div class="chapter reveal">
        <div class="no"><span>IV</span> — Today</div>
        <h2>Pilot, measure, improve.</h2>
        <p>The MVP is live and gathering real feedback. Every rating on a readout tests one hypothesis:
        that a guided answer beats an hour of anxious searching. The mission stays the same either way —
        make workers' comp usable, in all fifty states.</p>
    </div>
    """, unsafe_allow_html=True)
    footer()


# ============================================================
# WHY IT EXISTS
# ============================================================
def page_why():
    st.markdown("""
    <div class="pagehead reveal">
        <div class="k">Why it exists</div>
        <h2>Coverage without comprehension is a broken promise.</h2>
        <p>Workers' compensation is mandatory, no-fault insurance. It exists precisely for the moment
        you get hurt on the job. But a right you don't understand — with deadlines you've never heard
        of — might as well not exist. HardHat closes that gap.</p>
    </div>
    """, unsafe_allow_html=True)

    blk("warn", "The stakes", "Deadlines are brutal",
        "<p>Some states expect notice in days, not months. Missing the window can cost the entire claim, no matter how legitimate the injury.</p>")
    blk("blue", "The myth", "Filing is not suing",
        "<p>Comp is no-fault. You don't have to prove your employer did anything wrong, and reporting an injury is using coverage that already exists for you.</p>")

    st.markdown('<div class="pagehead reveal" style="padding: 40px 8px 16px;"><div class="k">Common questions</div></div>', unsafe_allow_html=True)
    with st.expander("Is this legal advice?"):
        st.write("No. HardHat provides general information about how workers' compensation works and what deadlines apply in your state. Complex situations deserve a real attorney — which is exactly what the readout will tell you when it applies.")
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
    <div class="pagehead reveal">
        <div class="k">Purpose</div>
        <h2>One problem, solved end to end.</h2>
    </div>
    """, unsafe_allow_html=True)

    blk("blue", "Who it's for", "Blue-collar workers first",
        "<p>Construction, manufacturing, warehousing, landscaping — the industries where injuries are most common and legal help feels furthest away. Office workers are covered too; many don't know it.</p>")
    blk("good", "What you get", "Readout, deadlines, action plan",
        "<p>In one pass: whether you likely have a valid claim, the notice and filing windows in your state, your next three steps, and an honest call on whether you need an attorney.</p>")
    blk("grey", "What makes it different", "Guidance, not lead generation",
        "<p>Most sites in this space exist to sell your contact information to law firms. HardHat's default answer is that you can handle it yourself. Trust is the product.</p>")

    st.markdown('<div style="height: 32px;"></div>', unsafe_allow_html=True)
    centered_button("Try the Claim Checker", "Claim Checker")
    footer()


# ============================================================
# CLAIM CHECKER — the centerpiece (assignment logic unchanged)
# ============================================================
def page_checker():
    st.markdown("""
    <div class="pagehead reveal" style="text-align:center; max-width: 560px;">
        <div class="k">The Claim Checker</div>
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
            time.sleep(0.9)  # a deliberate beat; the readout should feel considered

        rules = STATE_RULES[state]

        st.markdown("""
        <div class="pagehead reveal" style="text-align:center; padding: 48px 8px 8px; max-width: 560px;">
            <h2>Your readout.</h2>
        </div>
        """, unsafe_allow_html=True)

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
            blk("good", "Claim viability", "You likely have a valid claim",
                f"<p>Nearly every employer in {state if state != 'Other / not listed' else 'the U.S.'} is required to carry workers' compensation coverage. "
                f"An injury that happened at work or because of work is generally covered, including {injury.lower().split('(')[0].strip()} injuries. "
                f"You do <b>not</b> have to prove your employer did anything wrong. Comp is no-fault.</p>")
        else:
            blk("warn", "Claim viability", "Your window may be closing or closed",
                "<p>Based on the timing you selected, the standard filing deadline may have passed. There are exceptions — late discovery, employer misconduct, ongoing benefits — so don't assume it's over. Talk to someone.</p>")

        st.markdown(f"""<div class="blk reveal">
        <div class="label blue">Readout confidence</div>
        <h3>{confidence} percent</h3>
        <div class="bar"><div class="fill" style="width:{confidence}%;"></div></div>
        <p>How well your answers match the situations this readout is built for. Prompt written reporting,
        recent timing, and a covered state raise it; missing details lower it. It is <b>not</b> a prediction
        of your claim's outcome.</p></div>""", unsafe_allow_html=True)

        # ---- deadlines ----
        blk("blue", state, "Deadlines in your state", f"<p>{rules['note']}</p>")

        # ---- next 3 steps ----
        steps = []
        if reported != "Yes, in writing":
            steps.append("Report the injury to your employer in writing (text or email counts, keep a copy). Do this first, today.")
        steps.append("See a doctor and tell them clearly it's a work injury, so it enters the medical record that way. Your employer or their insurer may direct you to an approved provider.")
        steps.append("Write down what happened while it's fresh: date, time, place, witnesses, what you were doing. Photos help.")
        if len(steps) < 3:
            steps.append("Keep every document: medical bills, work restrictions, pay stubs showing missed time.")

        steps_html = "".join([f"<p><b>{i+1}.</b> {s}</p>" for i, s in enumerate(steps[:3])])
        blk("blue", "Action plan", "Your next three steps", steps_html)

        # ---- attorney trigger ----
        complex_flags = {"My claim was denied", "I think I'm being punished for reporting", "The injury looks permanent"}
        if status in complex_flags or not likely:
            blk("warn", "Representation advised", "Talk to an attorney. Seriously.",
                "<p>Your situation shows the signals — denial, retaliation, permanent injury, or deadline risk — where workers who get representation "
                "do meaningfully better. Workers' comp attorneys work on contingency: free consult, no fee unless you recover. "
                "In the full HardHat product, this is where we'd match you with a vetted attorney in your state.</p>")
        else:
            blk("good", "Our honest read", "You can likely handle this stage yourself",
                "<p>Straightforward, reported, recent claims usually don't need a lawyer. If your claim gets denied, payments stop, "
                "or your employer pushes back — that's when to get one. HardHat will be here for that moment.</p>")

        if caveats:
            caveats_html = "".join([f"<p>— {c}</p>" for c in caveats])
            blk("grey", "Worth knowing", "Before you go", caveats_html)

        st.markdown('<div style="height: 24px;"></div>', unsafe_allow_html=True)
        st.subheader("Was this useful?")
        st.slider("Rate this readout", 1, 5, 4)
        st.caption("In the pilot, this rating plus completion data tests whether guided readouts beat a Google search. Thank you for helping us find out.")


# ============================================================
# SUCCESS STORIES — honest: reserved, not invented
# ============================================================
def page_stories():
    st.markdown("""
    <div class="pagehead reveal">
        <div class="k">Success stories</div>
        <h2>This page is earned, not written.</h2>
        <p>HardHat is in its pilot phase. Rather than invent testimonials, we've reserved this space
        for real, verified outcomes — published with each user's permission, as they happen.</p>
    </div>

    <div class="ledger reveal">
        <div class="entry">
            <div class="meta">Reserved · No. 001</div>
            <h3>Your story could be here.</h3>
            <p>Used the Claim Checker and it helped? We'd like to hear how it went.</p>
        </div>
        <div class="entry">
            <div class="meta">Reserved · No. 002</div>
            <h3>A deadline saved.</h3>
            <p>For the first pilot user whose notice window was still open because they checked in time.</p>
        </div>
        <div class="entry">
            <div class="meta">Reserved · No. 003</div>
            <h3>A first accepted claim.</h3>
            <p>For the first pilot user who reported, filed, and had their claim accepted after a readout.</p>
        </div>
        <div class="entry">
            <div class="meta">Reserved · No. 004</div>
            <h3>The right call on representation.</h3>
            <p>For the first pilot user whose readout correctly flagged that their situation needed an attorney.</p>
        </div>
    </div>

    <div class="chapter reveal" style="border-top: none; padding: 72px 8px 40px; text-align: center; max-width: 560px;">
        <h2 style="font-size: 36px;">Help write this page.</h2>
        <p>Run the Claim Checker, rate your readout, and if it moved your situation forward — tell us.</p>
    </div>
    """, unsafe_allow_html=True)

    centered_button("Run the Claim Checker", "Claim Checker")
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
