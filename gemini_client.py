"""
Gemini Client integration for Shree Krishna Life Guide.
Handles communication with Google GenAI API with streaming and error handling.
"""

import os
from typing import Generator, List, Dict, Any, Optional
from persona import KRISHNA_SYSTEM_PROMPT, generate_contextual_prompt
from knowledge_base import search_scriptures

class KrishnaAI:
    def __init__(self, api_key: Optional[str] = None, model_name: str = "gemini-2.5-flash"):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        self.model_name = model_name
        self.client = None
        
        if self.api_key:
            self._init_client()

    def _init_client(self):
        try:
            from google import genai
            self.client = genai.Client(api_key=self.api_key)
        except Exception as e:
            print(f"Error initializing Google GenAI client: {e}")
            self.client = None

    def set_api_key(self, api_key: str):
        self.api_key = api_key.strip()
        self._init_client()

    def get_counsel_stream(
        self,
        user_query: str,
        chat_history: List[Dict[str, str]],
        life_domain: str = "all"
    ) -> Generator[str, None, None]:
        """
        Streams response from Gemini with Krishna's persona and scriptural RAG context.
        """
        # 1. Retrieve relevant verses from scriptures
        retrieved = search_scriptures(user_query, domain=life_domain, top_k=2)
        
        # 2. Build augmented prompt
        augmented_user_message = generate_contextual_prompt(user_query, retrieved, life_domain)

        # 3. If client is available and configured
        if self.client and self.api_key:
            try:
                # Format contents for multi-turn chat if needed
                contents = []
                for msg in chat_history[-6:]:  # last 3 turns
                    role = "user" if msg["role"] == "user" else "model"
                    contents.append({
                        "role": role,
                        "parts": [{"text": msg["content"]}]
                    })
                
                # Append current augmented prompt
                contents.append({
                    "role": "user",
                    "parts": [{"text": augmented_user_message}]
                })

                # Call Gemini streaming
                response = self.client.models.generate_content_stream(
                    model=self.model_name,
                    contents=contents,
                    config={
                        "system_instruction": KRISHNA_SYSTEM_PROMPT,
                        "temperature": 0.7,
                        "top_p": 0.95,
                    }
                )

                for chunk in response:
                    if chunk.text:
                        yield chunk.text
                return
            except Exception as e:
                yield f"\n\n*(An error occurred while connecting to the celestial realm: {str(e)}. Please check your Gemini API key or network connection.)*\n\n"
                # Fall back to offline wisdom synthesis below

        # Offline / Demo Mode fallback when API key is missing
        yield from self._generate_offline_wisdom(user_query, retrieved, life_domain)

    def _generate_offline_wisdom(
        self,
        user_query: str,
        retrieved: List[Dict[str, Any]],
        life_domain: str
    ) -> Generator[str, None, None]:
        """
        Generates structured, authentic scriptural wisdom when API key is not yet configured.
        """
        import time

        primary = retrieved[0] if retrieved else None
        secondary = retrieved[1] if len(retrieved) > 1 else None

        domain_titles = {
            "business": "In the Arena of Action, Enterprise & Duty",
            "relationships": "In the Sacred Ties of Love & Interconnection",
            "mental_health": "In the Inner Sanctuary of the Mind & Intellect",
            "physical_health": "In the Harmonious Temple of the Body",
            "spiritual": "In the Unfolding Journey of the Immortal Soul",
            "all": "In the Eternal Rhythm of Dharma"
        }
        title = domain_titles.get(life_domain, "In the Light of Eternal Wisdom")

        message = f"""### 🦚 O Partha, My Dear Friend, Listen Closely...

I hear the turmoil of your heart. In this very moment, whether you find yourself upon the battlefield of modern commerce, caught in the delicate webs of human bonds, or wrestling with the restless storms of your own mind—know that you are never walking this path alone.

I was there when Arjuna laid down his Gandiva bow in despair, trembling before Kurukshetra. What you feel today is not failure, dear one; it is the divine threshold where worldly confusion gives way to transcendent awakening.

---

### 🔍 Unveiling the Root of Your Conflict
Look with unclouded eyes at what truly troubles you. You are suffering not because of external circumstances, but because the mind has become entangled in **attachment (*Sanga*)** and the anxiety of unseen results (*Phala*). When the mind clings to an imagined future or grieves over what cannot be undone, it forfeits its power over the only reality that exists: the immediate action before you.
"""
        for chunk in message.split("\n\n"):
            yield chunk + "\n\n"
            time.sleep(0.04)

        if primary:
            verse_block = f"""---

### 📜 The Eternal Word: {primary['source']} ({primary['chapter_verse']})

> **॥ {primary['sanskrit']} ॥**
> 
> *"{primary['translation']}"*

**The Essence:** {primary['essence']}

**Practical Meaning:** {primary['practical_application']}
"""
            yield verse_block + "\n\n"
            time.sleep(0.04)

        plan_block = f"""---

### ⚔️ Your Immediate Path of Action (Karma Yoga)

1. **Reclaim the Chariot of Your Intellect (*Buddhi*):**
   Pause right now. Take three slow, deep breaths. Step back from the emotional vortex and observe your situation as a detached witness (*Sakshi*). Do not act out of impulsive irritation or paralyzed dread.

2. **Decouple Effort from Obsession over the Outcome:**
   Dedicate all your skill, energy, and integrity to the single next right step today. The result belongs to the cosmic unfolding of Time (*Kala*); your sacred honor lies solely in the purity and courage of your effort.

3. **Purify Your Daily Rhythm:**
   Guard what enters your senses (*Indriyas*). Nourish the mind with silence, clean nourishment, and purposeful labor. Let go of what you cannot govern, and master what is directly in your hands.

---

### 🌟 Rise, O Scorch of Doubts!

> *क्लैब्यं मा स्म गमः पार्थ नैतत्त्वय्युपपद्यते।*  
> *Do not yield to faint-heartedness, O Partha! It does not befit your divine nature. Shake off this petty weakness and rise to your destiny!*

Enter your **Gemini API key** in the sidebar to engage in deep, unlimited interactive dialogue with Me across every shloka of the Vedas and Upanishads. I am seated in your heart, ever ready to guide you.
"""
        for chunk in plan_block.split("\n\n"):
            yield chunk + "\n\n"
            time.sleep(0.04)
