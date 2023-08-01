# Crypto Discord Bot

The Crypto Discord Bot is a Python-based bot that fetches real-time cryptocurrency prices from Coingecko and displays them in your Discord server. With this bot, you and your server members can stay up-to-date with the latest prices of various cryptocurrencies.

## Table of Contents

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)

## About

The Crypto Discord Bot is designed to be a helpful tool for crypto enthusiasts and traders who want to keep track of cryptocurrency prices without leaving Discord. By integrating this bot into your server, you can easily check the prices of your favorite coins in real-time.

## Installation

### Prerequisites

To run the bot, ensure you have the following installed:

- Python (at least version 3.6)
- pip (Python package manager)

### Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/crypto-discord-bot.git
```

2. Navigate to the project directory:

```bash
cd crypto-discord-bot
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. Create a Discord bot and get your bot token:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Create a new application and add a bot to it.
   - Copy your bot token.

5. Set up your configuration:
   - Rename `config.example.ini` to `config.ini`.
   - Open `config.ini` and replace `YOUR_BOT_TOKEN` with your bot token.

### Running the Bot

To start the bot, run the following command:

```bash
python bot.py
```

The bot will now be active on your Discord server.

## Usage

Once the bot is running in your server, you can use the following commands to interact with it:

- `!price <coin>`: Fetches the current price of a specific cryptocurrency from Coingecko. Replace `<coin>` with the name or symbol of the cryptocurrency (e.g., `!price bitcoin` or `!price BTC`).
- `!help`: Displays a list of available commands and their usage.

## Contributing

We welcome contributions to enhance the functionality of the Crypto Discord Bot. If you want to add new features, improve existing ones, or fix bugs, feel free to contribute.

To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add your commit message here"
   ```
4. Push your changes to your forked repository:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request to the `main` branch of this repository.
6. We will review your contribution, provide feedback, and merge it once approved.

Please ensure your pull request follows our [Code of Conduct](CODE_OF_CONDUCT.md).

## License

This project is licensed under the [MIT License](LICENSE).
