from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import asyncio
import loadotenv
from os import getenv
from getpass import getpass

# Load environment variables from the .env file
loadotenv.load_env()
api_id = int(getenv('API_ID'))
api_hash = getenv('API_HASH')

# Session file name (you can use any)
session_file_name = 'retrieve_messages'

async def main():
    # Create a client
    client = TelegramClient(session_file_name, api_id, api_hash)

    # Let's start the session
    await client.connect()

    if not await client.is_user_authorized():
        # Please enter your phone number in international format
        phone_number = input('Enter your phone number (in international format, for example +79991234567):')
        await client.send_code_request(phone_number)
        code = input('Enter the code received in Telegram:')
        try:
            await client.sign_in(phone_number, code)
        except SessionPasswordNeededError:
            # If two-factor authentication is enabled
            password = getpass('Enter your Telegram password:')
            await client.sign_in(password=password)
        print('Authorization successful!')

    # Now the client is authorized and you can perform further actions
    me = await client.get_me()
    print(f'Logged in as {me.first_name} ({me.username})')

    # Example: Get the last 5 messages from the specified channel
    channels = ['gamer_developer', 'mlphys']

    for channel in channels:
        try:
            entity = await client.get_entity(channel)
            print(f'\nLatest messages from channel {channel}:')
            async for message in client.iter_messages(entity, limit=5):
                print(f'[{message.date.strftime("%Y-%m-%d %H:%M:%S")}] {message.sender_id}: {message.text}')
        except Exception as e:
            print(f'Failed to get messages from channel {channel}: {e}')

    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
