var tiles = [];
var cardvector = [];
var cardloc = [];
var scardloc = [];
var specialcardvector = [];
var tradecards=[0,0,0,0,0];
var menuIsLocked=false;var menuIsFrezzed=false;
function MakeNewTile(pozy,pozx,numar,material)
{
    let newtile = {};
    let tilenumber = {};
    pozx += Math.abs(3 - pozy) * 0.5;
    newtile.html=document.createElement("img");
    tilenumber.html=document.createElement("div");

    tilenumber.html.textContent=numar;
    tilenumber.html.style.left = pozx*204+90 + "px";
    tilenumber.html.style.top = pozy*179+30 + "px";
    tilenumber.html.classList.add("circle");

    newtile.html.style.left = pozx*208 + "px";
    newtile.html.style.top = pozy*179-60+ "px";
    newtile.html.classList.add("tileimage");
    if(material=="dessert")newtile.html.src="images/desert.png";
    if(material=="wool")newtile.html.src="images/wooltile.png";
    if(material=="brick")newtile.html.src="images/bricktile.png";
    if(material=="ore")newtile.html.src="images/oretile.png";
    if(material=="grain")newtile.html.src="images/graintile.png";
    if(material=="wood")newtile.html.src="images/woodtile.png";

    if(material!="dessert")document.body.appendChild(tilenumber.html);

    document.body.appendChild(newtile.html);
    tiles.push(newtile);
    tiles.push(tilenumber);
    return newtile;
}

function MakeTile(pozy,pozx,numar,material)
{
    let newtile = {};
    let tilenumber = {};
    pozx += Math.abs(3 - pozy) * 0.5;
    newtile.html=document.createElement("div");
    tilenumber.html=document.createElement("div");

    tilenumber.html.textContent=numar;
    tilenumber.html.style.left = pozx*204+90 + "px";
    tilenumber.html.style.top = pozy*179+40 + "px";
    tilenumber.html.classList.add("circle");

    newtile.html.style.left = pozx*208 + "px";
    newtile.html.style.top = pozy*179+ "px";
    newtile.html.classList.add("hex");
    var materialcolor;
    if(material=="dessert")materialcolor="rgba(176, 160, 106, 1)";
    if(material=="wool")materialcolor="rgba(193, 238, 88, 1)";
    if(material=="brick")materialcolor="rgba(219, 96, 44, 1)";
    if(material=="ore")materialcolor="rgba(118, 128, 138, 1)";
    if(material=="grain")materialcolor="rgba(239, 227, 64, 1)";
    if(material=="wood")materialcolor="rgba(35, 107, 45, 1)";
    newtile.html.style.backgroundColor= materialcolor;
    newtile.html.style.borderColor= materialcolor;

    if(material!="dessert")document.body.appendChild(tilenumber.html);
    document.body.appendChild(newtile.html);
    tiles.push(newtile);
    tiles.push(tilenumber);
    return newtile;
}

function MakeHarbour(pos,type)
{
    let newharbour = {};
    let harbourtype = {};

    newharbour.html=document.createElement("div");
    harbourtype.html=document.createElement("div");

    newharbour.html.classList.add("trapezoid");

    if(type!="all")
    {
        harbourtype.html.classList.add("circle2");
        if(type=="wool")harbourtype.html.style.backgroundColor="rgba(193, 238, 88, 1)";
        if(type=="brick")harbourtype.html.style.backgroundColor="rgba(219, 96, 44, 1)";
        if(type=="ore")harbourtype.html.style.backgroundColor="rgba(118, 128, 138, 1)";
        if(type=="grain")harbourtype.html.style.backgroundColor="rgba(239, 227, 64, 1)";
        if(type=="wood")harbourtype.html.style.backgroundColor="rgba(35, 107, 45, 1)";
    }

    switch (pos) //im fucking retarded
    {
        case 1:
            if(type!="all")harbourtype.html.style.left =350 + "px";harbourtype.html.style.top = 301 + "px";
            newharbour.html.style.transform = "rotate(-30deg)";
            newharbour.html.style.left = 297 + "px";
            newharbour.html.style.top = 301+ "px";
          break;
        case 2:
            if(type!="all")harbourtype.html.style.left =659 + "px";harbourtype.html.style.top = 122 + "px";
            newharbour.html.style.transform = "rotate(-30deg)";
            newharbour.html.style.left = 607 + "px";
            newharbour.html.style.top = 122+ "px";
          break;
        case 3:
            if(type!="all")harbourtype.html.style.left =183 + "px";harbourtype.html.style.top = 582 + "px";
            newharbour.html.style.transform = "rotate(-90deg)";
            newharbour.html.style.left = 133 + "px";
            newharbour.html.style.top = 582+ "px";
          break;
        case 4:
            if(type!="all")harbourtype.html.style.left =988 + "px";harbourtype.html.style.top = 126 + "px";
            newharbour.html.style.transform = "rotate(30deg)";
            newharbour.html.style.left = 934 + "px";
            newharbour.html.style.top = 122+ "px";
          break;
        case 5:
            if(type!="all")harbourtype.html.style.left = 342 + "px";harbourtype.html.style.top = 864 + "px";
            newharbour.html.style.transform = "rotate(-150deg)";
            newharbour.html.style.left = 296 + "px";
            newharbour.html.style.top = 862+ "px";
          break;
        case 6:
            if(type!="all")harbourtype.html.style.left = 1148 + "px";harbourtype.html.style.top = 414 + "px";
            newharbour.html.style.transform = "rotate(90deg)";
            newharbour.html.style.left = 1098 + "px";
            newharbour.html.style.top = 404+ "px";
          break;
        case 7:
            if(type!="all")harbourtype.html.style.left = 654 + "px";harbourtype.html.style.top = 1046 + "px";
            newharbour.html.style.transform = "rotate(-150deg)";
            newharbour.html.style.left = 608 + "px";
            newharbour.html.style.top = 1042+ "px";
          break;
        case 8:
            if(type!="all")harbourtype.html.style.left = 1148 + "px";harbourtype.html.style.top = 765 + "px";
            newharbour.html.style.transform = "rotate(90deg)";
            newharbour.html.style.left = 1098 + "px";
            newharbour.html.style.top = 760+ "px";
          break;
        case 9:
            if(type!="all")harbourtype.html.style.left = 978 + "px";harbourtype.html.style.top = 1048 + "px";
            newharbour.html.style.transform = "rotate(150deg)";
            newharbour.html.style.left = 934 + "px";
            newharbour.html.style.top = 1043+ "px";
          break;
    }
    if(type=="all")newharbour.html.textContent="3:1 ?";
    if(type!="all")newharbour.html.textContent="2:1";
    document.body.appendChild(newharbour.html);
    document.body.appendChild(harbourtype.html);
}

function MakeSettlement(tile,piece,type,player)
{
    point=tile_to_space(tile,piece)
    pozx=point.x
    pozy=point.y
    let newsettlement = {};

    newsettlement.html= document.createElement("img");
    newsettlement.html.style.shapeOutside = "url(https://i.imgur.com/lEuOmXn.png)";
    if(type!='road')
    {
      newsettlement.html.style.top = pozy+"px";
      newsettlement.html.style.left = pozx+"px";
    }

    if(piece==1 || piece==7)
      newsettlement.html.style.transform="rotate(120deg)"
    if(piece==5 || piece==11)
      newsettlement.html.style.transform="rotate(-120deg)"

    if(type=="town")
      {
        newsettlement.html.src="https://i.imgur.com/lEuOmXn.png";
        document.querySelector('.asezare').appendChild(newsettlement.html)
      }
      else if(type=="city")
      {
        newsettlement.html.src="https://i.imgur.com/FnMNoFx.png";
        document.querySelector('.oras').appendChild(newsettlement.html)
      }
    else
    {
      newsettlement.html.classList.add("rectangle");
      newsettlement.html.style.top=pozy+30+"px";
      newsettlement.html.style.left=pozx+40+"px";
      document.querySelector('.drum').appendChild(newsettlement.html)
    }
    switch(player)
    {
      case 1:
        newsettlement.html.style.filter = "invert(21%) sepia(77%) saturate(5326%) hue-rotate(336deg) brightness(92%) contrast(101%)";
        break;
      case 2:
        newsettlement.html.style.filter="invert(66%) sepia(93%) saturate(402%) hue-rotate(1deg) brightness(92%) contrast(99%)";
        break;
      case 3:
        newsettlement.html.style.filter = "invert(20%) sepia(73%) saturate(5005%) hue-rotate(238deg) brightness(84%) contrast(102%)";
        break;
      case 4:
        newsettlement.html.style.filter = "invert(100%) sepia(0%) saturate(7491%) hue-rotate(339deg) brightness(105%) contrast(103%)";
    }


}
function updateSettlement(pozx,pozy)
{
  let father=document.getElementsByClassName('asezare')[0]
  elements=father.children;
  for(let i=0;i<elements.length;i++)
  {
    if(elements[i].style.top==pozy+"px" && elements[i].style.left==pozx+"px")
    {
      let newsettlement= document.createElement("img");
      newsettlement.style.filter=elements[i].style.filter
      elements[i].remove()
      newsettlement.style.top = pozy+"px";
      newsettlement.style.left = pozx+"px";
      newsettlement.src="https://i.imgur.com/FnMNoFx.png";
      document.querySelector('.oras').appendChild(newsettlement)
      return
    }
  }

}
function MakeAndMoveThief(tile)
{
    if(document.getElementById("theif")!=null)
      document.getElementById("theif").remove();
    let newthief = {};
    newthief.html= document.createElement("img");
    newthief.html.src="https://i.imgur.com/x0MnP5O.png";
    newthief.html.classList.add("thief");
    newthief.id="thief";
    newthief.html.style.left =(tile_poz[tile].x-80)+"px";
    newthief.html.style.top = (tile_poz[tile].y-40)+"px";

    document.body.appendChild(newthief.html);
}

async function MakeMap(x)
{
    for(var i=1;i<=9;i++)
    {
        if(i%2==0)MakeHarbour(i,"all");
        if(i==1)MakeHarbour(i,"wool");
        if(i==3)MakeHarbour(i,"brick");
        if(i==5)MakeHarbour(i,"ore");
        if(i==7)MakeHarbour(i,"grain");
        if(i==9)MakeHarbour(i,"wood");
    }

    for(var i=0;i<x.length;i++)
    {
      var a,b;
      if(i<3)
      {
        a=1;
        b=i+1;
      }
      if(i>=3 && i<7)
      {
        a=2;
        b=i-2;
      }
      if(i>=7 && i<12)
      {
        a=3;
        b=i-6;
      }
      if(i>=12 && i<16)
      {
        a=4;
        b=i-11;
      }
      if(i>=16 && i<19)
      { 
        a=5;
        b=i-15;
      }
      if(x[i][1]==-1)MakeNewTile(a,b,x[i][0],"dessert")
      if(x[i][1]==0)MakeNewTile(a,b,x[i][0],"wood");
      if(x[i][1]==1)MakeNewTile(a,b,x[i][0],"brick");
      if(x[i][1]==2)MakeNewTile(a,b,x[i][0],"grain");
      if(x[i][1]==3)MakeNewTile(a,b,x[i][0],"wool");
      if(x[i][1]==4)MakeNewTile(a,b,x[i][0],"ore");
    }

    // MakeNewTile(1,1,2,"wool");
    // MakeNewTile(1,2,3,"brick");
    // MakeNewTile(1,3,4,"ore");
    // MakeNewTile(2,1,5,"grain");
    // MakeNewTile(2,2,6,"wood");
    // MakeNewTile(2,3,2,"brick");
    // MakeNewTile(2,4,8,"brick");
    // MakeNewTile(3,1,9,"grain");
    // MakeNewTile(3,2,10,"wood");
    // MakeNewTile(3,3,"","dessert");
    // MakeNewTile(3,4,12,"ore");
    // MakeNewTile(3,5,3,"ore");
    // MakeNewTile(4,1,4,"grain");
    // MakeNewTile(4,2,5,"wood");
    // MakeNewTile(4,3,6,"wool");
    // MakeNewTile(4,4,7,"brick");
    // MakeNewTile(5,1,8,"ore");
    // MakeNewTile(5,2,9,"grain");
    // MakeNewTile(5,3,12,"wood");

    MakeAndMoveThief(await get('pozThief',0));
}

function stringtoint(x)
{
  let modified=[]
  for(var i=0;i<x.length;i++)
  {
    if(x[i]=="wood")modified.push(0)
    if(x[i]=="brick")modified.push(1)
    if(x[i]=="grain")modified.push(2)
    if(x[i]=="wool")modified.push(3)
    if(x[i]=="ore")modified.push(4)
  }
  return modified;
}

//--UI----UI----UI----UI----UI----UI----UI----UI----UI----UI----UI----UI----UI----UI----UI----UI----UI----UI----UI--UI--

function PopUpShow() {
  var popup = document.getElementById("myPopup");
  popup.classList.toggle("show");
}

function RemoveCards(index)
{
  cardloc.splice(index,1);
  cardvector.splice(index,1);
}

function RemoveSpecialCards(index)
{
  scardloc.splice(index,1);
  specialcardvector.splice(index,1);
}

function NewCards(cardvector)
{
  for(var i=1;i<=cardvector.length;i++)
  {
      if(document.getElementById("card"+i)==null)
      {
        let newcard = {};
        newcard.mat=cardvector[i-1];
        newcard.html=document.createElement("div");
        newcard.html.classList.add("card");
        newcard.html.style.left=(i-1)*120+10+"px";
        newcard.html.id="card"+i;
        dragElement(newcard.html);
        cardloc.push(newcard);
        document.getElementById("cardpadding1").appendChild(newcard.html);
        if(cardvector[i-1]=="wood") newcard.html.style.backgroundImage="url(https://i.imgur.com/amAWx6q.png)";
        if(cardvector[i-1]=="brick") newcard.html.style.backgroundImage="url(https://i.imgur.com/jldnqDd.png)";
        if(cardvector[i-1]=="wool") newcard.html.style.backgroundImage="url(https://i.imgur.com/CEl8Sij.png)";
        if(cardvector[i-1]=="grain") newcard.html.style.backgroundImage="url(https://i.imgur.com/KILdl8B.png)";
        if(cardvector[i-1]=="ore") newcard.html.style.backgroundImage="url(https://i.imgur.com/l9yIY2E.png)";
      }
  }
}
function NewSpecialCards(specialcardvector)
{
  for(var i=1;i<=specialcardvector.length;i++)
  {
    if(document.getElementById("scard"+i)==null)
    {
      let newspecialcard= {};
      newspecialcard.mat=specialcardvector[i-1];
      newspecialcard.html=document.createElement("div");
      newspecialcard.html.classList.add("card");
      newspecialcard.html.style.top=176+"px";
      newspecialcard.html.style.left=(i-1)*120+10+"px";
      newspecialcard.html.id="scard"+i;
      dragElement(newspecialcard.html); 
      scardloc.push(newspecialcard);
      document.getElementById("cardpadding2").appendChild(newspecialcard.html);
      if(specialcardvector[i-1]=="LIB") newspecialcard.html.style.backgroundImage="url(https://i.imgur.com/cIVhMQv.png)";
      if(specialcardvector[i-1]=="KNG") newspecialcard.html.style.backgroundImage="url(https://i.imgur.com/ikUPxHo.png)";
      if(specialcardvector[i-1]=="RBD") newspecialcard.html.style.backgroundImage="url(https://i.imgur.com/O23yKZR.png)";
      if(specialcardvector[i-1]=="MNP") newspecialcard.html.style.backgroundImage="url(https://i.imgur.com/mbxoOLf.png)";
      if(specialcardvector[i-1]=="YOP") newspecialcard.html.style.backgroundImage="url(https://i.imgur.com/H9KBWNy.png)";
    }
  }
}

function openNav() {
  if(menuIsLocked==false)
  {
    NewSpecialCards(specialcardvector);
    NewCards(cardvector);
    document.getElementById("myNav").style.width = "100%";
  }
}

function closeNav() {
  if(menuIsFrezzed==false)
  {
    document.getElementById("myNav").style.width = "0%";
  }
}

function openNav1() {
  if(menuIsLocked==false)
  {
    NewSpecialCards(specialcardvector);
    NewCards(cardvector);
    document.getElementById("myNav1").style.width = "100%";
  }
}

function closeNav1() {
  if(menuIsFrezzed==false)
  {
    document.getElementById("myNav1").style.width = "0%";
  }
}



function updatenumbermat()
{
  var wood=0,wool=0,ore=0,brick=0,grain=0;
  var LIB=0,KNG=0,RBD=0,YOP=0,MNP=0;
  if(document.getElementById("myNav").style.width=="100%")
  {
    for(var i=0;i<cardloc.length;i++)
    {
      if(parseInt(cardloc[i].html.style.top)>445 && parseInt(cardloc[i].html.style.top)<875 && parseInt(cardloc[i].html.style.left)>700 && parseInt(cardloc[i].html.style.left)<1190)
      {
        if(cardloc[i].mat=="wood")wood++;
        if(cardloc[i].mat=="wool")wool++;
        if(cardloc[i].mat=="ore")ore++;
        if(cardloc[i].mat=="brick")brick++;
        if(cardloc[i].mat=="grain")grain++;
      }
    }
    document.getElementById("cwood").textContent=wood;
    document.getElementById("cwool").textContent=wool;
    document.getElementById("core").textContent=ore;
    document.getElementById("cbrick").textContent=brick;
    document.getElementById("cgrain").textContent=grain;
    for(var i=0;i<scardloc.length;i++)
    {
      if(parseInt(scardloc[i].html.style.top)>445 && parseInt(scardloc[i].html.style.top)<875 && parseInt(scardloc[i].html.style.left)>700 && parseInt(scardloc[i].html.style.left)<1190)
      {
        if(scardloc[i].mat=="LIB")LIB++;
        if(scardloc[i].mat=="YOP")YOP++;
        if(scardloc[i].mat=="RBD")RBD++;
        if(scardloc[i].mat=="KNG")KNG++;
        if(scardloc[i].mat=="MNP")MNP++;
      }
    }
    document.getElementById("LIB").textContent=LIB;
    document.getElementById("YOP").textContent=YOP;
    document.getElementById("RBD").textContent=RBD;
    document.getElementById("KNG").textContent=KNG;
    document.getElementById("MNP").textContent=MNP;
  }
}

function getTradecardsYouwant()
{
  tradecards[0]=parseInt(document.getElementById("twood").textContent);
  tradecards[1]=parseInt(document.getElementById("tbrick").textContent);
  tradecards[2]=parseInt(document.getElementById("tgrain").textContent);
  tradecards[3]=parseInt(document.getElementById("twool").textContent);
  tradecards[4]=parseInt(document.getElementById("tore").textContent);
}

var intervalId = window.setInterval(function()
{
  getTradecardsYouwant()
  updatenumbermat();
}, 1);

function dragElement(elmnt) {
  var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
  if (document.getElementById(elmnt.id)) {
    document.getElementById(elmnt.id).onmousedown = dragMouseDown;
  } else {
    elmnt.onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;
    elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
    elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
  }

  function closeDragElement() {
    document.onmouseup = null;
    document.onmousemove = null;
  }
}
const firstDice=document.querySelector("#dice1")
const secondDice=document.querySelector("#dice2")
const diceAnimation=document.querySelector("#dices")
var rollDice=document.querySelector("#diceButton")
function resetDice()
{
  firstDice.textContent="#"
  secondDice.textContent="#"
  diceAnimation.style.opacity="100%"
  rollDice.style.opacity="100%"
}

function showDice(x,y)
{
  firstDice.textContent=x
  secondDice.textContent=y
  diceAnimation.style.opacity="0%"
  rollDice.style.opacity="0%"
  removeEventListeners(rollDice);
  rollDice=document.querySelector("#diceButton")
}

function showData(x,y)
{
  for(var i=1;i<=cardvector.length;i++)
  {
      if(document.getElementById("card"+i)!=null)
      {
        document.getElementById("card"+i).remove()
      }
  }
  cardloc.splice(0)
  scardloc.splice(0)
  for(var i=1;i<=specialcardvector.length;i++)
  {
      if(document.getElementById("scard"+i)!=null)
      {
        document.getElementById("scard"+i).remove()
      }
  }
    var j=0;
    for(var i=0;i<x.length;i++)
    {
      while(x[i]!=0)
      {
        if(i==0)cardvector[j]="wood";
        if(i==1)cardvector[j]="brick";
        if(i==2)cardvector[j]="grain";
        if(i==3)cardvector[j]="wool";
        if(i==4)cardvector[j]="ore";
        j+=1;
        x[i]-=1;
      }
    }
    cardvector.splice(j)
    j=0;
    for(var i=0;i<y.length;i++)
    {
      while(y[i]!=0)
      {
        if(i==0)specialcardvector[j]="LIB";
        if(i==1)specialcardvector[j]="KNG";
        if(i==2)specialcardvector[j]="YOP";
        if(i==3)specialcardvector[j]="RBD";
        if(i==4)specialcardvector[j]="MNP";
        j+=1;
        y[i]-=1;
      }
    }
    specialcardvector.splice(j)
    NewCards(cardvector)
    NewSpecialCards(specialcardvector)
}