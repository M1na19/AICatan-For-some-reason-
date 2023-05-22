

var nrJucatori=4;
async function OnStartGame()
{
    lockMenu()
    for(var i=0;i<nrJucatori;i++)
    {
        if(i==0)
        {
            await showAvialable(await get("posibile_asezari"),0,false);
            await showAvialable(await get("posibile_drumuri"),0,false);
            await put("place_piece",0,chosedPosition);
        }
        else
        {
            MakeSettlement(await get("Ai_start_asezare"),"town",i);
        }
    }
    for(var i=nrJucatori-1;i>=1;i++)
    {
        if(i==0)
        {
            await showAvialable(await get("posibile_asezari"),0,false);
            await showAvialable(await get("posibile_drumuri"),0,false);
            await put("place_piece",0,chosedPosition); 
            unlockMenu()
        }
        else
        {
            let AIChosed=await get("Ai_start_asezare");
            MakeSettlement(AIChosed,"town",i);
        }

    }
}

async function TheGame()
{
    while(await get("gameWon"))
    {
        for(let i=0;i<=nrJucatori;i++)
        {
            if(i==0)
            {
                await playerGame()
            }
            else
            {
                let action=""
                while(action!="pas")
                {
                    action=await get("AIaction")
                    manageAction(action)
                }
            }
        }
    }
}
async function test()
{
    lockMenu()
    await showAvialable([{tile:0,piece:2},{tile:0,piece:3}],0,true);
    unlockMenu()
    console.log("jel")
}
test()
//await OnStartGame();
//await TheGame()