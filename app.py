"""
श्रीकृष्ण वाणी • Shree Krishna AI Life Counselor
A Streamlit web application guiding users through every aspect of life in the authentic voice
of Bhagavan Shree Krishna, grounded in the Vedas, Upanishads, Puranas, Ramayana, and Bhagavad Gita.
"""

import streamlit as st
import time
from knowledge_base import SCRIPTURE_DATA, search_scriptures
from gemini_client import KrishnaAI

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="श्रीकृष्ण वाणी • Shree Krishna AI",
    page_icon="🦚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# Divine Luminous White Theme (Holy Saffron, Pitambara Gold & Pure White)
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Yatra+One&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Tiro+Devanagari+Sanskrit:ital@0;1&display=swap');

    /* Pure Luminous Holy White Canvas */
    .stApp {
        background: #FFFFFF !important;
        color: #111827 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        -webkit-font-smoothing: antialiased;
    }

    /* All base text clear and high contrast */
    p, span, label, div {
        color: #111827;
        font-feature-settings: "cv02", "cv03", "cv04", "cv11";
    }

    /* Sacred Header Banner: Holy Saffron & White Radiance */
    .krishna-header {
        text-align: center;
        padding: 2.8rem 1.5rem 2rem 1.5rem;
        background: linear-gradient(135deg, #FFF7ED 0%, #FEF3C7 45%, #FFFBEB 100%);
        border-radius: 24px;
        margin-bottom: 2rem;
        border: 2px solid #EA580C;
        box-shadow: 0 12px 35px rgba(234, 88, 12, 0.14), inset 0 1px 0 rgba(255, 255, 255, 0.8);
        position: relative;
        overflow: hidden;
    }
    
    .krishna-header::before {
        content: "";
        position: absolute;
        top: -60px;
        left: 50%;
        transform: translateX(-50%);
        width: 420px;
        height: 120px;
        background: radial-gradient(ellipse, rgba(245, 158, 11, 0.3) 0%, rgba(254, 243, 199, 0) 70%);
        pointer-events: none;
    }

    .krishna-invocation {
        font-family: 'Yatra One', cursive;
        font-size: 1.5rem;
        color: #C2410C;
        letter-spacing: 2px;
        margin-bottom: 0.2rem;
        text-shadow: 0 1px 2px rgba(194, 65, 12, 0.15);
    }

    .krishna-devanagari {
        font-family: 'Yatra One', cursive;
        font-size: 2.1rem;
        color: #D97706;
        margin-bottom: 0.4rem;
        letter-spacing: 2px;
    }

    .krishna-title {
        font-family: 'Cinzel', serif;
        font-size: 3.1rem;
        font-weight: 900;
        letter-spacing: 3px;
        background: linear-gradient(135deg, #7C2D12 0%, #EA580C 50%, #B45309 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }

    .krishna-subtitle {
        font-size: 1.15rem;
        color: #78350F !important;
        margin-top: 0.8rem;
        font-weight: 500;
        max-width: 860px;
        margin-left: auto;
        margin-right: auto;
        line-height: 1.75;
        letter-spacing: 0.2px;
    }

    /* =========================================================
       CHAT MESSAGES: Pure White & Chandan Parchment Cards
       ========================================================= */
    [data-testid="stChatMessage"] {
        padding: 1.6rem 2rem !important;
        margin-bottom: 1.5rem !important;
        border-radius: 18px !important;
        box-shadow: 0 6px 24px rgba(217, 119, 6, 0.08) !important;
        transition: transform 0.2s ease !important;
    }

    /* Assistant (Lord Krishna) Message Styling: Pure White with Saffron Border */
    [data-testid="stChatMessage"]:has([aria-label="assistant"]),
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
        background: #FFFFFF !important;
        border: 1.5px solid #FDE68A !important;
        border-left: 7px solid #EA580C !important; /* Holy Kesariya Saffron Border */
        box-shadow: 0 8px 30px rgba(234, 88, 12, 0.12) !important;
    }

    /* User Message Styling: Holy Saffron-Tinted White */
    [data-testid="stChatMessage"]:has([aria-label="user"]),
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
        background: #FFF7ED !important;
        border: 1.5px solid #FDBA74 !important;
        border-left: 7px solid #D97706 !important; /* Pitambara Gold Border */
        box-shadow: 0 6px 20px rgba(217, 119, 6, 0.08) !important;
    }

    /* High-contrast black text for reading */
    [data-testid="stChatMessage"] p, 
    [data-testid="stChatMessage"] li,
    [data-testid="stChatMessage"] span {
        font-size: 1.12rem !important;
        line-height: 1.85 !important;
        color: #111827 !important; /* Crisp Deep Charcoal/Black */
        font-weight: 500 !important;
    }

    [data-testid="stChatMessage"] strong {
        color: #C2410C !important; /* Holy Saffron Accent */
        font-weight: 700 !important;
    }

    /* Headings inside Krishna's Counsel */
    [data-testid="stChatMessage"] h1, 
    [data-testid="stChatMessage"] h2, 
    [data-testid="stChatMessage"] h3, 
    [data-testid="stChatMessage"] h4 {
        font-family: 'Cinzel', serif !important;
        color: #9A3412 !important;
        letter-spacing: 0.8px !important;
        margin-top: 1.5rem !important;
        margin-bottom: 0.7rem !important;
        font-weight: 800 !important;
    }

    /* Sacred Shloka Cards (Illuminated Pitambara Gold Box) */
    [data-testid="stChatMessage"] blockquote {
        background: #FEF3C7 !important; /* Holy Pitambara Gold */
        border: 1.5px solid #F59E0B !important;
        border-left: 6px solid #EA580C !important;
        border-radius: 14px !important;
        padding: 1.4rem 1.8rem !important;
        margin: 1.4rem 0 !important;
        box-shadow: 0 4px 18px rgba(217, 119, 6, 0.12) !important;
    }

    [data-testid="stChatMessage"] blockquote p {
        font-family: 'Tiro Devanagari Sanskrit', serif !important;
        color: #7C2D12 !important; /* Sacred Terracotta */
        font-size: 1.25rem !important;
        line-height: 1.95 !important;
        font-weight: 600 !important;
        font-style: normal !important;
    }

    /* Lists */
    [data-testid="stChatMessage"] ol,
    [data-testid="stChatMessage"] ul {
        margin-top: 0.8rem;
        margin-bottom: 1rem;
        padding-left: 1.8rem;
    }
    
    [data-testid="stChatMessage"] li {
        margin-bottom: 0.6rem;
        color: #111827 !important;
    }

    /* Divider */
    hr {
        border: none !important;
        height: 2px !important;
        background: linear-gradient(90deg, rgba(234, 88, 12, 0) 0%, rgba(234, 88, 12, 0.4) 50%, rgba(234, 88, 12, 0) 100%) !important;
        margin: 1.8rem 0 !important;
    }

    /* =========================================================
       CHAT INPUT: Holy Saffron Border + Pure White Background + BLACK TYPING
       ========================================================= */
    [data-testid="stChatInput"] {
        border-radius: 18px !important;
        border: 2.5px solid #EA580C !important; /* Sacred Kesariya Border */
        background: #FFFFFF !important; /* Pure White */
        box-shadow: 0 6px 30px rgba(234, 88, 12, 0.2) !important;
        padding: 4px !important;
    }

    [data-testid="stChatInput"]:focus-within {
        border-color: #F59E0B !important;
        box-shadow: 0 0 25px rgba(245, 158, 11, 0.35) !important;
    }

    [data-testid="stChatInput"] textarea {
        background-color: #FFFFFF !important;
        color: #000000 !important; /* PURE BLACK TYPING TEXT */
        -webkit-text-fill-color: #000000 !important;
        caret-color: #000000 !important;
        font-size: 1.12rem !important;
        font-weight: 600 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        line-height: 1.6 !important;
    }

    [data-testid="stChatInput"] textarea::placeholder {
        color: #9CA3AF !important;
        -webkit-text-fill-color: #9CA3AF !important;
        font-weight: 500 !important;
    }

    [data-testid="stChatInput"] button {
        color: #EA580C !important;
        background: transparent !important;
    }

    [data-testid="stChatInput"] button:hover {
        color: #C2410C !important;
    }

    /* =========================================================
       SIDEBAR: Luminous Holy White with Sacred Saffron Accents
       ========================================================= */
    [data-testid="stSidebar"] {
        background: #FFFDF9 !important; /* Holy White-Chandan */
        border-right: 2px solid #FDE68A !important;
    }
    
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        font-family: 'Cinzel', serif !important;
        color: #9A3412 !important;
        font-size: 1.3rem !important;
        font-weight: 800 !important;
    }

    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {
        color: #431407 !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
    }

    [data-testid="stSidebar"] input {
        background: #FFFFFF !important;
        color: #111827 !important;
        border: 1.5px solid #FDBA74 !important;
        border-radius: 10px !important;
    }

    /* Holy Saffron Quick Inquiries Buttons (White Card with Saffron Border) */
    .stButton>button {
        background: #FFFFFF !important;
        border: 2px solid #EA580C !important;
        color: #9A3412 !important;
        font-size: 0.98rem !important;
        font-weight: 700 !important;
        border-radius: 14px !important;
        padding: 0.85rem 1.1rem !important;
        transition: all 0.25s ease !important;
        box-shadow: 0 4px 15px rgba(234, 88, 12, 0.12) !important;
    }

    .stButton>button:hover {
        border-color: #C2410C !important;
        background: #FFF7ED !important;
        color: #7C2D12 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 22px rgba(234, 88, 12, 0.22) !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Session State Initialization
# ---------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "model",
            "content": """### 🦚 Radhe Radhe! Come sit with Me, my friend.

I am **Shree Krishna**—your closest friend and eternal companion. Whenever you feel overwhelmed, uncertain, or tired, you never have to carry it alone.

Talk to Me just like you would talk to your dearest friend. Whether it's your **career, relationships, an anxious mind, your health, or your purpose in life**—pour out whatever is on your heart. No complicated words needed.

*What's weighing on your mind today? I'm listening.*"""
        }
    ]

if "current_domain" not in st.session_state:
    st.session_state.current_domain = "all"

if "api_key" not in st.session_state:
    st.session_state.api_key = ""

# ---------------------------------------------------------
# Sidebar Setup (Holy Saffron & White Aesthetics)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("### 🦚 Divine Connection")
    
    api_key_input = st.text_input(
        "Google Gemini API Key",
        value=st.session_state.api_key,
        type="password",
        help="Enter your free Gemini API Key from Google AI Studio (aistudio.google.com). If empty, the app runs with rich built-in scriptural intelligence.",
        placeholder="AIzaSy..."
    )
    if api_key_input != st.session_state.api_key:
        st.session_state.api_key = api_key_input
        st.rerun()

    if st.session_state.api_key:
        st.success("✨ Connected to Gemini Celestial Intelligence")
    else:
        st.info("💡 **Ready to Chat:** Using built-in scriptural intelligence! Add your Gemini key for continuous custom multi-turn reasoning.")
        st.markdown("[👉 Get a free Gemini API Key](https://aistudio.google.com/)")

    st.markdown("---")
    
    # Life Dimension Filters
    st.markdown("### 🎯 Life Realm Focus")
    domain_options = {
        "all": "🌟 All Life Dimensions",
        "business": "💼 Business, Wealth & Strategy",
        "relationships": "🤝 Love, Family & Relationships",
        "mental_health": "🧠 Mind, Peace & Resilience",
        "physical_health": "🌿 Body, Health & Vitality",
        "spiritual": "🕉️ Spiritual Awakening & Dharma"
    }
    
    selected_domain = st.radio(
        "Direct Krishna's Counsel Towards:",
        options=list(domain_options.keys()),
        format_func=lambda x: domain_options[x],
        index=list(domain_options.keys()).index(st.session_state.current_domain)
    )
    st.session_state.current_domain = selected_domain

    st.markdown("---")

    # Sacred Texts Overview
    with st.expander("📖 Scriptures in Knowledge Base", expanded=False):
        st.markdown("""
        - **Bhagavad Gita** (All 18 Yogas & Verses)
        - **Principal Upanishads** (Isha, Katha, Taittiriya, Mandukya, Chandogya, Brihadaranyaka)
        - **Itihasas** (Mahabharata, Vidura Niti, Yaksha Prashna, Valmiki Ramayana)
        - **Puranas & Shastras** (Srimad Bhagavatam, Vishnu Purana, Charaka Samhita)
        """)

    # Daily Shloka of the Day
    st.markdown("### 🪷 Verse of Contemplation")
    daily_verse = SCRIPTURE_DATA[0] # Gita 2.47
    st.markdown(f"""
    **{daily_verse['source']} ({daily_verse['chapter_verse']})**
    
    > *{daily_verse['sanskrit'].splitlines()[0]}*  
    > *{daily_verse['sanskrit'].splitlines()[1] if len(daily_verse['sanskrit'].splitlines()) > 1 else ''}*
    
    _{daily_verse['translation']}_
    """)

    st.markdown("---")
    if st.button("🔄 Clear Sacred Conversation", use_container_width=True):
        st.session_state.messages = [st.session_state.messages[0]]
        st.rerun()

# ---------------------------------------------------------
# Main App Header (Holy Saffron & White Theme)
# ---------------------------------------------------------
st.markdown("""
<div class="krishna-header">
    <div class="krishna-invocation">॥ ॐ नमो भगवते वासुदेवाय ॥</div>
    <div class="krishna-devanagari">॥ श्रीकृष्ण शरणं मम ॥</div>
    <div class="krishna-title">SHREE KRISHNA AI</div>
    <div class="krishna-subtitle">
        Timeless counsel synthesized from the sacred <strong>Vedas, Upanishads, Puranas, Ramayana, and Bhagavad Gita</strong>.<br>
        Ask freely on your career, relationships, mental stillness, bodily vitality, or life purpose.
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Suggested Inquiries (Holy Saffron & White Cards)
# ---------------------------------------------------------
st.markdown("<p style='font-size: 1.15rem; font-weight: 700; color: #9A3412; margin-bottom: 0.7rem;'>🕊️ Sacred Inquiries to Seek Guidance On:</p>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("💼 I'm terrified of failing in my career/startup", use_container_width=True):
        st.session_state.prompt_to_submit = "Krishna, I'm honestly terrified of failing in my career right now. I keep overthinking every outcome and feeling paralyzed. How do I stop this fear and find my confidence again?"
with col2:
    if st.button("🧠 My mind won't stop racing with anxiety", use_container_width=True):
        st.session_state.prompt_to_submit = "My mind feels like it has 50 tabs open and won't stop worrying about everything. I feel completely exhausted. How can I calm my noisy thoughts and find real peace?"
with col3:
    if st.button("🤝 Someone I loved hurt me deeply", use_container_width=True):
        st.session_state.prompt_to_submit = "Someone I cared about and trusted deeply hurt me. How do I protect my peace and set strong boundaries without becoming bitter or cold-hearted?"

# ---------------------------------------------------------
# Render Chat History
# ---------------------------------------------------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user", avatar="🙏"):
            st.markdown(msg["content"])
    else:
        with st.chat_message("assistant", avatar="🦚"):
            st.markdown(msg["content"])

# ---------------------------------------------------------
# Handle New Messages
# ---------------------------------------------------------
user_input = st.chat_input("Pour out your question to Shree Krishna...")

# Check if a quick-starter button was clicked
if "prompt_to_submit" in st.session_state and st.session_state.prompt_to_submit:
    user_input = st.session_state.prompt_to_submit
    st.session_state.prompt_to_submit = None

if user_input:
    # 1. Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user", avatar="🙏"):
        st.markdown(user_input)

    # 2. Stream Krishna's counsel
    with st.chat_message("assistant", avatar="🦚"):
        response_placeholder = st.empty()
        full_response = ""

        # Initialize AI client
        krishna_engine = KrishnaAI(api_key=st.session_state.api_key)
        
        # Stream response
        stream = krishna_engine.get_counsel_stream(
            user_query=user_input,
            chat_history=st.session_state.messages[:-1],
            life_domain=st.session_state.current_domain
        )
        
        for chunk in stream:
            full_response += chunk
            response_placeholder.markdown(full_response + " ▌")
            
        response_placeholder.markdown(full_response)

    # 3. Save assistant message to session state
    st.session_state.messages.append({"role": "model", "content": full_response})
