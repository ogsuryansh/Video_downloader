# Video Downloader Bot

A Telegram bot that can download videos from YouTube, Instagram, TikTok, and Twitter.

## Features

- Download videos from multiple platforms
- Automatic file size management
- Auto-deletion of messages and files after 30 minutes
- User statistics tracking
- Admin commands for monitoring

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create a `.env` file:**
   ```bash
   # Copy the example and fill in your values
   cp .env.example .env
   ```

3. **Configure environment variables:**
   ```
   BOT_TOKEN=your_telegram_bot_token_here
   OWNER_ID=your_telegram_user_id_here
   ```

4. **Run the bot:**
   ```bash
   python main.py
   ```

## Environment Variables

- `BOT_TOKEN`: Your Telegram bot token from @BotFather
- `OWNER_ID`: Your Telegram user ID (for admin commands)

## Usage

1. Start the bot with `/start`
2. Send a video link from supported platforms
3. Wait for the bot to download and send the video
4. Files are automatically deleted after 30 minutes

## Supported Platforms

- YouTube
- Instagram
- TikTok
- Twitter

## Admin Commands

- `/stats` - View bot statistics (owner only)

## Security Notes

- The `.env` file is ignored by git to protect your bot token
- Downloaded videos are automatically deleted after sending
- Messages are auto-deleted after 30 minutes to prevent copyright issues

## Requirements

- Python 3.11+ (recommended for deployment)
- Internet connection
- Valid Telegram bot token

## Deployment

**💡 Free Hosting Recommendations**: Since Heroku no longer offers a free tier, consider these free alternatives:
- **Railway**: $5 free credit monthly
- **Render**: Free tier available
- **Fly.io**: Generous free tier (3 VMs)
- **Replit**: Free tier available

### Heroku
1. Fork this repository
2. Create a new Heroku app
3. Connect your GitHub repository
4. Set environment variables in Heroku dashboard:
   - `BOT_TOKEN`: Your Telegram bot token
   - `OWNER_ID`: Your Telegram user ID
5. Deploy the app

**Note**: Heroku no longer has a free tier. You'll need a paid plan ($7/month minimum).

### Railway
1. Fork this repository
2. Connect to Railway
3. Set environment variables in Railway dashboard
4. Deploy

### Render
1. Fork this repository
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Set environment variables
5. Deploy

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your bot token and owner ID

# Run the bot
python main.py
``` 