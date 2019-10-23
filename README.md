# KermodeBot
Final Project for Intro to Computer Programming

This final project is the creation of a bot to be used on Discord. Discord is a voice and text channel software often used by video game players, among others. Quest itself has a server which I administrate in order to schedule tournaments and communicate with teammates. The bot exists as a .py file which, when run, activates the bot in the servers it has access to through the Discord Developer Portal. You should be able to run the file yourself to activate the bot, but it has no functionality outside of the servers it is authorized in. In order to evaluate, I am happy to allow you access to the test discord server that I built the bot on, or to send you images of it performing its function. Please let me know what works. This bot uses the discord.py library, which is publicly available. My primary information came from the following sources:

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
 - !yeet: Kicks a member from the server (!yeet [member.name]) - note that this is not listed in "!intro" because it is an administrator-      only command

The on_message code responds passively to any message which triggers its conditionals. Here are the functioning conditionals:

 - If Michael Lee sends a message, the bot reacts with an angry face emoji

I've set up a test account for you to use in order to evaluate the success of the bot, using my quest email: jacob.richardson@questu.ca
The password for the account is Kermode2, and it is only able to access the test server. I've also given it moderator privileges, so you can run commands that have more serious consequences. If you need anything else, don't hesitate to let me know. This has been a challenging and engaging project, for sure!
