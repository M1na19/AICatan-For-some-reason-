const backgroundstyle="position: absolute; top:0%; height:100%; width:100%;color:green"

const dice=document.querySelector('#diceButton')
const develop=document.querySelector('#developButton')
const buildAsezare=document.querySelector("#asezareButton");
const buildOras=document.querySelector("#orasButton");
const buildDrum=document.querySelector("#drumButton");
const sendTrade=document.querySelector("#sendTrade");
const pass=document.querySelector("#passButton");
var acceptTrade=document.querySelector('#acceptTradeButton')

function sum(list)
{
    let x=0
    for(let i=0;i<list.length;i++)
    {
        x+=list[i];
    }
    return x;
}
function frecvToIter(list)
{
    let modified=[]
    for(let i=0;i<list.length;i++)
    {
        for(let j=0;j<list[i];j++)
        {
            modified.push(i);
        }
    }
    return modified;
}
function removeEventListeners(buton)
{
    let copy=buton.cloneNode()
    buton.replaceWith(copy)
}
async function flashHexagon(hex)
{
    let opacity=50;
    let increment=-2;
    let maxopacity=50;
    while(document.contains(hex))
    {
        if(opacity<=0)
        {
            increment=2;
        }
        else if(opacity>maxopacity)
        {
            increment=-2;
        }
        opacity+=increment;
        hex.style.opacity=(opacity+increment)+"%";
        await new Promise((resolve) => {
            setTimeout(resolve,50)
        })
    }
}
async function Trade()
{
    //Mache
}
async function development()
{
    //Mache
}
async function moveThief(can_abandon)
{
    //const pozThief=await get("pozThief",-1);
    var exit;
    if(can_abandon)
    {
        exit=makeExit()
        exit.addEventListener('click',()=>
        {
            for(let i=0;i<buttons.length;i++)
            {
                buttons[i].remove();
            }
            exit.remove()
            resolve()
        })
    }
    const pozThief=9;
    let buttons=[]
    for(let i=0;i<19;i++)
    {
        if(i!=pozThief)
        {
            const thiefButton=document.createElement('button');
            const theImage=document.createElement('img');
            thiefButton.style="position:absolute; top:"+(tile_poz[i].y-20)+"px; left:"+(tile_poz[i].x-20)+"px;height:150px;width:150px;z-index:10";thiefButton.style.backgroundColor="transparent";thiefButton.style.border="none";
            theImage.src="images/hexagon.png"
            theImage.style="height:250px; width:250px;top:-50px;left:-50px;z-index:-1;";theImage.style.rotate="30deg";
            buttons.push(thiefButton);
            document.body.appendChild(thiefButton);
            thiefButton.appendChild(theImage);
            flashHexagon(theImage);
        }
    }
    var tileChosed=-1;
    await new Promise((resolve) => {
      for(let i=0;i<18;i++)
      {
        buttons[i].addEventListener('click',async ()=>
        {
            tileChosed=i;
            //await put("moveThief",-1,tileChosed)//doesnt matter player
            for(let i=0;i<18;i++)
            {
                buttons[i].remove();
            }
            if(can_abandon)
                exit.remove();
            resolve()
        })
      }  
    })
    return tileChosed;
}
async function steal(tile,player)
{
    //optionPlayers=await get("playerInTile",player)
    let optionPlayers=[1,0,1,1]
    let buttons=[]
    showDice(4,5)
    lockMenu()
    const stealPage=document.createElement('div');stealPage.style.zIndex="10001"
    document.body.appendChild(stealPage);
    

    const background=document.createElement('img');
    background.style=backgroundstyle;
    background.src="images/background.png"
    stealPage.appendChild(background);

    const distanceBetweenPlayers=window.screen.width/(sum(optionPlayers)+1)+300;
    var lastPlaced=-500

    for (let i=0;i<sum(optionPlayers);i++)
    {
        lastPlaced+=distanceBetweenPlayers;
        const spotLight=document.createElement('img');spotLight.src="images/spotlight.png"
        const buttonPlayer=document.createElement('button');
        const indx=document.createElement('p');indx.textContent=frecvToIter(optionPlayers)[i]+1;

        spotLight.style="position:absolute; left:"+lastPlaced+"px ; top:400px; height:800px; width: auto;"

        buttonPlayer.style="position:absolute; left:"+(lastPlaced+200)+"px; top:60%; height:200px; width: 200px"
        buttonPlayer.style.backgroundImage = "url('images/player.png')";
        buttonPlayer.style.backgroundSize = "cover";
        buttonPlayer.style.zIndex = "10";
        buttonPlayer.style.backgroundColor="transparent"
        buttonPlayer.style.borderBlockColor="transparent"

        indx.style="position: absolute; top:80%;left:"+(lastPlaced+250)+"px;z-index:10;"
        indx.style.fontSize="100px"
        indx.style.color="white"
        

        buttons.push(buttonPlayer)

        stealPage.appendChild(spotLight);
        stealPage.appendChild(buttonPlayer);
        stealPage.appendChild(indx)

        

    }
    await new Promise((resolve)=>
    {
        for(let i=0;i<buttons.length;i++)
        {
            let otherplayer=frecvToIter(optionPlayers)[i];
            buttons[i].addEventListener('click',async ()=>
            {
                //await put("steal",player,otherplayer)
                stealPage.remove()
                resolve()
            })
        }
    })
    unlockMenu()
}
async function discard()
{
    //nu depinde de player
}
async function tradeProposal(cardsReceived,cardsGiven,player)
{
    openNav()
    const namePlayer=document.querySelector('#TradePlayerName')
    namePlayer.textContent="Trade from: player "+player
    const yw=[document.querySelector('#ywwood'),document.querySelector('#ywbrick'),document.querySelector('#ywgrain'),document.querySelector('#ywwool'),document.querySelector('#ywore')]
    const yl=[document.querySelector('#ylwood'),document.querySelector('#ylbrick'),document.querySelector('#ylgrain'),document.querySelector('#ylwool'),document.querySelector('#ylore')]
    for(let i=0;i<cardsReceived.length;i++)
    {
        yw[i].textContent=cardsReceived[i]
    }
    for(let i=0;i<cardsGiven.length;i++)
    {
        yl[i].textContent=cardsGiven[i]
    }
    await new Promise((resolve) => {
        setTimeout(()=>
        {
            namePlayer.textContent="Trade from: None"
            for(let i=0;i<cardsReceived.length;i++)
            {
                yw[i].textContent=0
            }
            for(let i=0;i<cardsGiven.length;i++)
            {
                yl[i].textContent=0
            }
            removeEventListeners(acceptTrade);
            acceptTrade=document.querySelector('#acceptTradeButton');
            acceptTrade.textContent="ACCEPT TRADE"
            resolve()
        },20000)
        acceptTrade.addEventListener('click',async()=>
        {
            //await put("playersTrade")
            namePlayer.textContent="Trade from: None"
            for(let i=0;i<cardsReceived.length;i++)
            {
                yw[i].textContent=0
            }
            for(let i=0;i<cardsGiven.length;i++)
            {
                yl[i].textContent=0
            }
            removeEventListeners(acceptTrade);
            acceptTrade=document.querySelector('#acceptTradeButton');
            acceptTrade.textContent="ACCEPT TRADE"
            resolve()
        })
        
    })


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
async function playerBuyDevelopment(player)
{
    if(typeof(await get("getDezv",player))==="number")
    {
        //warning tab
    }
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