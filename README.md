# Cyoa
Choose Your Own Adventure game for a terminal. Uses custom scripting. You can make your own Script/Story
# Installation
You don't need to install any extra packages you can use out of the box.
First clone the repo from GitHub
```
git clone https://github.com/5h3ll0/cyoa
cd cyoa
```
and run with passing file name or location of the game file(.cyoa)
```
python cyoa.py -g story.cyoa
```


# Scripting
cyoa script is created for Choose Your Own Adventure project and uses .cyoa extension

### Rooms
Your story can contain multiple rooms
Example:

```
[roomname]

Room Data

[/roomname]
[exampleroom]

Room Data

[/exampleroom]
```
You must include one start room **Game starts from there**

And each Room contains two room data

* Room text
* Choices

### Room Text
In each room you should include one room text, this text shows the beginning of the room.
Example:

```
[start]
{
Hello welcome to this game
You can sit here and enjoy your tea while we checking other things
}

[/start]
```
if you run this script you will get this output

```

Hello welcome to this game
You can sit here and enjoy your tea while we checking other things

```

### Choices
Every room should contain at least one choice, these choices referenced with room names
Example:
```
[start]
{
Hello welcome to this game
You can sit here and enjoy your tea while we checking other things
}
(c)
exampleroom:you should definitely choose this one
sketchyroom:Don't go from this way
(/c)
[/start]
```
Output:
```

Hello welcome to this game
You can sit here and enjoy your tea while we checking other things

1)you should definitely choose this one
2)Don't go from this way

Select:
```
### Ending
If you don't put any choices in your room then after printing text, the program automatically exits
```
[escape]
{
You ran away and nothing happened
}
[/escape]
```
### Example Story
Well you learned everything now let's combine all of them an create a little story

```
[start]
{
Welcome you're standing in front of this cave
What would you do
}
(c)
cave:Go into the cave
escape:Runaway
(/c)
[/start]


[cave]
{
You're in the cave now
You're felt something under your foot
}
(c)
take:Take the mysterious thing
flashlight:Try to turn on the flashlight
(/c)
[/cave]


[take]
{
You take plant under your feet
and injured yourself with poisonous spikes
}
(c)

(/c)
[/take]

[flashlight]
{
You turned on the flashlight and saw poisonous plant under your feet
You survived
}
[/flashlight]

[escape]
{
You ran away and nothing happened
}
[/escape]
```
# Playing
Now start game using 
```
python cyoa.py -g story.cyoa
```
This project already has an example game file named story.cyoa
You've should see something like this

```
Welcome you're standing in front of this cave
What would you do

1)Go into the cave
2)Runaway

Select:
```
You should select 1 or 2, write your choice in number and press enter, now if you chose 1 screen cleans and your selected option applies.

```
You're in the cave now
You're felt something under your foot

1)Take the mysterious thing
2)Try to turn on the flashlight

Select:
```
