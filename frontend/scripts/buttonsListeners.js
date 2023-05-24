async function buttonSendTrade()
{
    sendTrade.addEventListener('click',async ()=>
    {
        await Trade()
    })
}
async function buttonDevelop()
{
    develop.addEventListener('click',async ()=>
    {
        await playerBuyDevelopment()
    })
}
async function buttonUseDevelop()
{
    useDevelop.addEventListener('click',async ()=>
    {
        await develop()
    })
}
async function buttonBuildAsezare()
{
    buildAsezare.addEventListener('click',async ()=>
    {
        await playerPlaceAsezare()
    })
}
async function buttonBuildDrum()
{
    buildDrum.addEventListener('click',async ()=>
    {
        await playerPlaceDrum()
    })
}
async function buttonBuildOras()
{
    buildAsezare.addEventListener('click',async ()=>
    {
        await playerPlaceOras()
    })
}