import aiohttp
import asyncio
import json

async def fetch_page(session, api_url, page):
    async with session.get(f"{api_url}?page={page}") as response:
        return await response.json()

async def fetch_all_data(api_url):
    all_data = []
    page = 1

    async with aiohttp.ClientSession() as session:
        while True:
            data = await fetch_page(session, api_url, page)
            if not data:
                break
            all_data.extend(data)
            page += 1
            await asyncio.sleep(0.1)  # Small delay to prevent server overload

    return all_data

def find_citations(response, sources):
    citations = []
    for source in sources:
        if source['context'] in response:
            citations.append({
                "id": source["id"],
                "link": source.get("link", "")
            })
    return citations

async def process_data(api_url):
    data = await fetch_all_data(api_url)
    result = []
    for item in data:
        response = item.get('response', '')
        sources = item.get('sources', [])
        citations = find_citations(response, sources)
        result.append(citations)
    return result

async def main():
    api_url = "https://devapi.beyondchats.com/api/get_message_with_sources"
    citations = await process_data(api_url)
    for citation in citations:
        print(citation)

if __name__ == "__main__":
    asyncio.run(main())
