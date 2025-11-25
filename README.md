# Kiwi Bot

Kiwi Bot is a small Discord bot used to save audit logs in the supabase storage. It includes a few utility commands and uses rich embeds for responses.

## Features

- Saves audit logs to supabase storage(configured in the bot code)
- A few utility commands (for example: `ping`)
- Uses Discord embeds for nicer messages

## Quick install

1. Clone the repo

```bash
git clone https://github.com/RjNlxe/KiwiBot
cd KiwiBot
```

2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies

If you have a `requirements.txt` file, use:

```bash
pip install -r requirements.txt
```

Otherwise install the main dependencies:

```bash
pip install -U discord.py python-dotenv
```

4. Configure environment variables

Copy `.env.example` to `.env` and add your bot token and optionally a prefix:

```bash
cp .env.example .env
# then edit .env and set DISCORD_BOT_TOKEN and PREFIX
```

Example `.env` contents:

```
DISCORD_BOT_TOKEN=your_token_here
PREFIX=!
```

5. Run the bot

```bash
python3 main.py
```

## Notes

- The bot uses cogs in `commands/utility/` for commands. Add new command modules there.
- Embeds are created with helper utilities in `helpers/responses.py`.
- Supabase Initialization are in `helpers/supabase.py`.

That's all — clone, set up the venv, configure `.env`, and run `main.py`.
