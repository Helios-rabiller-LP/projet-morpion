pos= (".........")
player= X

render()
{ 
 echo 
 +---------+
 ("|${pos[7]}|{pos[8]}|{pos[9]}|")
 ("|${pos[7]}|{pos[8]}|{pos[9]}|")
 ("|${pos[7]}|{pos[8]}|{pos[9]}|")
 +---------+
 Player $;player 
 }

render

while [1];do
    read -rsn1 p
    pos[$p]=$player
    echo -en "\033[10D\033[10A"
    if [$player == "X"]
    then
        player=0
    else:
        player=X
    fi
    render
    
done
        