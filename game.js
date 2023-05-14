var OrdineaJucatorilor=[0,1,2,3];

function shuffle(array)
{
    let OrdineaJucatorilor = array.length,randomIndex;
    while (currentIndex != 0) {
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;
      [array[currentIndex], array[randomIndex]]=[array[randomIndex], array[currentIndex]];
    }
    return array;
}

function OnStartGame()
{
    shuffle(OrdineaJucatorilor);
    for(var i=1;i<=OrdineaJucatorilor.length;i++)
    {
        if(i==0)
        {
            showAvailable(get("posibile_asezari"),0);
            showAvailable(get("posibile_drumuri"),0);
        }
        else
        {
            MakeSettlement(get("Ai_start_asezare"),"town",i);
        }
    }
    for(var i=OrdineaJucatorilor.length;i>=1;i++)
    {
        if(i==0)
        {
            showAvailable(get("posibile_asezari"),0);
            showAvailable(get("posibile_drumuri"),0);
        }
        else
        {
            MakeSettlement(get("Ai_start_asezare"),"town",i);
        }
    }
}

OnStartGame();