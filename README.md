# Discord Bot 🤖🔊

A 24/7 continuous-hosting Discord bot built with `discord.py` and `Flask`. It automatically connects to a designated voice channel upon startup and features an embedded web server for free-tier cloud deployment platform keep-alive pings (Render, Railway, Replit, UptimeRobot).

---

## ⚡ Features

- **Automated Voice Channel Join**: Automatically connects to a targeted Discord Voice Channel on startup with automatic reconnect support.
- **Flask Keep-Alive Web Server**: Serves an HTTP endpoint (`/`) on port `10000` to satisfy cloud health check requirements and prevent deployment sleep mode.
- **Asynchronous Task Management**: Utilizes `discord.py` async loops alongside Python threading for non-blocking HTTP and bot operation.

---

## 🛠️ Tech Stack

- **Language**: Python 3.9+
- **Bot Framework**: `discord.py` v2.x
- **Web Framework**: Flask
- **Concurrency**: `asyncio`, `threading`

---

## ⚙️ Environment Variables & Configuration

Configure the following parameters in `main.py` or via environment variables:

| Variable / Parameter | Description |
| :--- | :--- |
| `TOKEN` | Discord Bot Token (set in system environment / `.env`) |
| `GUILD_ID` | Discord Server (Guild) ID |
| `VOICE_CHANNEL_ID` | Target Voice Channel ID to auto-connect |

---

## 🚀 Setup & Deployment

### Local Development

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/NodeNexus/DiscordBot.git
   cd DiscordBot
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variable & Run**:
   ```bash
   # On Linux/macOS
   export TOKEN="your_bot_token_here"
   python main.py

   # On Windows (PowerShell)
   $env:TOKEN="your_bot_token_here"
   python main.py
   ```

### Deploying to Render / Railway / Replit

1. Create a new Web Service on [Render](https://render.com/).
2. Connect your GitHub repository `NodeNexus/DiscordBot`.
3. Set the **Build Command**: `pip install -r requirements.txt`
4. Set the **Start Command**: `python main.py`
5. Add `TOKEN` under **Environment Variables**.
6. Set up a free ping monitor (e.g., [UptimeRobot](https://uptimerobot.com/)) pointing to your Render app URL to keep it active 24/7.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).