#!/usr/bin/env python3

import discord

client = discord.Client()

@client.event
async def on_ready():
    print('---------- Ditador - Online ----------')
    print('Nome: {}'.format(client.user.name))
    print('  ID: {}'.format(client.user.id))
    print('--------------------------------------')

    await client.change_presence(game=discord.Game(name="🌠  =help", type=1))

@client.event
async def on_message(message):

    #######################################################################################################

    if message.content.lower().startswith('=help'):
        embed1 = discord.Embed(
            title=':gear: Comandos',
            color=0xff0000,
            description='`=userinfo` 》Informações do usuário.\n'
                        '`=ban` 》Bane um usuário do seu servidor.\n'
                        '`=mute` 》Silencia um usuário por um período de tempo determinado.\n'
                        '`=unmute` 》Desfazer o mute.\n'
                        '`=avisos` 》Avisos de mundanças/eventos no servidor.\n'
                        '`=avatar` 》Ver avatar do membro.\n',
        )
        embed1.set_footer(text="Criador: Troy")
        await client.send_message(message.channel, embed=embed1)

    #######################################################################################################

    if message.content.lower().startswith("=userinfo"):
        try:
            user = message.mentions[0]
            role = ",".join([r.name for r in user.roles if r.name!="@everyone"])
            userjoinedat = str(user.joined_at).split('.', 1)[0]
            usercreatedat = str(user.created_at).split('.', 1)[0]
            embed =discord.Embed(
                 title='',
                 color=0xff0000,
                 description=''
            )


            embed.add_field(name=":inbox_tray: Data de Entrada:", value=userjoinedat, inline=True)

            embed.add_field(name="\n:beginner: Usuário:", value=user2.name, inline=True)

            embed.add_field(name="\n:calendar_spiral: Conta criada em:", value=usercreatedat, inline=True)

            embed.add_field(name="\n:unlock: ID:", value=user.id, inline=True)

            embed.add_field(name="\n:label: Tag:", value=user.discriminator, inline=True)

            embed.add_field(name="\n:mag_right: Cargos:", value=role, inline=True)

            embed.set_thumbnail(url=user.avatar_url)

            await client.send_message(message.channel, embed=embed)

        except IndexError:
            user2 = message.author
            role2 = ", ".join([r.name for r in message.author.roles if r.name!= "@everyone"])
            userjoinedat2 = str(user2.joined_at).split('.', 1)[0]
            usercreatedat2 = str(user2.created_at).split('.', 1)[0]
            embed1 = discord.Embed(
                title='',
                color=0xff0000,
                description=''
            )


            embed1.add_field(name=":inbox_tray: Data de Entrada:", value=userjoinedat2, inline=True)

            embed1.add_field(name="\n:beginner: Usuário:", value=user2.name, inline=True)

            embed1.add_field(name="\n:calendar_spiral: Conta criada em:", value=usercreatedat2, inline=True)

            embed1.add_field(name="\n:unlock: ID:", value=user2.id, inline=True)

            embed1.add_field(name="\n:label: Tag:", value=user2.discriminator, inline=True)

            embed1.add_field(name="\n:mag_right: Cargos:", value=role2, inline=True)

            embed1.set_thumbnail(url=message.author.avatar_url)

            await client.send_message(message.channel, embed=embed1)

        finally:
            pass

    #######################################################################################################

    if message.content.lower().startswith('=ban'):
        try:
            if not message.author.server_permissions.administrator:
                embed1 = discord.Embed(
                    title=':no_entry: Usuário sem Permissão!',
                    color=0xff0000,
                    description='Permissão insuficiente'
                )

                return await client.send_message(message.channel, embed=embed1)
            author = message.author.mention
            user = message.mentions[0]
            await client.ban(user)

            embed1 = discord.Embed(
                title=':white_check_mark: Usuário banido com Sucesso!',
                color=0xff0000,
                description='Usuário: {} foi banido do servidor pelo administrador: {}.'.format(user.mention,author)
            )
            await client.send_message(message.channel, embed=embed1)

        except  discord.errors.Forbidden:
            embed1 = discord.Embed(
                title=':cry: Usuário com privilégios administrativos!',
                color=0xff0000,
                description='Não foi possível banir o usuário: {}.'.format(user.mention)
            )
            return await client.send_message(message.channel, embed=embed1)

    #######################################################################################################

    if message.content.lower().startswith('=mute'):
        if not message.author.server_permissions.administrator:
            embed1 = discord.Embed(
                title=':no_entry: Usuário sem Permissão!',
                color=0xff0000,
                description='Permissão insuficiente'
            )

        author = message.author.mention
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Mutado')
        await client.add_roles(user, cargo)

        embed1 = discord.Embed(
            title=':white_check_mark: Usuário mutado com Sucesso!',
            color=0xff0000,
            description='Usuário: {} foi mutado do servidor pelo administrador: {}.'.format(user.mention,author)
        )
        await client.send_message(message.channel, embed=embed1)

    #######################################################################################################

    if message.content.lower().startswith("=unmute"):
        if not message.author.server_permissions.administrator:
            embed1 = discord.Embed(
                title=':no_entry: Usuário sem Permissão!',
                color=0xff0000,
                description='Permissão insuficiente'
            )

        author = message.author.mention
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Mutado')
        await client.remove_roles(user, cargo)

        embed1 = discord.Embed(
            title=':white_check_mark: Usuário desmultado com Sucesso!',
            color=0xff0000,
            description='Usuário: {} foi desmultado do servidor pelo administrador: {}.'.format(user.mention,author)
        )
        await client.send_message(message.channel, embed=embed1)

    #######################################################################################################

    if message.content.lower().startswith('=avatar'):
        try:
            membro = message.mentions[0]

            embed1 = discord.Embed(
                title=":mountain: Imagem de Perfil",
                color=0x4d0083,
                description='[Clique aqui]('+membro.avatar_url+') para acessar o link do avatar de {}!'.format(membro.name)
            )
            embed1.set_image(url=membro.avatar_url)
            await client.send_message(message.channel, embed=embed1)

        except:
            membro = message.author

            embed = discord.Embed(
                title=':mountain: Imagem de Perfil'.format(membro.name),
                color=0x4d0083,
                description='[Download]('+membro.avatar_url+') do avatar!.'.format(membro.name)
            )
            embed.set_image(url=membro.avatar_url)
            await client.send_message(message.channel, embed=embed)

    #######################################################################################################

    if message.content.lower().startswith('=avisos'):
        role = discord.utils.get(message.server.roles, name='avisos')
        if not role in message.author.roles:
            embed1 = discord.Embed(
                title=':warning: Ocorreu um Erro!',
                color = 0xff0000,
                description="`Você não tem permissão:` Você precisa do cargo @avisos para utilizar."
            )
            embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            return await client.send_message(message.channel, embed=embed1)

        msg = message.content.strip('=avisos')

        embed2 = discord.Embed(
            title=':hourglass: Enviado Mensagem...',
            color=0x7289DA,
            description="`Mensagem: `\n**{}**".format(msg)
        )

        embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
        await client.send_message(message.channel, embed=embed2)

        x = list(message.server.members)
        s = 0
        
        for member in x:
            embed1 = discord.Embed(color=0x1ce1de, description=(msg))
            embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)

            try:
                await client.send_message(member, embed=embed1)
                print(member.name)
                s += 1

            except:
                pass
        print('\nAviso enviado para {} membros de {}'.format(s, len(x)))
        embed2 = discord.Embed(
            title=':thumbsup: Mensagem Enviada Com Sucesso!',
            color=0x42f445,
            description=":ok_hand:"
        )

        embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
        await client.send_message(message.channel, embed=embed2)

    #######################################################################################################

client.run("NDYwMTQzMzg5ODE2NjUxNzk0.DhAddg.1UVyPyIoShBbAjTf1wKhXZzWejU")
