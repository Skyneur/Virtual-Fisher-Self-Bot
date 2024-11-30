import discord
from discord.ext import tasks, commands  # Ajoutez commands
import re

# Ton token personnel (UTILISATION À TES RISQUES ET PÉRILS)
TOKEN = "VOTRE TOKEN"
CHANNEL_ID = ID DU CHANNEL  # ID du canal où se trouve le bot "Virtual Fisher"
BUTTON_LABEL = "Fish Again"  # Nom du bouton à cliquer

# Initialisation du bot en mode self-bot
bot = commands.Bot(command_prefix="!", self_bot=True)  # Utilisez commands.Bot sans intents

def extract_fish(message_content):
    """Extrait les poissons et leurs quantités du message."""
    fish_pattern = re.compile(r'(\d+)\s+(\w+\s*\w*)')  # Modifiez le motif de regex
    fish_caught = fish_pattern.findall(message_content)
    return fish_caught

@bot.event
async def on_ready():
    print(f"[✅] Connecté en tant que {bot.user}")
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        print(f"[✅] Canal trouvé : {channel.name}")
        if not fish_task.is_running():
            fish_task.start()  # Démarre la tâche dès que le bot est prêt
            print("\n\n[🔄] Démarrage du bot.\n\n")
            print("· ------------ · 𖥸   · ------------ ·")  # Ligne de séparation
    else:
        print("[❌] Impossible de trouver le canal. Vérifie l'ID.")

@tasks.loop(seconds=2.4)
async def fish_task():
    """Tâche périodique pour cliquer sur le bouton Fish."""
    print("[🛠️] Exécution de la tâche fish...")  # Ajoutez cette ligne pour le débogage
    try:
        channel = bot.get_channel(CHANNEL_ID)
        if not channel:
            print("[❌] Canal introuvable.")
            return

        # Parcourt les derniers messages du canal
        async for message in channel.history(limit=10):
            if hasattr(message, "components") and message.components:
                for component in message.components:
                    for button in component.children:
                        print(f"[🚧] Bouton détecté : {button.label}")
                        if button.label == BUTTON_LABEL:
                            try:
                                await button.click()
                                print("[✅] Bouton cliqué avec succès !\n")
                                print("⋟----------------------------------⋞\n")  # Ligne de séparation
                                return  # Quitte après un clic
                            except Exception as e:
                                print(f"[❌] Erreur en cliquant sur le bouton : {e}\n")
                                print("⋟----------------------------------⋞\n")  # Ligne de séparation
    except Exception as e:
        print(f"[❌] Erreur dans la tâche fish : {e}\n")
        print("⋟----------------------------------⋞\n")  # Ligne de séparation

@bot.event
async def on_message(message):
    """Événement déclenché lorsqu'un message est reçu."""
    global fish_task  # Ajoutez cette ligne pour éviter l'erreur UnboundLocalError

    if message.channel.id == CHANNEL_ID and "Virtual Fisher" in message.author.name:
        if not fish_task.is_running():
            fish_task.start()  # Démarre la tâche uniquement si elle n'est pas déjà active
            print("\n\n[🔄] Démarrage dubot.\n\n")
            print("· ------------ · 𖥸   · ------------ ·")  # Ligne de séparation

    if message.author == bot.user:
        return

    # Vérifie si l'embed contient le texte de vérification spécifique
    for embed in message.embeds:
        if embed.description and "solve the captcha posted above with the /verify command" in embed.description:
            print("\n\n[⚠️] Embed de vérification détecté. Arrêt de la pêche.\n\n")
            if fish_task.is_running():
                fish_task.stop()
            print("· ------------ · 𖥸   · ------------ ·")  # Ligne de séparation
            return

    # Affiche uniquement la description des embeds de manière lisible
    for embed in message.embeds:
        embed_dict = embed.to_dict()
        if 'description' in embed_dict:
            description = re.sub(r'<.*?>', '', embed_dict['description'])  # Supprime le texte entre < et >
            print("\n[🆕] Embed reçu :")
            description_lines = description.split('\n')
            for line in description_lines:
                if "XP" not in line and "Global boost" not in line:
                    print(f"  {line}")

# Lancer le bot
try:
    bot.run(TOKEN)  # Utilisez la variable TOKEN définie en haut du fichier
except Exception as e:
    print(f"[❌] Erreur lors de la connexion : {e}")
