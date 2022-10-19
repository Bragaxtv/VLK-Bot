import os
import random
from tkinter import N
import discord
from discord.ext import commands





comeco = ['Season nova, ', 'Amanhã, ']
meio = ['Pegar elo maximo, ', 'no minimo, ', 'vo pegar, ']
final = ['Challanger.', 'radiante.', 'GCzinho.']

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#Montador de frases
@bot.command()
async def fimdaseason(ctx):
    await ctx.send((random.choice(comeco) + random.choice(meio) + random.choice(final)))

#Funções de ADICIONAR mais elementos nas listas
@bot.command()
async def addcomeco(ctx, arg):
    comeco.append(arg)
    await ctx.send(f'{arg} Foi Adicionado a lista de **começo** de frases.')   

@bot.command()
async def addmeio(ctx, arg):
    meio.append(arg)
    await ctx.send(f'{arg} Foi Adicionado a lista de **meio** de frases.')

@bot.command()
async def addfinal(ctx, arg):
    final.append(arg)
    await ctx.send(f'{arg} Foi Adicionado a lista de **final** de frases.')    
#Fim das funçoes de ADICIONAR elementos

#Funções de DELETAR elementos das listas
@bot.command()
async def removecomeco(ctx, arg):
    comeco.remove(arg)
    await ctx.send(f'{arg} Foi Removido da lista de **começo** de frases.')   

@bot.command()
async def removemeio(ctx, arg):
    meio.remove(arg)
    await ctx.send(f'{arg} Foi Removido da lista de **meio** de frases.')    

@bot.command()
async def removefinal(ctx, arg):
    final.remove(arg)
    await ctx.send(f'{arg} Foi Removido da lista de **final** de frases.')        
#Fim das funçoes de DELETAR elementos das listas

#!Help
@bot.command()
async def ajudaprimo(ctx):
    await ctx.send(f'__!fimdaseason__ -> Monta uma frase do hozarilol no final de **TODAS** as seasons dos games\n__!add__ (comeco | meio | final) -> Adiciona um elemento(texto) para a sua parte da frase.\n__!remove__ (comeco | meio | final) -> Remove um elemento(texto) da respectiva parte da frase.')
    await ctx.send(f'\n__!listas__ -> Mostra as listas atuais de frases')

#Printa as listas atuais
@bot.command()
async def listas(ctx):
    await ctx.send(f'Começo: {comeco}') 
    await ctx.send(f'Meio: {meio}') 
    await ctx.send(f'Final: {final}') 

#Pega o token do txt (txt precisa estar na mesma pasta do .py)
tokentxt = open(r".\\TOKEN.txt", "r")
TOKEN = tokentxt.read()
tokentxt.close
bot.run(TOKEN)