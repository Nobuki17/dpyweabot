import os
import traceback

token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print("Weabot / うぇあぼっと のログインが完了しました。")
    await client.change_presence(activity=discord.Game(f"ヘルプは wb:help | 導入サーバー数: {len(client.guilds)}"))

#inlineはTrueになってるやつが前のやつの隣に行く、Falseは前のやつの下
@client.event
async def on_message(message):
    async def embox(title,description,color,message):
      embed = discord.Embed(title=title,description=description,color=color)
      await message.channel.send(embed=embed)

    if message.author == client.user:
        return
      
    if message.author.bot:
        return

    elif client.user in message.mentions:
        print(f"{message.author.name}にメンションされました")
        reply = f'{message.author.mention} \nwb:help でヘルプを表示します。'
        await message.channel.send(reply)
        return

    elif message.content == "wb:help":
        embed = discord.Embed(title="ヘルプ", description="このヘルプコマンドにはプレフィックスを書いていないため、\n実行には全て`wb:コマンド名`とする必要があります。",color=0x77aa27)
        embed.add_field(name="help", value="このコマンドです。",inline=False)
        embed.add_field(name="newinfo", value="新着情報を確認します。",inline=False)
        embed.add_field(name="wiki", value="開発者が知っていること、関係することについてwiki形式で見ることができます。",inline=False)
        embed.add_field(name="dice", value="サイコロを振ることができます。",inline=False)
        embed.add_field(name="ping", value="BOTのメッセージ送信速度をチェックします。",inline=False)
        embed.add_field(name="about", value="botについてや、botの招待リンクを確認できます。",inline=False)
        embed.add_field(name="serverintroduction", value="開発者が運営しているサーバーについて表示できます。",inline=False)
        await message.channel.send(embed=embed)

    elif message.content == "wb:about":
        embed = discord.Embed(title="このbotについて...", description="Weabot / うぇあぼっと",color=0x77aa27)
        embed.add_field(name="製作者", value="Weapon of / うぇぽん#6928",inline=True)
        embed.add_field(name="バージョン", value="Ver.1.5b",inline=False)
        embed.add_field(name="招待リンク", value="https://discord.com/api/oauth2/authorize?client_id=699585993988374628&permissions=117824&scope=bot",inline=False)
        await message.channel.send(embed=embed)

    elif message.content == "wb:serverintroduction":
        embed = discord.Embed(title="開発者のサーバーについて...", description="以下のリンクから参加できます。",color=0x77aa27)
        embed.add_field(name="招待リンク:", value="https://discord.gg/9ayfU9K")
        await message.channel.send(embed=embed)

    elif message.content == "wb:credit":
      await embox("このBOTの製作者","このBOTの製作者は、 **Weapon of / うぇぽん#6928** です。\n他にも、Pythonに詳しい人からのサポートを受けて開発されています。",0x77aa27,message)

    elif message.content == "wb:newinfo":
      await embox("新着情報","**2020 5/15** 一般公開を開始しました。\n**2020 5/14** help等のコマンドを3つ実装しました。\n**2020 5/2 **  BOTの稼働を開始しました。",0x77aa27,message)

    elif message.content == "wb:test":
      await embox("これはテストコマンドです。","特に意味はありません。",0x77aa27,message)

    elif message.content == "wb:dice":
        await embox(f"{message.author.name}さんがサイコロコマンドを実行しました","何が出るかな？！何が出るかな？！",0x77aa27,message)
        time.sleep(1) # 一秒待つ
        x = random.randint(1,6) # 50から100の乱数をxに代入
        await embox("結果は、、",f"結果は {str(x)} でした！",0x77aa27,message)
        return

    elif message.content == "wb:ping":
        starttime = time.time()
        msg = await message.channel.send("測定中です...しばらくお待ちください。")
        ping = time.time() - starttime
        await msg.edit(content=f"結果:{round(ping * 1000)}ms")
        
        #float(ping * 1000)

    elif message.content.startswith("こんにち"):
        await message.channel.send("こんにちは！")

    elif message.content.startswith("こんちゃ"):
        await message.channel.send("こんちゃっちゃ！！")

    elif message.content.startswith("ども"):
        await message.channel.send("どうも！")

    elif message.content.startswith("よろし"):
        await message.channel.send("よろしくお願いします！")

    elif message.content.startswith("ただいま"):
        await message.channel.send("おかえり～")

    elif message.content.startswith("飯落ち"):
        await message.channel.send("いってらっしゃい！")

    elif message.content.startswith("落ち"):
        await message.channel.send("お疲れ～")

    elif message.content.startswith("ばい"):
        await message.channel.send("ばい～")

    elif message.content.startswith("死ね"):
        await message.channel.send("暴言はまずいですよ！！")

    elif message.content.startswith("おはよ"):
        await message.channel.send("おはようございます～")
        
    elif message.content.startswith("暇"):
        await message.channel.send("暇ですねぇ...")


    elif message.content == "wb:wiki":
        embed = discord.Embed(title="WeaのWikiへようこそ！", description="開発者が知っていることや関係することについてwiki形式で紹介します。\n(実行は全て`wb:wiki 単語名`というように行ってください。)",color=0x77aa27)
        embed.add_field(name="現在登録されているもの:", value="アスファルト 9: Legends\nNintendo Switch\nTJAPlayer3")
        await message.channel.send(embed=embed)

    elif message.content == "wb:wiki アスファルト 9: Legends":
        await embox("アスファルト 9: Legends","アスファルト 9: Legends とは、\nゲームロフトが開発した\niOS、Android、Windows、Nintendo Switch、MacOS で\nプレイできるカーアクションレースゲームのこと。\nアスファルトシリーズ13作目(ナンバリングでは9作目)で、\n実在する車(マシン)を操作し、様々なロケーションでレースを行う。",0x77aa27,message)
    
    elif message.content == "wb:wiki Nintendo Switch":
        await embox("Nintendo Switch","Nintendo Switch とは、\n任天堂が開発・販売をしている、\n据え置き型ゲーム機のこと。",0x77aa27,message)

    elif message.content == "wb:wiki TJAPlayer3":
        await embox("TJAPlayer3","TJAPlayer3 とは、\nWindows向けの太鼓の達人エミュレーターの一つ。\n現在は配布を終了している。(Waybackmachineというツールを使用すればDL可)\n.tja 形式の譜面データと音源ファイルを用意することでプレイ可能。",0x77aa27,message)

client.run("token")
