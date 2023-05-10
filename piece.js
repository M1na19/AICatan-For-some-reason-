
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
//trb sa pun pt fiecare sa calculez
const distanceEdge=120
const distanceMuchie=104
const horizontalSpacing=3/2*distanceEdge
const verticalSpacing=distanceMuchie*2

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

const angle_to_piece=[270,300,330,0,30,60,90,120,150,180,210,240]
const anglePieces=[0,30,0,90,0,-30,0,30,0,90,-30]

var buttons=[]
var pozbuttons=[]
function tile_to_space(tile,piece)
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
function edgeClicked(button)
{
    let index = Array.prototype.indexOf.call(buttons, button);
    MakeSettlement(pozbuttons[index].tile,pozbuttons[index].piece,"town",player_turn)
    destroyPieces()
}
function muchieClicked(button)
{
    let index = Array.prototype.indexOf.call(buttons, button);
    MakeSettlement(pozbuttons[index].tile,pozbuttons[index].piece,"road",player_turn)
    destroyPieces()
}


function giveDrumStyle(piece,x,y,angle)
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



function giveAsezareStyle(piece,x,y)
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
let opacity=100
let opacityDir=0.5
let offset=0
async function flashButton(button, duration) {
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


function showAvialable(poz)
{
    //am ca input un sir cu poz[i] de tipul {tile,piece(adica indexu pe tile)}
    for(let i=0;i<poz.length;i++)
    {
        var point=tile_to_space(poz[i].tile,poz[i].piece)
        buttons.push(document.createElement("button"))
        pozbuttons.push(poz[i])
        //aici calculez unde se afla fata de centru hexagonului si creez butoane care asculta

        if(poz[i].piece%2==0)//pt asezari
        {
            document.querySelector('.asezare').appendChild(buttons[i])
            giveAsezareStyle(buttons[i],point.x,point.y)
            
            buttons[i].addEventListener("click",function(event){
                edgeClicked(event.target)
            })
        }
        else//pt drumuri
        {
            document.querySelector('.drum').appendChild(buttons[i])
            giveDrumStyle(buttons[i],point.x,point.y,anglePieces[poz[i].piece])

            buttons[i].addEventListener("click",function(event){
                muchieClicked(event.target)
            })
        }
    }
}
function showUpgradable()
{

}
function destroyPieces()//la final distrug toate piesele
{
    buttons.forEach(element => {
        element.remove()
    });
}