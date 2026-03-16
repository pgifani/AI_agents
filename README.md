# 🌍 ADK City Agents

Two AI agents built with [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/) that provide real-time **time** and **weather** information for cities around the world — powered by [Groq](https://console.groq.com) (free) and [Open-Meteo](https://open-meteo.com/) (free, no API key needed).

---

## 📁 Repository Structure

```
adk-city-agents/
│
├── single_agent/          # Time-only agent (60 cities)
│   ├── agent.py
│   └── .env
│
├── multi_agent/           # Weather + Time agent (100 cities)
│   ├── agent.py
│   └── .env
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🤖 Agents

### `single_agent` — Time Agent
A simple agent that tells the **current local time** in 60+ cities worldwide.

**Supported regions:** Americas, Europe, Middle East, Asia, Africa, Oceania

**Example:**
```
[user]: what time is it in Tehran?
[agent]: The current time in Tehran is 06:30 PM

[user]: tokyo?
[agent]: The current time in Tokyo is 11:00 PM
```

---

### `multi_agent` — Weather & Time Agent
An agent that tells both the **current local time** and **real-time weather** (temperature, humidity, wind speed, conditions) for 100+ cities worldwide.

Weather data is sourced live from the [Open-Meteo API](https://open-meteo.com/) — completely free with no API key required.

**Example:**
```
[user]: london
[agent]: The current time in London is 14:12:35 GMT and the weather is
         overcast with a temperature of 9.4°C (48.9°F), humidity 45%,
         and wind speed of 21.6 km/h.

[user]: what about Tehran?
[agent]: The current time in Tehran is 17:42:51 +0330 and the weather is
         partly cloudy with a temperature of 7.5°C (45.5°F), humidity 60%,
         and wind speed of 4.2 km/h.

[user]: weather and time in Dubai?
[agent]: The current time in Dubai is 18:13 +04. The weather is partly cloudy
         with a temperature of 25.8°C (78.4°F), humidity 69%, wind 14.0 km/h.
```

---

## ⚙️ Requirements

- Python 3.13+
- Windows / macOS / Linux
- A free [Groq API key](https://console.groq.com)

---

## 🚀 Installation

### Step 1 — Install dependencies

```cmd
pip install -r requirements.txt
```

Or individually:
```cmd
pip install google-adk
pip install google-adk[extensions]
pip install pytz
pip install requests
```

### Step 2 — Add ADK Scripts to PATH (Windows)

Find your Python Scripts folder:
```cmd
python -c "import sys; print(sys.prefix + '\\Scripts')"
```

The output will look like:
```
C:\Users\YourName\AppData\Roaming\Python\Python313\Scripts
```

Add this path to **System Environment Variables → PATH**, then restart your terminal.

Verify:
```cmd
adk --version
```

---

## 🔑 API Keys

### Get a free Groq API key
1. Sign up at [console.groq.com](https://console.groq.com)
2. Go to **API Keys** → **Create API Key**
3. Copy the key (starts with `gsk_`)

### Configure `.env`

Create a `.env` file inside **each agent folder** you want to run:

```env
GOOGLE_GENAI_USE_VERTEXAI=0
GROQ_API_KEY=gsk_your_groq_key_here
```

> ⚠️ Important:
> - No quotes around the value
> - No spaces around `=`
> - `GROQ_API_KEY` not `GOOGLE_API_KEY`
> - Never commit `.env` to GitHub (already covered by `.gitignore`)

---

## ▶️ Running the Agents

Always run from the **parent folder** (not inside the agent folder):

```cmd
cd path/to/adk-city-agents
```

### Terminal (CLI) mode
```cmd
# Time-only agent
adk run single_agent

# Weather + Time agent
adk run multi_agent
```

### Web UI mode
```cmd
adk web
```
Then open [http://localhost:8000](http://localhost:8000) in your browser and select the agent from the left panel.

### Clear cache (if changes not taking effect)
```cmd
rmdir /s /q single_agent\__pycache__
rmdir /s /q multi_agent\__pycache__
```

---

## 🌆 Supported Cities

### single_agent (60 cities)

| Region | Cities |
|--------|--------|
| Americas | New York, Los Angeles, Chicago, Toronto, Vancouver, Mexico City, São Paulo, Buenos Aires |
| Europe | London, Paris, Berlin, Madrid, Rome, Amsterdam, Brussels, Vienna, Zurich, Stockholm, Oslo, Moscow, Istanbul |
| Middle East | Dubai, Tehran, Riyadh, Doha, Kuwait City, Baghdad, Beirut, Tel Aviv |
| Asia | Tokyo, Beijing, Shanghai, Hong Kong, Singapore, Seoul, Mumbai, Delhi, Karachi, Lahore, Dhaka, Bangkok, Jakarta, Kuala Lumpur |
| Africa | Cairo, Lagos, Nairobi, Johannesburg, Casablanca |
| Oceania | Sydney, Melbourne, Auckland |

### multi_agent (100 cities)

| Region | Cities |
|--------|--------|
| North America | New York, Los Angeles, Chicago, Houston, Miami, San Francisco, Seattle, Toronto, Vancouver, Montreal, Mexico City |
| South America | São Paulo, Rio de Janeiro, Buenos Aires, Bogotá, Lima, Santiago |
| Europe | London, Paris, Berlin, Madrid, Rome, Amsterdam, Brussels, Vienna, Zurich, Stockholm, Oslo, Copenhagen, Helsinki, Warsaw, Prague, Budapest, Bucharest, Athens, Lisbon, Dublin, Istanbul, Moscow, Kyiv |
| Middle East | Dubai, Abu Dhabi, Tehran, Riyadh, Jeddah, Baghdad, Kuwait City, Doha, Muscat, Beirut, Tel Aviv, Amman |
| Asia | Delhi, Mumbai, Bangalore, Kolkata, Karachi, Lahore, Dhaka, Colombo, Kathmandu, Kabul, Tashkent, Almaty, Bangkok, Ho Chi Minh, Hanoi, Phnom Penh, Yangon, Kuala Lumpur, Singapore, Jakarta, Manila, Tokyo, Osaka, Beijing, Shanghai, Hong Kong, Taipei, Seoul, Ulaanbaatar |
| Africa | Cairo, Lagos, Nairobi, Johannesburg, Cape Town, Casablanca, Accra, Addis Ababa, Dar es Salaam, Khartoum, Tunis, Algiers |
| Oceania | Sydney, Melbourne, Brisbane, Perth, Auckland, Wellington |

> To add a new city to `multi_agent`, add one entry to `CITY_DATA`:
> ```python
> "cape verde": {"tz": "Atlantic/Cape_Verde", "lat": 14.9330, "lon": -23.5133},
> ```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Agent Framework | [Google ADK](https://google.github.io/adk-docs/) v1.27+ |
| LLM | [Groq](https://console.groq.com) — `llama-3.3-70b-versatile` |
| Weather API | [Open-Meteo](https://open-meteo.com/) (free, no key needed) |
| Timezone | `pytz` library |

---

## 🔧 Troubleshooting

| Error | Cause | Fix |
|-------|-------|-----|
| `adk not recognized` | Scripts folder not in PATH | Add Scripts path to PATH, restart terminal |
| `Invalid API Key` | Wrong `.env` variable name | Use `GROQ_API_KEY=`, not `GOOGLE_API_KEY=` |
| `model decommissioned` | Old model name | Use `groq/llama-3.3-70b-versatile` |
| `tool_use_failed` | Cached old code | Delete `__pycache__` folder and restart |
| `limit: 0` on Gemini | No Gemini quota | Switch to Groq (already configured) |
| Agent not updating | Old cache loaded | Run `rmdir /s /q <agent>\__pycache__` |

---

## 📝 Notes

- **Tehran** uses a `+3:30` half-hour timezone offset — handled correctly by `pytz` with `"Asia/Tehran"`
- **Weather data** is updated every few minutes by Open-Meteo and requires no API key
- **Groq free tier** provides 14,400 requests/day and 6,000 tokens/minute — more than enough for development and testing
- **`sub_agents`** with `transfer_to_agent` are not supported by Groq — both tools live in a single `root_agent`

---

## 📄 License

MIT License — free to use and modify.
