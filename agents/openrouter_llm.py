from langchain_core.language_models.llms import BaseLLM
from langchain_core.outputs import LLMResult, Generation
from typing import Any, List, Optional, Dict, Iterator
import requests
from config import Config

class OpenRouterLLM(BaseLLM):
    temperature: float = 0.7
    max_tokens: int = 1000
    
    @property
    def _llm_type(self) -> str:
        return "openrouter"

    def _generate(
        self,
        prompts: List[str],
        stop: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> LLMResult:
        generations = []
        for prompt in prompts:
            headers = {
                "Authorization": f"Bearer {Config.OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": Config.OPENROUTER_MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": kwargs.get("temperature", self.temperature),
                "max_tokens": kwargs.get("max_tokens", self.max_tokens)
            }

            response = requests.post(
                f"{Config.OPENROUTER_BASE_URL}/chat/completions",
                headers=headers,
                json=payload
            )
            
            if response.status_code != 200:
                raise ValueError(f"OpenRouter API error: {response.text}")
            
            content = response.json()["choices"][0]["message"]["content"]
            generations.append([Generation(text=content)])
        
        return LLMResult(generations=generations)

    async def _agenerate(
        self,
        prompts: List[str],
        stop: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> LLMResult:
        return self._generate(prompts, stop, **kwargs)