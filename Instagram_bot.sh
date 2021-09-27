#!/bin/bash

xdg-open https://www.instagram.com/accounts/edit/ &

sleep 3

x=1
while [ $x -le 17 ]
do
  #echo "$x times"
  x=$(( $x + 1 ))
  xdotool key 'Tab'
done

xdotool key 'Ctrl'+'End'
xdotool key 'Shift'+'Ctrl'+'Home'
xdotool type "When I in dreams behold thy fairest shade
In them doth wake the sleeping morn
The daytime shadow of my love betray'd
Lends night to dreams faded form"

x=1
while [ $x -le 6 ]
do
  x=$(( $x + 1 ))
  xdotool key 'Tab'
done

xdotool key 'Enter'

sleep 0.5

xdotool key 'Ctrl'+w                              