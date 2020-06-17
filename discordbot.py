from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='wb:')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await bot.change_presence(activity=discord.Game(f"ヘルプは wb:help | 導入サーバー数: {len(client.guilds)}"))
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
   


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
