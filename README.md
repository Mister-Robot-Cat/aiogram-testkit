# aiogram-testkit

A lightweight toolkit for testing [aiogram](https://github.com/aiogram/aiogram) (v3.x) bots in `pytest` without making real Telegram Bot API network requests.

## Features

- **MockedSession**: In-memory `BaseSession` implementation that records all outgoing bot requests and returns predefined responses.
- **Request Inspection**: Query recorded requests with helpers like `get_request`, `find_requests`, `has_request`, and `last_request`.
- **Zero External Mocks**: Clean, type-safe API that does not require monkeypatching `aiohttp`.

## Installation

```bash
pip install aiogram-testkit
```

## Quick Start

```python
import pytest
from aiogram import Bot
from aiogram.methods import SendMessage
from aiogram.types import Message, Chat
from aiogram_testkit import MockedSession

@pytest.mark.asyncio
async def test_bot_send_message():
    session = MockedSession()
    bot = Bot(token="1234:TEST", session=session)

    # Mock response
    session.add_result(
        "SendMessage",
        Message(
            message_id=1,
            date=1700000000,
            chat=Chat(id=42, type="private"),
            text="pong",
        ),
    )

    # Trigger bot logic
    result = await bot.send_message(chat_id=42, text="ping")

    assert result.text == "pong"
    assert session.has_request(SendMessage)
    assert session.last_request.chat_id == 42
```
