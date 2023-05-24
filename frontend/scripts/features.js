const backgroundstyle="position: absolute; top:0%; height:100%; width:100%;color:green"

var dice=document.querySelector('#diceButton')
var develop=document.querySelector('#developButton')
var useDevelop=document.querySelector('#useDevelopButton');
var buildAsezare=document.querySelector("#asezareButton");
var buildOras=document.querySelector("#orasButton");
var buildDrum=document.querySelector("#drumButton");
var sendTrade=document.querySelector("#sendTrade");
var pass=document.querySelector("#passButton");
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
function iterToFrecv(list)
{
    let modified=[0,0,0,0,0]
    for(let i=0;i<list.length;i++)
    {
        modified[list[i]]++;
    }
    return modified;
}
function hoverIluminate(button)
{
    button.addEventListener('mouseover',()=>
    {
        button.style.border="2px solid white"
    })
    button.addEventListener('mouseout',()=>
    {
        button.style.border="None"
    })
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
async function Trade(player)
{
    getTradecardsYouwant()
    const player2=NaN;
    await new Promise(async (resolve) => {
        let resources=[0,0,0,0,0];
        for(let i=0;i<cardloc.length;i++)
        {
            if(parseInt(cardloc[i].html.style.top)>445 && parseInt(cardloc[i].html.style.top)<875 && parseInt(cardloc[i].html.style.left)>700 && parseInt(cardloc[i].html.style.left)<1190)
            {
                if(cardloc[i].mat=="wood")resources[0]++;
                if(cardloc[i].mat=="wool")resources[3]++;
                if(cardloc[i].mat=="ore")resources[4]++;
                if(cardloc[i].mat=="brick")resources[1]++;
                if(cardloc[i].mat=="grain")resources[2]++;
            }
        }
        await put("proposalTrade",player,player2,resources,tradecards);
    })
}
async function development(player)
{
    let first=-1
    for(let i=0;i<scardloc.length;i++)
    {
      if(parseInt(scardloc[i].html.style.top)>445 && parseInt(scardloc[i].html.style.top)<875 && parseInt(scardloc[i].html.style.left)>700 && parseInt(scardloc[i].html.style.left)<1190)
      {
        if(scardloc[i].mat=="LIB"){first=0;break;}
        if(scardloc[i].mat=="YOP"){first=1;break;}
        if(scardloc[i].mat=="RBD"){first=2;break;}
        if(scardloc[i].mat=="KNG"){first=3;break;}
        if(scardloc[i].mat=="MNP"){first=4;break;}
      }
    }

    switch (first)
    {
        case 0:
        {
            //anounce u have one victory point
        }
        case 1:
        {
            await new Promise(async (resolve) => {
                freezeMenu()
                sendTrade=document.querySelector("#sendTrade");
                sendTrade.textContent="CHOOSE 2 GAINED RESOURCES"
                sendTrade.addEventListener('click',async ()=>
                {
                    getTradecardsYouwant()
                    if(sum(tradecards)==2)
                    {
                        //await put("gain2Resources",tradecards)
                        resolve();
                    }
                    else
                    {
                        //warning message
                    }
                })
                setTimeout(resolve,15000);
            });
            freezeMenu();
            unfreezeMenu();
            buttonSendTrade();
            break;
        }
        case 2:
        {
            await new Promise(async (resolve) => {
                await showAvialable(await get('possibleDrumuri',player),player,true)
                if(chosedPosition==NaN)
                {
                    resolve()
                }
                await showAvialable(await get('possibleDrumuri',player),player,false)
                resolve()
            })
        }
        case 3:
        {
            await new Promise(async (resolve) => {
                let tile=await moveThief(true);
                if(tile>=0)
                {
                    await steal(tile,player);
                }
                resolve()
            })
            break;
        }
        case 4:
        {
            await new Promise(async (resolve) => {
                await monopol()
            })
        }
    }
    
}
async function moveThief(can_abandon)
{
    //const pozThief=await get("pozThief",-1);
    var exit;
    if(can_abandon)
    {
        exit=makeExit("ABANDON")
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
    background.src="https://i.imgur.com/PXGHWnl.png"
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
async function discard(nrCards,player)
{
    freezeMenu()
    //warn discard
    await new Promise(async (resolve) => {
        let notClicked=true;
        useDevelop.addEventListener('click',async ()=>
        {
            let resources=[0,0,0,0,0];
            for(let i=0;i<cardloc.length;i++)
            {
                if(parseInt(cardloc[i].html.style.top)>445 && parseInt(cardloc[i].html.style.top)<875 && parseInt(cardloc[i].html.style.left)>700 && parseInt(cardloc[i].html.style.left)<1190)
                {
                    if(cardloc[i].mat=="wood")resources[0]++;
                    if(cardloc[i].mat=="wool")resources[3]++;
                    if(cardloc[i].mat=="ore")resources[4]++;
                    if(cardloc[i].mat=="brick")resources[1]++;
                    if(cardloc[i].mat=="grain")resources[2]++;
                }
            }
            if(sum(resources)==nrCards)
            {
                //await put('discard',player,)
                notClicked=false;
                resolve()
            }
        })
        while(notClicked)
        {
            let resources=[0,0,0,0,0];
            for(let i=0;i<cardloc.length;i++)
            {
                if(parseInt(cardloc[i].html.style.top)>445 && parseInt(cardloc[i].html.style.top)<875 && parseInt(cardloc[i].html.style.left)>700 && parseInt(cardloc[i].html.style.left)<1190)
                {
                    if(cardloc[i].mat=="wood")resources[0]++;
                    if(cardloc[i].mat=="wool")resources[3]++;
                    if(cardloc[i].mat=="ore")resources[4]++;
                    if(cardloc[i].mat=="brick")resources[1]++;
                    if(cardloc[i].mat=="grain")resources[2]++;
                }
            }
            useDevelop.textContent="DISCARD ("+(nrCards-sum(resources))+")"
            await new Promise((innerresolve)=>{setTimeout(innerresolve,100)});
        }
    })
    freezeMenu()
    unfreezeMenu()
}
async function monopol(player)
{
    const monopolScreen=document.createElement('div');
    monopolScreen.style="position:absolute;z-index:100; height:800px; width:1375px;top:300px;left:600px"
    monopolScreen.style.backgroundImage="url(https://i.imgur.com/PXGHWnl.png)";monopolScreen.style.backgroundSize="cover"
    document.body.appendChild(monopolScreen);
    const lemn=document.createElement('button');
    const argila=document.createElement('button');  
    const oaie=document.createElement('button');
    const fan=document.createElement('button');
    const piatra=document.createElement('button');
    const buttonStyle="border:none;background-color:transparent; position:absolute;z-index:10; height:344px; width:225px;top:250px; background-size:cover;"
    lemn.style=argila.style=oaie.style=fan.style=piatra.style=buttonStyle;
    lemn.style.backgroundImage="url(https://i.imgur.com/amAWx6q.png)";argila.style.backgroundImage="url(https://i.imgur.com/jldnqDd.png)";fan.style.backgroundImage="url(https://i.imgur.com/KILdl8B.png)";oaie.style.backgroundImage="url(https://i.imgur.com/CEl8Sij.png)";piatra.style.backgroundImage="url(https://i.imgur.com/l9yIY2E.png)"; 
    lemn.style.left="75px";
    argila.style.left="325px";
    fan.style.left="575px";
    oaie.style.left="825px";
    piatra.style.left="1075px";
    hoverIluminate(lemn);hoverIluminate(argila);hoverIluminate(oaie);hoverIluminate(fan);hoverIluminate(piatra);
    monopolScreen.appendChild(lemn);monopolScreen.appendChild(argila);monopolScreen.appendChild(fan);monopolScreen.appendChild(oaie);monopolScreen.appendChild(piatra);
    let exit=makeExit("ABANDON");
    await new Promise((resolve) => {
        lemn.addEventListener('click',async ()=>
        {
            await put('monopol',player,0)
            resolve()
        })
        argila.addEventListener('click',async ()=>
        {
            await put('monopol',player,1)
            resolve()
        })
        oaie.addEventListener('click',async ()=>
        {
            await put('monopol',player,3)
            resolve()
        })
        fan.addEventListener('click',async ()=>
        {
            await put('monopol',player,2)
            resolve()
        })
        piatra.addEventListener('click',async ()=>
        {
            await put('monopol',player,4)
            resolve()
        })
        exit.addEventListener('click',async ()=>
        {
            exit.remove()
            resolve()
        })
    })
    monopolScreen.remove()
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
function freezeMenu()
{
    const textDevelop="USE DEVELOPMENT";
    const textTrade="SEND TRADE";
    openNav()
    removeEventListeners(useDevelop);
    useDevelop=document.querySelector('#useDevelopButton')
    useDevelop.textContent=textDevelop;

    removeEventListeners(develop);
    develop=document.querySelector('#developButton')
    
    removeEventListeners(buildAsezare);
    buildAsezare=document.querySelector("#asezareButton");

    removeEventListeners(buildOras)
    buildOras=document.querySelector("#orasButton");

    removeEventListeners(buildDrum)
    buildDrum=document.querySelector("#drumButton");

    removeEventListeners(sendTrade);
    sendTrade=document.querySelector("#sendTrade");
    sendTrade.textContent=textTrade;
    
    menuIsFrezzed=true
}
function unfreezeMenu()
{
    buttonUseDevelop()
    buttonBuildAsezare()
    buttonBuildDrum()
    buttonDevelop()
    buttonBuildOras()
    buttonSendTrade()
    menuIsFrezzed=false;
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
    const pass=makeExit('PASS')
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
        buttonSendTrade();
        buttonDevelop()
        buttonBuildAsezare()
        buttonBuildDrum()
        buttonBuildOras()
        
        pass.addEventListener('click', () => {
          resolve();
        });
      });
}