

var nrJucatori=4;
async function OnStartGame()
{
    lockMenu()
    for(var i=0;i<nrJucatori;i++)
    {
        if(i==0)
        {
            await showAvialable(await get("posibile_asezari",i),0,false);
            await showAvialable(await get("posibile_drumuri",i),0,false);
            await put("place_piece",0,chosedPosition);
        }
        else
        {
            MakeSettlement(await get("Ai_start_asezare",i),"town",i);
        }
    }
    for(var i=nrJucatori-1;i>=1;i++)
    {
        if(i==0)
        {
            await showAvialable(await get("posibile_asezari",i),0,false);
            await showAvialable(await get("posibile_drumuri",i),0,false);
            await put("place_piece",0,chosedPosition); 
            unlockMenu()
        }
        else
        {
            let AIChosed=await get("Ai_start_asezare",i);
            MakeSettlement(AIChosed,"town",i);
        }

    }
}

async function TheGame()
{
    while(await get("gameWon",0))
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
    await post(0,4)
    await TheGame()
}

test()
