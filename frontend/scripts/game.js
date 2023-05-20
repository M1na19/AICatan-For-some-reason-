

var nrJucatori=4;
async function OnStartGame()
{
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
        }
        else
        {
            let AIChosed=await get("Ai_start_asezare");
            MakeSettlement(AIChosed,"town",i);
        }

    }
}

function TheGame()
{

}
async function test()
{
    await showAvialable([{tile:0,piece:2}],0,true);
    console.log("jel")
}
test()
//OnStartGame();