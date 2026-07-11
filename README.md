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

WEEK 2.

What this is
Continuing the 6-week AI/LLM security project. This week was about learning
the OWASP Top 10 for LLMs (2025) and getting hands-on with prompt injection —
the 1 risk on that list.

What I did
- Studied the OWASP Top 10 2025 for LLM applications
- Tried prompt injection against my own Week 1 script (`llm_logger.py`)
- Completed a prompt injection lab on TryHackMe to see a proper, structured example

What I found
My own script wasn't a useful target for injection — it has no system prompt,
no hidden instructions, no secrets, and no privileged actions tied to the
model's output. It just takes my input and passes it straight to Llama 3.3 70B.
There was nothing to "hijack" because there was no trust boundary to break.

This was actually a useful negative result: prompt injection needs a system
that trusts the model's output to do *something* — call a tool, reveal hidden
context, bypass a rule, take an action. A bare input → LLM → output loop with
no privilege attached isn't a meaningful attack surface.

The TryHackMe lab showed a proper case: a chatbot with a hidden system prompt
instructing it to keep certain information secret, which could be extracted
or overridden by crafting input that made the model ignore its original
instructions.

Why this matters for security
Prompt injection is OWASP's  1 LLM risk for a reason — it's the equivalent of
SQL injection or XSS for LLM-powered apps, except there's no clean separator
between "code" and "data" the way there is in traditional injection classes.
Any system that mixes untrusted user input with trusted instructions
(system prompts, retrieved documents, tool outputs) is potentially exposed.

Key takeaway
Injection risk scales with what the model is *trusted to do*, not just what
it's told. A logging script with no privileges is low-risk by design.
A chatbot with hidden instructions, tool access, or secret data is where
injection actually bites.

Stack
- Python 3.14
- Groq API
- Llama 3.3 70B
