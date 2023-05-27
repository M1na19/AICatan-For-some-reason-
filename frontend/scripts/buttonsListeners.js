async function buttonSendTrade()
{
    sendTrade.addEventListener('click',async ()=>
    {
        await Trade(0)
        data=await get('playerData',0)
        showData(data[0],data[1])

    })
}
async function buttonDevelop()
{
    develop.addEventListener('click',async ()=>
    {
        await playerBuyDevelopment(0)
        data=await get('playerData',0)
        showData(data[0],data[1])

    })
}
async function buttonUseDevelop()
{
    useDevelop.addEventListener('click',async ()=>
    {
        await development(0)
        data=await get('playerData',0)
        showData(data[0],data[1])

    })
}
async function buttonBuildAsezare()
{
    buildAsezare.addEventListener('click',async ()=>
    {
        await playerPlaceAsezare(0)
        data=await get('playerData',0)
        showData(data[0],data[1])

    })
}
async function buttonBuildDrum()
{
    buildDrum.addEventListener('click',async ()=>
    {
        await playerPlaceDrum(0)
        data=await get('playerData',0)
        showData(data[0],data[1])

    })
}
async function buttonBuildOras()
{
    buildOras.addEventListener('click',async ()=>
    {
        await playerPlaceOras(0)
        data=await get('playerData',0)
        showData(data[0],data[1])

    })
}