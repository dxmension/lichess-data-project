import httpx
import json
from typing import Dict, Any, List

async def get_player_games(student_username: str, student_token: str, since: int) -> List[Dict[str, Any]]:

    url = f"https://lichess.org/api/games/user/{student_username}"

    headers = {
        "Authorization": f"Bearer {student_token}",
        "Accept": "application/x-ndjson",
    }

    params = {
        "since": since
    }

    async with httpx.AsyncClient(timeout=20.0) as client:
        response = await client.get(url=url,headers=headers, params=params)

        if response.status_code != 200:
            raise Exception(f"Lichess API error {response.status_code}: {response.text}")

    games = []
    for line in response.text.splitlines():
        if line.strip():
            try:
                games.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"Skipping line: {e}")
    
    return games

async def get_player_puzzles(student_username: str, student_token: str, since: int, max_puzzles: int = 500) -> List[Dict[str, Any]]:
    
    url = f"https://lichess.org/api/puzzle/activity"
    headers = {
        "Authorization": f"Bearer {student_token}",
        "Accept": "application/x-ndjson",
    }
    params = { "max": max_puzzles }

    puzzles = []

    async with httpx.AsyncClient(timeout=30.0) as client:
        async with client.stream("GET", url, headers=headers, params=params) as response:
            if response.status_code != 200:
                raise Exception(f"Lichess API error: {response.status_code}")

            async for line in response.aiter_lines():
                if not line.strip():
                    continue
                try:
                    puzzle = json.loads(line)
                except json.JSONDecodeError:
                    continue

                if puzzle.get("date") < since:
                    continue

                puzzles.append(puzzle)

                if len(puzzles) >= max_puzzles:
                    break

    return puzzles
    
async def get_player_stats(student_username: str, student_token: str) -> Dict[str, Any]:

    url = f"https://lichess.org/api/user/{student_username}"

    headers = {
        "Authorization": f"Bearer {student_token}",
        "Accept": "application/json"
    }

    async with httpx.AsyncClient(timeout=20.0) as client:
        response = await client.get(url, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Lichess API error {response.status_code}: {response.text}")
    
    return response.json()