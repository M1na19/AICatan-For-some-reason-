

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
async function pointsData()
{
    for(let i=0;i<nrJucatori;i++)
    {
        const vp=document.getElementById('Player'+(i+1)+'vp')
        vp.textContent="Player"+(i+1)+" has "+await get('visiblePoints',i)+" points"
    }

}
async function TheGame()
{
    while(!await get("gameWon",0))
    {
        for(let i=0;i<nrJucatori;i++)
        {
            await pointsData()
            if(i==0)
            {
                await playerGame(i)
            }
            else
            {
                await zar(i)
                let action=["",""]
                while(action[0]!="pass")
                {
                    new Promise((resolve)=>{setTimeout(()=>{thinking(false),resolve()},2000)}) 
                    action=await get("AIaction",i)
                    thinking(true)
                    await manageAction(action,i)
                    data=await get('playerData',0)
                    showData(data[0],data[1])
                }
                if(document.getElementById('think'))
                    document.getElementById('think').remove()
                await put('pas',i)
            }
        }
    }
}
async function test()
{
    starting=await post(0,4)
    await MakeMap(starting[0])
    for(let i=0;i<starting[1].length;i++)
        if(starting[1][i][1]%2==0)
            MakeSettlement(starting[1][i][0],starting[1][i][1],'town',Math.floor(i/4))
        else
            MakeSettlement(starting[1][i][0],starting[1][i][1],'road',Math.floor(i/4))
    
    
    await TheGame()
}

test()
