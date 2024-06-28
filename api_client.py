import httpx


async def get_insult(api_url="https://evilinsult.com/generate_insult.php?type=plain&lang=ru"):
    # Asynchronously get an insult from the API
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
        if response.status_code == 200:
            # The API response is plain text, so directly return it
            insult_text = response.text  # Use .text for plain text response
            return insult_text
        else:
            return "Чёт не получилось тебя отхуесосить, увы"
