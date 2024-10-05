import discord
from discord.ext.commands import Bot
import dotenv


class MyClient(Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        channel = message.channel
        mess = message.content.lower()
        status = {"erreur":'🔴', "aide":'🟠', "cours":'🔵', "tests":'🟣', "fini":'🟢'}

        if (mess[:2] == "p ") or (mess[:4] == "past"):
            for pastille in status.keys():
                if pastille in mess:
                    print(f'{message.author} change la pastille de {channel.name} en {pastille}')

                    if channel.name[0] in status.values():
                        await channel.edit(name=f'{status[pastille]} - {channel.name[1:]}')

                    else:
                        await channel.edit(name=f'{status[pastille]} - {channel.name}')
                    
                    await channel.send(f"Pastille {status[pastille]} changée avec succès !", delete_after=3)
                    await message.delete(delay=3)
                    return None


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(command_prefix="past", intents=intents)
game = discord.Game(name="gérer votre code de singes", 
                    assets={'large_image':'bocchi_chair', 'large_text':'hmmm'}
                    )
client.activity = game

client.run(dotenv.get_key('.env','TOKEN'))
