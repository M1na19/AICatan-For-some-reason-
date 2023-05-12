var OrdineaJucatorilor=[0,1,2,3];
var Settlements=[];
var Cards=[];
var DCards=[];
Cards.push([]);
Settlements.push([]);

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
        let construction={};
        construction.type="town";
        construction.x=5;
        construction.x=4;
        Settlements[i].push(construction);
        // ALEGI CE LOC SA PUI CASA
        // ALEGI SA PUI DRUMUL
    }
    for(var i=OrdineaJucatorilor.length;i>=1;i++)
    {
        let construction={};
        construction.type="town";
        construction.x=5;
        construction.x=4;
        Settlements[i].push(construction);
        let newcard={};
        newcard.type="brick";
        Cards[i].push(newcard);
        newcard={};
        newcard.type="wood";
        Cards[i].push(newcard);
        newcard={};
        newcard.type="wool";
        Cards[i].push(newcard);
        // ALEGI CE LOC SA PUI CASA
        // ALEGI SA PUI DRUMUL
    }
}

OnStartGame();