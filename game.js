var OrdineaJucatorilor=[0,1,2,3];

var p=[2,2,2,2];

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
            showAvialable(get("posibile_asezari"),0);
            showAvialable(get("posibile_drumuri"),0);
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
            showAvialable(get("posibile_asezari"),0);
            showAvialable(get("posibile_drumuri"),0);
        }
        else
        {
            MakeSettlement(get("Ai_start_asezare"),"town",i);
        }
    }
}

function RollDice()
{
    var val1,val2;
    var1=Math.floor(Math.random()*6)+1;
    var1=Math.floor(Math.random()*6)+1;

    document.getElementById("dice1").textContent=val1;
    document.getElementById("dice2").textContent=val2;

    return var1+var2;
}

function TheGame()
{
    var i=0,winner=-1;
    while(winner==-1)
    {
        var newdice=RollDice();
        put("dice",i,newdice);

        i++;i%=4;
    }
}

OnStartGame();