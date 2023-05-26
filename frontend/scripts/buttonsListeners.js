async function buttonSendTrade()
{
    sendTrade.addEventListener('click',async ()=>
    {
        await Trade()
        showData(await(get('playerData',player)))

    })
}
async function buttonDevelop()
{
    develop.addEventListener('click',async ()=>
    {
        await playerBuyDevelopment()
        showData(await(get('playerData',player)))

    })
}
async function buttonUseDevelop()
{
    useDevelop.addEventListener('click',async ()=>
    {
        await development()
        showData(await(get('playerData',player)))

    })
}
async function buttonBuildAsezare()
{
    buildAsezare.addEventListener('click',async ()=>
    {
        await playerPlaceAsezare()
        showData(await(get('playerData',player)))

    })
}
async function buttonBuildDrum()
{
    buildDrum.addEventListener('click',async ()=>
    {
        await playerPlaceDrum()
        showData(await(get('playerData',player)))

    })
}
async function buttonBuildOras()
{
    buildAsezare.addEventListener('click',async ()=>
    {
        await playerPlaceOras()
        showData(await(get('playerData',player)))

    })
}