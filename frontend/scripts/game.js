
var p=[2,2,2,2];
var nrJucatori=4;
async function OnStartGame()
{
    for(var i=0;i<nrJucatori;i++)
    {
        if(i==0)
        {
            await showAvialable(get("posibile_asezari"),0);
            await showAvialable(get("posibile_drumuri"),0);
        }
        else
        {
            MakeSettlement(get("Ai_start_asezare"),"town",i);
        }
    }
    for(var i=nrJucatori-1;i>=1;i++)
    {
        if(i==0)
        {
            await showAvialable(get("posibile_asezari"),0);
            await showAvialable(get("posibile_drumuri"),0);
        }
        else
        {
            MakeSettlement(get("Ai_start_asezare"),"town",i);
        }
    }
}

function TheGame()
{

}
async function test()
{
    await showAvialable([{tile:0,piece:2},0]);
    console.log("jel")
}
test()
//OnStartGame();