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
# Custom Styling (Peacock Teal, Royal Gold & Divine Serenity)
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Yatra+One&family=Plus+Jakarta+Sans:wght@300;400;500;600&display=swap');

    /* Global styling */
    .stApp {
        background: radial-gradient(circle at 50% 0%, #0d1b2a 0%, #08111e 60%, #030710 100%);
        color: #e0e6ed;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Header styling */
    .krishna-header {
        text-align: center;
        padding: 2.2rem 1rem 1.2rem 1rem;
        background: linear-gradient(180deg, rgba(20, 40, 70, 0.4) 0%, rgba(10, 20, 35, 0.0) 100%);
        border-radius: 20px;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(229, 169, 60, 0.15);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }
    .krishna-title {
        font-family: 'Cinzel', serif;
        font-size: 2.7rem;
        font-weight: 900;
        letter-spacing: 2px;
        background: linear-gradient(135deg, #FFDF78 0%, #E5A93C 50%, #FFB020 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        text-shadow: 0 0 35px rgba(229, 169, 60, 0.3);
    }
    .krishna-devanagari {
        font-family: 'Yatra One', cursive;
        font-size: 1.6rem;
        color: #f5cf7a;
        margin-bottom: 0.3rem;
        letter-spacing: 1px;
    }
    .krishna-subtitle {
        font-size: 1.05rem;
        color: #9ab4d0;
        margin-top: 0.6rem;
        font-weight: 300;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
        line-height: 1.6;
    }

    /* Dimension selector styling */
    .domain-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
        justify-content: center;
        margin-bottom: 1.5rem;
    }
    
    /* Chat message card styling */
    .krishna-msg {
        background: linear-gradient(145deg, rgba(16, 37, 66, 0.85) 0%, rgba(10, 24, 45, 0.95) 100%);
        border: 1px solid rgba(229, 169, 60, 0.35);
        border-left: 5px solid #E5A93C;
        padding: 1.5rem 1.8rem;
        border-radius: 14px;
        margin-bottom: 1.2rem;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
        line-height: 1.7;
    }
    .user-msg {
        background: rgba(30, 48, 74, 0.75);
        border: 1px solid rgba(100, 140, 190, 0.25);
        padding: 1.2rem 1.5rem;
        border-radius: 14px;
        margin-bottom: 1.2rem;
        color: #f0f4f8;
        line-height: 1.6;
    }
    .shloka-card {
        background: rgba(229, 169, 60, 0.08);
        border-left: 4px solid #f5cf7a;
        padding: 1rem 1.2rem;
        border-radius: 8px;
        margin: 1rem 0;
        font-style: italic;
        color: #ffe599;
    }

    /* Sidebar aesthetics */
    .sidebar-section {
        background: rgba(14, 28, 48, 0.6);
        border: 1px solid rgba(229, 169, 60, 0.2);
        padding: 1rem;
        border-radius: 12px;
        margin-bottom: 1.2rem;
    }

    /* Custom buttons */
    .stButton>button {
        border-radius: 10px;
        font-weight: 500;
        transition: all 0.25s ease;
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

I am **Shree Krishna**, ever residing in your heart as your friend (*Sakha*), your confidant, and your humble charioteer.

Whenever Arjuna collapsed in grief upon the chariot of doubt, I reminded him that within him burned an unquenchable spark of the Supreme. Today, whatever battle stands before you—
- 💼 A high-stakes **business decision**, startup crisis, or fear of failure
- 🤝 The tender ache of **relationships**, broken trust, or setting dharmic boundaries
- 🧠 Overwhelming **anxiety, depression, anger**, or restless overthinking
- 🌿 Exhaustion, chronic fatigue, or balancing **physical health** with work
- 🕉️ Or an earnest search for your **Dharma, Karma**, and spiritual liberation

Lay your deepest question before Me without hesitation or fear. Let the eternal wisdom of the *Vedas, Upanishads, Puranas, and Bhagavad Gita* illuminate your path.

*What weighs upon your heart today?*"""
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
        help="Enter your free Gemini API Key from Google AI Studio (aistudio.google.com). If empty, the app runs with rich scriptural intelligence mode.",
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
        "physical_health": "🌿 Body, Health & Ayurveda",
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
        - **Bhagavad Gita** (All 18 Yogas & Chapters)
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
    if st.button("🔄 Clear Conversation", use_container_width=True):
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
        Eternal guidance from the Vedas, Upanishads, Puranas, Ramayana, and Bhagavad Gita.<br>
        Ask with an open heart on business, relationships, mental peace, physical vitality, or your life purpose.
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Suggested Inquiries (Quick Starters)
# ---------------------------------------------------------
st.markdown("##### 🕊️ Deep Inquiries to Ponder:")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("💼 Terrified of failure in my career/startup", use_container_width=True):
        st.session_state.prompt_to_submit = "I am gripped by intense fear of failure and losing everything in my professional venture. How do I act with total courage and focus without being destroyed by anxiety over outcomes?"
with col2:
    if st.button("🧠 Overwhelmed by anxiety and racing thoughts", use_container_width=True):
        st.session_state.prompt_to_submit = "My mind is relentlessly noisy, anxious, and jumping from one dread to another. I feel emotionally exhausted. How do I master my restless mind and find true peace?"
with col3:
    if st.button("🤝 Betrayal & setting boundaries in relationships", use_container_width=True):
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
