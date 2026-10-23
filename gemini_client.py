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
                        "top_p": 0.9,
                        "max_output_tokens": 500,
                    }
                )

                for chunk in response:
                    if chunk.text:
                        yield chunk.text
                return
            except Exception as e:
                yield f"\n\n*(An error occurred while connecting: {str(e)}. Please check your Gemini API key.)*\n\n"
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
        Generates concise, beautiful, ChatGPT-grade wisdom (120-160 words).
        """
        import time

        primary = retrieved[0] if retrieved else None
        shloka_line = primary['sanskrit'].splitlines()[0] if (primary and primary.get('sanskrit')) else "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन।"
        ref = f"{primary['source']} ({primary['chapter_verse']})" if primary else "Bhagavad Gita 2.47"
        essence = primary['essence'] if primary else "Focus 100% on the present action, and release the anxious grip on outcomes."

        message = f"""Hey my dear friend, take a slow, deep breath. I hear you, and it makes complete sense that you feel this way. You don't have to carry the weight of the whole world on your shoulders today.

Remember the words I shared with Arjuna when he felt completely stuck:

> *॥ {shloka_line} ॥*  
> **{ref}** — *{essence}*

Think of life like planting a seed: give it water and care today, and trust the universe to handle the timing. When you stop obsessing over the finish line, your mind becomes still, and your strength returns.

Here are two simple things to do right now:
1. **Focus on just the next hour:** Pick only the single next small step in front of you. Do it with love, and let tomorrow take care of itself.
2. **Be gentle with yourself:** You don't need all the answers tonight. You are growing, and you are doing better than your anxious mind tells you.

Smile a little, my friend. I'm right here beside you. Now, take that next small step."""

        for paragraph in message.split("\n\n"):
            yield paragraph + "\n\n"
            time.sleep(0.04)
