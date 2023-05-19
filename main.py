import asyncio
import string
import json
import itertools

class nameSniper:
    def __init__(self):
        self.config = self._config
        self.token = self.config.get("token")
        self.min_length = self.config.get("min_length")
        self.all_characters = list(string.ascii_lowercase + string.digits + "._")
        self.generated_strings = asyncio.Queue()
        assert self.token or self.min_length, "Missing arguments"
        self.semaphore = asyncio.Semaphore(float("inf"))
        
    @property
    def _config(self):
        with open("config.json", "r") as f: return json.load(f)
    
    async def check_username(self, username):
        # Simulated check for username availability
        name_used = False

        if name_used:
            print(f"Sniped Username: {username}")
        else:
            print(f"Already used: {username}")

    async def generate_combinations(self):
        min_length = self.config.get("min_length")
        async for combination in self.async_combinations(self.all_characters, min_length):
            yield ''.join(combination)

    async def async_combinations(self, iterable, r):
        pool = tuple(iterable)
        n = len(pool)
        indices = [0] * r
        yield tuple(pool[i] for i in indices)
        while True:
            for i in reversed(range(r)):
                if indices[i] != n - 1:
                    break
            else:
                return
            indices[i:] = [indices[i] + 1] * (r - i)
            yield tuple(pool[i] for i in indices)

    async def snipe(self):
        while True:
            tasks = []
            async for current_string in self.generate_combinations():
                tasks.append(asyncio.create_task(self.check_username(current_string)))
                
            await asyncio.gather(*tasks)
            self.config['min_length'] += 1
        
            
    
asyncio.run(nameSniper().snipe())
