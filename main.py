import discord
from discord.ext.commands import Bot
import dotenv

intents = discord.Intents.default()
intents.message_content = True



client = Bot(command_prefix="past", 
                  intents=intents, 
                  description="Gère les pastilles pour clarifier l'avancement du projet",
                  strip_after_prefix= True)

game = discord.Game(name="gérer votre code de singes", 
                    assets={'large_image':'bocchi_chair', 'large_text':'hmmm'}
                    )
client.activity = game

@client.tree.command(
    name="pastille",
    description="Change le statut actuel du salon, ",
    guild=discord.Object(905399047521697802),
)
async def set_pastille(interaction:discord.Interaction, statut:str):
    '''Change le statut du salon. \n
      Args:
        statut: "erreur": 🔴, "aide": 🟠, "cours": 🔵, "tests": 🟣, "fini": 🟢 '''
    channel = interaction.channel
    couleurs = {"erreur":'🔴', "aide":'🟠', "cours":'🔵', "tests":'🟣', "fini":'🟢'}

    await interaction.response.send_message(content=f"statut changée en {couleurs[statut]} !")
    if channel.name[0] in couleurs.values():
        await channel.edit(name=f'{couleurs[statut]}-{channel.name[1:]}')
    else:
        await channel.edit(name=f'{couleurs[statut]}-{channel.name}')


@client.event
async def on_ready():
    await client.tree.sync(guild=discord.Object(905399047521697802))
    # "erreur: 🔴, aide: 🟠, cours: 🔵, tests: 🟣, fini: 🟢"
    print("Ready!")

client.run(dotenv.get_key('.env','TOKEN'))
