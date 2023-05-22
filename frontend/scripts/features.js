const dice=document.querySelector('zarButton')
const develop=document.querySelector('developButton')
const buildAsezare=document.querySelector("asezareButton");
const buildOras=document.querySelector("orasButton");
const buildDrum=document.querySelector("drumButton");
const sendTrade=document.querySelector("sendTrade");
const pass=document.querySelector("passButton");
async function Trade()
{

}
async function development()
{

}
async function moveThief()
{

}
async function steal()
{

}
async function discard()
{
    //nu depinde de player
}
async function tradeProposal()
{
    //doar pe tura altora
}
function lockMenu()
{
    closeNav()
    menuIsLocked=true
}
function unlockMenu()
{
    menuIsLocked=false;
}
async function playerPlaceDrum()
{
    lockMenu();
    await showAvialable(await get("possibleDrum",player));
    await put('placePiece',player,chosedPosition);
    unlockMenu()
}
async function playerPlaceAsezare()
{
    lockMenu();
    await showAvialable(await get("possibleAsezare",player));
    await put('placePiece',player,chosedPosition);
    unlockMenu()
}
async function playerPlaceOras()
{
    lockMenu();
    await showUpgradable(await get("possibleOras",player));
    await put('placePiece',player,chosedPosition);
    unlockMenu()
}
async function zar()
{
    showDice(await get('zar',0))//doesnt matter player
}

async function playerGame(player)
{
    showData(await(get('playerData',player)))

    await new Promise((resolve)=>{
        dice.addEventListener('click',async ()=>
        {
            await zar()
            resolve()
        })
    })

    showData(await(get('playerData',player)))

    return new Promise((resolve) => {
        develop.sendTrade('click',async ()=>
        {
            await sendTrade()
        })
        develop.addEventListener('click',async ()=>
        {
            await develop()
        })
        buildAsezare.addEventListener('click',async ()=>
        {
            await playerPlaceAsezare()
        })
        buildDrum.addEventListener('click',async ()=>
        {
            await playerPlaceDrum()
        })
        buildAsezare.addEventListener('click',async ()=>
        {
            await playerPlaceOras()
        })
        pass.addEventListener('click', () => {
          resolve();
        });
      });
}
function showDice()
{

}
function showData()
{

}