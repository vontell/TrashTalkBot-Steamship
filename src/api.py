from steamship import check_environment, RuntimeEnvironments, Steamship, SteamshipError
from steamship.invocable import post, PackageService
import json
import time

# Hint: Try changing this!
PROMPT = 'Please create a response to an enemy game player who says "{phrase}". ' \
         'The trash talk should be related to the game, which is a Minecraft ' \
         'capture the flag game.'


class PromptPackage(PackageService):
    """Generates trash talk"""

    @post("generate")
    def generate(self, phrase: str = None) -> str:

        # First, create an LLM instance (specifically GPT-4)
        llm = self.client.use_plugin("gpt-4",
                                     config={
                                         "max_tokens": 30,
                                         "temperature": 0.8
                                     })
        retries = 3
        while retries > 0:
            try:
                response = llm.generate(text=PROMPT.format(phrase=phrase))
                response.wait()
                return json.dumps({"response": response.output.blocks[0].text})
            except SteamshipError as e:
                time.sleep(1)
                retries = retries - 1

        return json.dumps({"error": f"Error getting response: {e}"})


# Try it out locally by running this file!
if __name__ == "__main__":
    print("Generate Trash Talk with GPT-4\n")

    # This helper provides runtime API key prompting, etc.
    check_environment(RuntimeEnvironments.REPLIT)

    with Steamship.temporary_workspace() as client:
        package = PromptPackage(client)

        player_said = input("What did the player say? ")

        print("Generating...")

        # This is the prompt-based generation call
        result = json.loads(package.generate(phrase=player_said))
        insult = result['response']
        print("Insult: ", f'{insult}')