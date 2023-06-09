
const color='green'
class pozition
{
    constructor(x,y)
    {
        this.x=x
        this.y=y
    }
}

const tile_poz=[new pozition(470,180),new pozition(0,0),new pozition(0,0),new pozition(0,0),new pozition(0,0),new pozition(0,0),new pozition(0,0),new pozition(0,0),new pozition(0,0),new pozition(0,0),new pozition(0,0),new pozition(0,0),new pozition(0,0),new pozition(0,0),new pozition(0,0),new pozition(0,0),new pozition(0,0),new pozition(0,0),new pozition(0,0)]

const distanceEdge=120
const distanceMuchie=104
const horizontalSpacing=3/2*distanceEdge
const verticalSpacing=distanceMuchie*2

//tot cct asta calculeaza centru la hexagoane pt toate hexagoanele
for(let i=1;i<=2;i++)
{
    tile_poz[i].x=tile_poz[i-1].x+verticalSpacing
    tile_poz[i].y=tile_poz[i-1].y
}
tile_poz[3].x=tile_poz[0].x-distanceMuchie
tile_poz[3].y=tile_poz[0].y+horizontalSpacing
for(let i=4;i<=6;i++)
{
    tile_poz[i].x=tile_poz[i-1].x+verticalSpacing
    tile_poz[i].y=tile_poz[i-1].y
}
tile_poz[7].x=tile_poz[3].x-distanceMuchie
tile_poz[7].y=tile_poz[3].y+horizontalSpacing
for(let i=8;i<=11;i++)
{
    tile_poz[i].x=tile_poz[i-1].x+verticalSpacing
    tile_poz[i].y=tile_poz[i-1].y
}
tile_poz[12].x=tile_poz[7].x+distanceMuchie
tile_poz[12].y=tile_poz[7].y+horizontalSpacing
for(let i=13;i<=15;i++)
{
    tile_poz[i].x=tile_poz[i-1].x+verticalSpacing
    tile_poz[i].y=tile_poz[i-1].y
}
tile_poz[16].x=tile_poz[12].x+distanceMuchie
tile_poz[16].y=tile_poz[12].y+horizontalSpacing
for(let i=17;i<=18;i++)
{
    tile_poz[i].x=tile_poz[i-1].x+verticalSpacing
    tile_poz[i].y=tile_poz[i-1].y
}

const angle_to_piece=[270,300,330,0,30,60,90,120,150,180,210,240]//unghi din centru la piesa
const anglePieces=[0,30,0,90,0,-30,0,30,0,90,-30]//unghi al drumurilor

var buttons=[]
var pozbuttons=[]
var chosedPosition=NaN
function tile_to_space(tile,piece)//transforma din format (tile,piece) in (x,y)
{
    var x,y;
    radAngle=angle_to_piece[piece]*(Math.PI/180)
    if(piece%2==0)
    {
        x=tile_poz[tile].x+Math.cos(radAngle)*distanceEdge
        y=tile_poz[tile].y+Math.sin(radAngle)*distanceEdge
    }
    else
    {
        x=tile_poz[tile].x+Math.cos(radAngle)*distanceMuchie
        y=tile_poz[tile].y+Math.sin(radAngle)*distanceMuchie
    }
    return ({x:x,y:y})
}

function edgeClicked(button,player_turn)//colt apasat
{
    let index = Array.prototype.indexOf.call(buttons, button);
    MakeSettlement(pozbuttons[index][0],pozbuttons[index][1],"town",player_turn)
    destroyPieces()
    chosedPosition=pozbuttons[index]
}
function muchieClicked(button,player_turn)//linie apasata
{
    let index = Array.prototype.indexOf.call(buttons, button);
    MakeSettlement(pozbuttons[index][0],pozbuttons[index][1],"road",player_turn)
    destroyPieces()
    chosedPosition=pozbuttons[index]
}


function giveDrumStyle(piece,x,y,angle)//style pt drum
{
    piece.style.height='20px'
    piece.style.width='60px'
    piece.style.position='absolute'
    piece.style.top=y+50+'px'
    piece.style.left=x+20+'px'
    piece.style.backgroundColor=color
    piece.style.transform="rotate("+angle+"deg)"
    piece.style.zIndex="10000"
    flashButton(piece,50)
}



function giveAsezareStyle(piece,x,y)//style pt asezare
{
    piece.style.height='30px'
    piece.style.width='30px'
    piece.style.position='absolute'
    piece.style.top=y+40+'px'
    piece.style.left=x+35+'px'
    piece.style.backgroundColor=color
    piece.style.zIndex="10000"
    flashButton(piece,50)
}


function giveOrasStyle(piece,x,y)
{
    piece.style='border-radius: 50%; width: 80px; height: 80px;'
    piece.style.position='absolute'
    piece.style.top=y+20+'px'
    piece.style.left=x+7+'px'
    piece.style.backgroundColor="white"
    piece.style.zIndex="10000"
    flashButtonOras(piece,50,50)
}
//face button sa fie flashy
async function flashButton(button, duration) {
    let opacity=100
    let opacityDir=0.5
    let offset=0
    while (document.contains(button)) {
        if(opacity<=0 || opacity>=100)
        {
            opacityDir*=-1
            offset*=-1
        }
        else if(Math.sign(opacityDir)==-1 && opacity<=95)
            offset=-10
        else if(opacity>=95)
            offset=0
        opacity+=opacityDir+offset
        button.style.opacity=opacity+"%"
      await new Promise(resolve => setTimeout(resolve, duration));
    }
  }
  //ii dau overload la functie pt oras
  async function flashButtonOras(button, duration,maxopacity) {
    let opacity=maxopacity
    let opacityDir=0.5
    let offset=0
    while (document.contains(button)) {
        if(opacity<=0 || opacity>=maxopacity)
        {
            opacityDir*=-1
            offset*=-1
        }
        else if(Math.sign(opacityDir)==-1 && opacity<=maxopacity-5)
            offset=-10
        else if(opacity>=maxopacity-5)
            offset=0
        opacity+=opacityDir+offset
        button.style.opacity=opacity+"%"
      await new Promise(resolve => setTimeout(resolve, duration));
    }
  }
async function showAvialable(poz,player_turn,can_abandon)
{
    //am ca input un sir cu poz[i] de tipul {tile,piece(adica indexu pe tile)}
    if(poz.length==0)
    {    
        chosedPosition=NaN
        return
    }
    console.log(poz)
    buttons.length=0
    pozbuttons.length=0
    for(let i=0;i<poz.length;i++)
    {
        let point=tile_to_space(poz[i][0],poz[i][1])
        buttons.push(document.createElement("button"))
        pozbuttons.push(poz[i])

        if(poz[i][1]%2==0)//pt asezari
        {
            document.querySelector('.asezare').appendChild(buttons[i])
            giveAsezareStyle(buttons[i],point.x,point.y)
        }
        else//pt drumuri
        {
            document.querySelector('.drum').appendChild(buttons[i])
            giveDrumStyle(buttons[i],point.x,point.y,anglePieces[poz[i][1]])
        }
    }
    await new Promise((resolve)=>
    {
        let exit=NaN
        if(can_abandon==true)
        {
            exit=makeExit("ABANDON")
            exit.addEventListener('click',()=>
            {
                exit.remove()
                destroyPieces()
                resolve()
            })
        }        
        for(let i=0;i<poz.length;i++)
        {
            if(pozbuttons[i][1]%2==0)
            {
                buttons[i].addEventListener('click',()=>
                {
                    edgeClicked(buttons[i],player_turn)
                    if(exit)
                    {
                        exit.remove()
                    }
                    resolve()
                })
            }
            else
            {
                buttons[i].addEventListener('click',()=>
                {
                    muchieClicked(buttons[i],player_turn)
                    if(exit)
                    {
                        exit.remove()
                    }
                    resolve()
                })
            }
        }
        

    })
}
async function showUpgradable(poz)
{
    if(poz.length==0)
    {    
        chosedPosition=NaN
        return
    }
    buttons.length=0
    pozbuttons.length=0
    for(let i=0;i<poz.length;i++)
    {
        var point=tile_to_space(poz[i][0],poz[i][1])
        buttons.push(document.createElement("button"))
        document.querySelector('.oras').appendChild(buttons[i])
        giveOrasStyle(buttons[i],point.x,point.y)
        buttons[i].addEventListener("click",function(event){
            showing=false;
            updateSettlement(point.x,point.y)
            destroyPieces()
            chosedPosition=pozbuttons[index]
        })
    }
}
function makeExit(text)
{
    let exit=document.createElement("button");
    exit.classList.add('button')
    document.body.appendChild(exit);

    exit.style.position="absolute"
    exit.style.height="100px"
    exit.style.width="200px"
    exit.textContent=text;
    exit.style.color="black"
    exit.style.fontFamily = 'Arial, sans-serif';
    exit.style.top="1000px"
    exit.style.left="2400px"
    return exit;
}
function destroyPieces()//la final distrug toate piesele
{
    buttons.forEach(element => {
        element.remove()
    });
    buttons.slice(0)
    pozbuttons.slice(0)
}