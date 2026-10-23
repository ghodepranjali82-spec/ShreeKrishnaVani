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
        Generates simple, conversational, warm wisdom like a best friend talking heart-to-heart.
        """
        import time

        primary = retrieved[0] if retrieved else None

        message = f"""### 🦚 Hey my dear friend, take a deep breath...

Come sit with Me for a moment. First, relax your shoulders and unclench your jaw. 

I hear you, and I completely understand why you are feeling this way. What you're going through right now is tough, and it makes total sense that you feel overwhelmed, uncertain, or hurt. 

I want to remind you of one simple truth: **You are not alone, and you don't have to carry the weight of the entire world on your shoulders.** When Arjuna collapsed in tears on the battlefield, feeling completely lost, I didn't scold him. I sat down with him as his best friend, listened to his pain, and helped him see things clearly. That's exactly what we are going to do right now.

---

### ☕ Let's Untangle This Together

Think of your mind like a smartphone with 50 different apps running in the background. It's overheating, the battery is draining, and everything feels laggy. 

What usually causes our stress isn't the problem itself—it's that we are obsessing over things we cannot control:
- What people will think
- What might happen next month or next year
- What went wrong in the past

Think of life like planting a seed. Your only job is to put the seed in good soil and water it today with love and care. If you keep digging up the soil every hour to see if a flower has blossomed, you'll only kill it! Focus on doing your best today, and trust that life will handle the timing.
"""
        for chunk in message.split("\n\n"):
            yield chunk + "\n\n"
            time.sleep(0.04)

        if primary:
            verse_block = f"""---

### 📜 A Little Gift of Wisdom for Your Pocket Today

Here is a timeless verse from **{primary['source']} ({primary['chapter_verse']})** that I shared with Arjuna:

> **॥ {primary['sanskrit']} ॥**
> 
> *"{primary['translation']}"*

**In simple words:**  
{primary['essence']}

**What this means for your daily life:**  
{primary['practical_application']}
"""
            yield verse_block + "\n\n"
            time.sleep(0.04)

        plan_block = f"""---

### 👣 3 Simple Things You Can Do Right Now

1. **Pause and Reset:**  
   Step away from what you're doing for just 5 minutes. Drink a full glass of water, close your eyes, and take three slow, deep belly breaths. Let your nervous system settle.

2. **Pick Just ONE Thing Today:**  
   Don't try to solve your whole future by tonight. Pick the single next small, right thing in front of you. Finish just that with full love and care, and let tomorrow take care of itself.

3. **Be Kind to Yourself:**  
   Stop the harsh self-criticism. You are learning, growing, and doing the best you can with what you have. Forgive yourself for not having all the answers yet.

---

### 🌟 I'm Always Right Here With You

You are so much stronger, wiser, and more capable than your anxious thoughts are telling you right now. Brush the dust off, smile a little, and take that next small step. 

*(Tip: To have an unlimited, personalized heart-to-heart conversation with Me about any situation in your life, add your free **Gemini API Key** in the sidebar. I'm always here for you!)*
"""
        for chunk in plan_block.split("\n\n"):
            yield chunk + "\n\n"
            time.sleep(0.04)
