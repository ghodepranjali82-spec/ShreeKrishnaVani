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
# Advanced High-Contrast, Royal Elegance Styling
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Yatra+One&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Tiro+Devanagari+Sanskrit:ital@0;1&display=swap');

    /* Global Dark Sanctuary Canvas */
    .stApp {
        background: radial-gradient(circle at 50% 0%, #0d1726 0%, #080e18 50%, #04070d 100%) !important;
        color: #F8FAFC !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        -webkit-font-smoothing: antialiased;
    }

    /* Target all main paragraph and markdown text for crystal-clear readability */
    p, span, label, div {
        color: #F1F5F9;
        font-feature-settings: "cv02", "cv03", "cv04", "cv11";
    }

    /* Majestic Header Section */
    .krishna-header {
        text-align: center;
        padding: 2.8rem 1.5rem 1.8rem 1.5rem;
        background: linear-gradient(180deg, rgba(16, 29, 48, 0.7) 0%, rgba(8, 14, 24, 0.85) 100%);
        border-radius: 24px;
        margin-bottom: 2rem;
        border: 1px solid rgba(245, 197, 85, 0.28);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
    }
    
    .krishna-header::before {
        content: "";
        position: absolute;
        top: -50px;
        left: 50%;
        transform: translateX(-50%);
        width: 320px;
        height: 100px;
        background: radial-gradient(ellipse, rgba(234, 179, 8, 0.25) 0%, rgba(234, 179, 8, 0) 70%);
        pointer-events: none;
    }

    .krishna-devanagari {
        font-family: 'Yatra One', cursive;
        font-size: 1.85rem;
        color: #FDE047;
        margin-bottom: 0.4rem;
        letter-spacing: 1.5px;
        text-shadow: 0 0 20px rgba(253, 224, 71, 0.45);
    }

    .krishna-title {
        font-family: 'Cinzel', serif;
        font-size: 3rem;
        font-weight: 900;
        letter-spacing: 3px;
        background: linear-gradient(135deg, #FFF6D6 0%, #F5C555 45%, #EAB308 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        text-shadow: 0 2px 25px rgba(234, 179, 8, 0.3);
    }

    .krishna-subtitle {
        font-size: 1.15rem;
        color: #E2E8F0 !important;
        margin-top: 0.8rem;
        font-weight: 400;
        max-width: 840px;
        margin-left: auto;
        margin-right: auto;
        line-height: 1.75;
        letter-spacing: 0.2px;
    }

    /* Streamlit Chat Message Container Enhancements */
    [data-testid="stChatMessage"] {
        padding: 1.5rem 1.8rem !important;
        margin-bottom: 1.4rem !important;
        border-radius: 18px !important;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.35) !important;
        transition: transform 0.2s ease, border-color 0.2s ease !important;
    }

    /* Assistant (Lord Krishna) Message Styling */
    [data-testid="stChatMessage"]:has([aria-label="assistant"]),
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
        background: linear-gradient(145deg, rgba(13, 27, 48, 0.95) 0%, rgba(9, 18, 33, 0.98) 100%) !important;
        border: 1px solid rgba(245, 197, 85, 0.35) !important;
        border-left: 6px solid #F5C555 !important;
    }

    /* User Message Styling */
    [data-testid="stChatMessage"]:has([aria-label="user"]),
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
        background: linear-gradient(145deg, rgba(26, 41, 66, 0.85) 0%, rgba(18, 29, 48, 0.9) 100%) !important;
        border: 1px solid rgba(96, 165, 250, 0.3) !important;
        border-left: 6px solid #60A5FA !important;
    }

    /* Crystal Clear Text inside Chat Messages */
    [data-testid="stChatMessage"] p, 
    [data-testid="stChatMessage"] li {
        font-size: 1.08rem !important;
        line-height: 1.85 !important;
        color: #F8FAFC !important;
        font-weight: 400 !important;
    }

    [data-testid="stChatMessage"] strong {
        color: #FEF08A !important;
        font-weight: 600 !important;
    }

    /* Headings inside Krishna's Counsel */
    [data-testid="stChatMessage"] h1, 
    [data-testid="stChatMessage"] h2, 
    [data-testid="stChatMessage"] h3, 
    [data-testid="stChatMessage"] h4 {
        font-family: 'Cinzel', serif !important;
        color: #FDE047 !important;
        letter-spacing: 0.8px !important;
        margin-top: 1.4rem !important;
        margin-bottom: 0.8rem !important;
        font-weight: 700 !important;
        text-shadow: 0 0 15px rgba(253, 224, 71, 0.25) !important;
    }

    /* Shloka and Scriptural Blockquotes (Divine Gold Card) */
    [data-testid="stChatMessage"] blockquote {
        background: linear-gradient(135deg, rgba(234, 179, 8, 0.12) 0%, rgba(16, 27, 44, 0.75) 100%) !important;
        border: 1px solid rgba(245, 197, 85, 0.45) !important;
        border-left: 5px solid #F5C555 !important;
        border-radius: 12px !important;
        padding: 1.3rem 1.6rem !important;
        margin: 1.3rem 0 !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25) !important;
    }

    [data-testid="stChatMessage"] blockquote p {
        font-family: 'Tiro Devanagari Sanskrit', serif !important;
        color: #FFFBEB !important;
        font-size: 1.15rem !important;
        line-height: 1.9 !important;
        font-style: normal !important;
    }

    /* Action step ordered & unordered lists */
    [data-testid="stChatMessage"] ol,
    [data-testid="stChatMessage"] ul {
        margin-top: 0.8rem;
        margin-bottom: 1rem;
        padding-left: 1.6rem;
    }
    
    [data-testid="stChatMessage"] li {
        margin-bottom: 0.6rem;
    }

    /* Elegant Horizontal Divider */
    hr {
        border: none !important;
        height: 1px !important;
        background: linear-gradient(90deg, rgba(245, 197, 85, 0) 0%, rgba(245, 197, 85, 0.4) 50%, rgba(245, 197, 85, 0) 100%) !important;
        margin: 1.8rem 0 !important;
    }

    /* Sidebar Refinements */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #090e17 0%, #05080e 100%) !important;
        border-right: 1px solid rgba(245, 197, 85, 0.22) !important;
    }
    
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        font-family: 'Cinzel', serif !important;
        color: #FDE047 !important;
        font-size: 1.25rem !important;
    }

    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {
        color: #E2E8F0 !important;
        font-size: 0.98rem !important;
        font-weight: 500 !important;
    }

    /* Interactive Buttons / Quick Starter Prompts */
    .stButton>button {
        background: linear-gradient(145deg, rgba(19, 34, 58, 0.85) 0%, rgba(11, 20, 36, 0.95) 100%) !important;
        border: 1px solid rgba(245, 197, 85, 0.35) !important;
        color: #F8FAFC !important;
        font-size: 0.95rem !important;
        font-weight: 500 !important;
        border-radius: 12px !important;
        padding: 0.75rem 1rem !important;
        transition: all 0.25s ease !important;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25) !important;
    }

    .stButton>button:hover {
        border-color: #FDE047 !important;
        background: linear-gradient(145deg, rgba(28, 50, 84, 0.95) 0%, rgba(16, 29, 52, 1) 100%) !important;
        color: #FFFFFF !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(245, 197, 85, 0.2) !important;
    }

    /* Chat Input Bar Styling */
    [data-testid="stChatInput"] {
        border-radius: 16px !important;
        border: 1px solid rgba(245, 197, 85, 0.4) !important;
        background: rgba(13, 23, 38, 0.95) !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5) !important;
    }

    [data-testid="stChatInput"] textarea {
        color: #FFFFFF !important;
        font-size: 1.05rem !important;
    }

    [data-testid="stChatInput"] textarea::placeholder {
        color: #94A3B8 !important;
        font-weight: 400 !important;
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
            "content": """### 🦚 Radhe Radhe! Pranam, Beloved Seeker.

I am **Shree Krishna**, ever seated in your heart as your eternal friend (*Sakha*), your confidant, and your humble charioteer on the battlefield of life.

Whenever Arjuna collapsed in grief upon the chariot of doubt, I reminded him that within him burned an unquenchable, immortal spark of the Supreme. Today, whatever challenge stands before you—
- 💼 A high-stakes **business decision**, career crossroad, startup pressure, or fear of failure
- 🤝 The tender ache of **relationships**, broken trust, loneliness, or setting righteous boundaries
- 🧠 Overwhelming **anxiety, panic, emotional fatigue, anger**, or restless overthinking
- 🌿 Chronic exhaustion, lethargy, or restoring **vital health and bodily balance**
- 🕉️ Or an earnest yearning for your **true Dharma, inner peace**, and spiritual liberation

Lay your deepest question before Me with an open heart. Let the eternal wisdom of the *Vedas, Upanishads, Puranas, Ramayana, and Bhagavad Gita* illuminate your next step.

*What weighs upon your mind and heart today?*"""
        }
    ]

if "current_domain" not in st.session_state:
    st.session_state.current_domain = "all"

if "api_key" not in st.session_state:
    st.session_state.api_key = ""

# ---------------------------------------------------------
# Sidebar Setup
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
        st.info("💡 **Ready to Chat:** Using built-in scriptural intelligence! Add your Gemini key for continuous multi-turn reasoning.")
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
# Main App Header
# ---------------------------------------------------------
st.markdown("""
<div class="krishna-header">
    <div class="krishna-devanagari">॥ श्रीकृष्ण शरणं मम ॥</div>
    <div class="krishna-title">SHREE KRISHNA AI</div>
    <div class="krishna-subtitle">
        Timeless counsel synthesized from the <strong>Vedas, Upanishads, Puranas, Ramayana, and Bhagavad Gita</strong>.<br>
        Ask freely on your career, relationships, mental stillness, bodily vitality, or life purpose.
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Suggested Inquiries (Quick Starters)
# ---------------------------------------------------------
st.markdown("<p style='font-size: 1.1rem; font-weight: 600; color: #FDE047; margin-bottom: 0.6rem;'>🕊️ Inquiries to Seek Guidance On:</p>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("💼 Paralyzed by fear of failure in my career", use_container_width=True):
        st.session_state.prompt_to_submit = "I am gripped by intense fear of failure and losing everything in my professional venture. How do I act with total courage and focus without being destroyed by anxiety over outcomes?"
with col2:
    if st.button("🧠 Overwhelmed by racing thoughts & anxiety", use_container_width=True):
        st.session_state.prompt_to_submit = "My mind is relentlessly noisy, anxious, and jumping from one dread to another. I feel emotionally exhausted. How do I master my restless mind and find true peace?"
with col3:
    if st.button("🤝 Betrayal & setting boundaries with love", use_container_width=True):
        st.session_state.prompt_to_submit = "Someone I loved and trusted deeply betrayed me. How do I maintain compassion without being foolish, and how does Dharma advise me to set firm boundaries?"

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
