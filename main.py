import string
import json
import itertools

class nameSniper:
    def __init__(self):
        self.config = self._config
        self.token = self.config.get("token")
        self.min_length = self.config.get("min_length")
        self.all_characters = list(string.ascii_lowercase + string.digits + "._")
        assert self.token or self.min_length, "Missing arguments"
        
    @property
    def _config(self):
        with open("config.json", "r") as f: return json.load(f)
    
    def snipe(self):
        while True:
            random_string = [''.join(p) for p in itertools.product(self.all_characters, repeat=self.config.get("min_length"))]
            for current_string in random_string:
                # check if user_name is used
                name_used = False
                if name_used:
                    return print(f"User {current_string} sniped")
                else:
                    print(f"Not avaible: {current_string}")
            self.config['min_length'] += 1
        
            
    
nameSniper().snipe()