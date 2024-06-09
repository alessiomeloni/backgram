# Reverse Shell Controller with Telegram Bot

## Description

This script was created when I was 14 or 15 years old, and it probably doesn't run anymore due to its age and lack of updates. It served as a reverse shell controller using Telegram, allowing me to execute commands on a remote machine via a Telegram bot. I used it to play porn on the interactive whiteboard in my classroom to prank my professors. Our professors were getting seriously mad about it and even started investigating, but no one ever caught me. This script is shared for educational purposes only.

## Features

- **Telegram Bot Integration**: Utilizes the Telepot library to create a Telegram bot.
- **Command Execution**: Executes shell commands received via Telegram and sends back the output.
- **Simple Confirmation**: Sends a confirmation message if the command executes without producing output.

## How It Works

1. **Bot Setup**: The script initializes a Telegram bot using a provided token.
2. **Message Handling**: It listens for incoming messages via the `MessageLoop` function.
3. **Command Execution**: When a text message is received, it treats the message content as a shell command and executes it.
4. **Response**: The output of the command is sent back to the user through Telegram. If there's no output, a confirmation message is sent.

## Usage

1. **Install Dependencies**: Ensure you have the `telepot` library installed. You can install it using pip:
   ```bash
   pip install telepot
   ```
2. **Set the Token**: Replace the `TOKEN` variable in the script with your Telegram bot token.
3. **Run the Script**: Execute the script using Python:
   ```bash
   python backgram.py
   ```
4. **Send Commands**: Send shell commands to your bot through Telegram, and it will execute them and return the output.

## Important Notes

- This script is outdated and might not work with current versions of Python or the Telepot library.
- Using this script for malicious purposes is illegal and unethical. It was created as a prank and should not be used for harmful activities.
- Always consider the legal and ethical implications of using reverse shells or similar tools.

## Disclaimer

This script was created during my teenage years for fun and pranks. It is not a well-maintained or secure piece of software. Use it at your own risk and for educational purposes only. I do not take any responsibility for any misuse or damage caused by this script.
