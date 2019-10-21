# KermodeBot
Final Project for Intro to Computer Programming

This final project is the creation of a bot to be used on Discord. Discord is a voice and text channel software often used by video game players, among others. Quest itself has a server which I administrate in order to schedule tournaments and communicate with teammates. This bot uses the discord.py library, which is publicly available. My primary information came from the following sources:

discord.py API: https://discordpy.readthedocs.io/en/latest/api.html#
discord.py discord help server: https://discordapp.com/channels/336642139381301249/381965829857738772
A video series by YouTuber "Lucas:" https://www.youtube.com/watch?v=nW8c7vT6Hl4&list=PLW3GfRiBCHOhfVoiDZpSz8SM_HybXRPzZ

The bot has two main pieces of code, beyond the set-up code which allows it to access the server and send messages. The two code elements are commands and on_message responses.

A command takes the format "@client.command" and is activated when its name is typed preceded by the "command prefix," which in this case is "!". Commands then have asynchronous functions which they perform, such as pinging the server to determing latency. The commands current written into bot1.py are listed here:

 - !intro: Lists commands
 - !time: Prints the current time
 - !joke: Prints a random joke from an array of bad video game puns
 - !pingu: Pings the server and prints latency in ms (as well as saying Noot Noot)
 - !ding: Prints from a random list of aggressive condemnations ('ding' is the username of the member who requested the function)
 - !yeet: Kicks a member from the server (!yeet [member.name]) 

The on_message code responds passively to any message which triggers its conditionals. Here are the functioning conditionals:

 - If Michael Lee sends a message, the bot reacts with an angry face emoji
