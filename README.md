LLM Security Project 

WEEK 1. 

What this is
A Python script that connects to Groq's API and runs Llama 3.3 70B.
Interactive — you type a prompt, get a response, everything gets logged to a JSON file.
Built as week 1 of a 6-week hands-on AI/LLM security learning project.

Why this matters for security
Input/output logging is a security primitive for any AI system in production.
Without it you have no audit trail, no way to detect prompt injection attempts,
and no forensic data if something goes wrong.
This script is the simplest working version of that pattern.

What I ran into
- Exposed my Groq API key in a commit — GitHub push protection caught it
- Rotated the key, rewrote commit history
- First real lesson: never hardcode secret

How to run it
1. Get a free API key at console.groq.com
2. Set it: `GROQ_API_KEY="your_key_here"`
3. Run: `python3 llm_logger.py`
4. Type your prompt, get a response, type `exit` to quit
5. Check `log.json` for the full conversation log

Stack
- Python 3.14
- Groq API
- Llama 3.3 70B
