  var tiles = [];
var cardvector = ["brick","wool","wood","ore","grain","brick","wool","wood","ore","grain","brick","wool","wood","ore","grain"];
var cardloc = [];
var specialcardvector = ["vp","soldier","2newroads","monopoly","yop","vp","soldier","2newroads","monopoly","yop","vp","soldier","2newroads","monopoly","yop"];

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
      newsettlement.html.src="https://i.imgur.com/lEuOmXn.png";
    else if(type=="city")
      newsettlement.html.src="https://i.imgur.com/FnMNoFx.png";
    else
      {
        newsettlement.html.classList.add("rectangle");
        newsettlement.html.style.top=pozy+30+"px"
        newsettlement.html.style.left=pozx+40+"px"
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

    document.body.appendChild(newsettlement.html);
}

function MakeAndMoveThief(pozx,pozy)
{
    //document.body.getElementById("theif").remove();
    let newthief = {};
    newthief.html= document.createElement("img");
    newthief.html.src="https://i.imgur.com/x0MnP5O.png";
    newthief.html.classList.add("thief");
    newthief.id="thief";
    pozx += Math.abs(3 - pozy) * 0.5;
    newthief.html.style.left = pozx*204-10+"px";
    newthief.html.style.top = pozy*179-40 + "px";

    document.body.appendChild(newthief.html);
}

function MakeMap()
{
    var temp = [6, 4, 8, 5, 10, 6, 10, 5, 8, 4, 6];
    for (let j = 0; j < 19; j++)
      for (let i = 1; i <= 11; i+=2)
        MakeSettlement(j,i, "road", Math.floor(1 + Math.random() * 4))
    MakeSettlement(0,0,"town",Math.floor(1 + Math.random() * 4));
    MakeSettlement(1,0,"town",Math.floor(1 + Math.random() * 4));
    MakeSettlement(5,0,"city",Math.floor(1 + Math.random() * 4));
    MakeSettlement(16,4,"city",Math.floor(1 + Math.random() * 4));
    MakeSettlement(11,0,"town",Math.floor(1 + Math.random() * 4));
    MakeSettlement(14,2,"town",Math.floor(1 + Math.random() * 4));
    MakeSettlement(1,4,"city",Math.floor(1 + Math.random() * 4));
    MakeSettlement(18,4,"city",Math.floor(1 + Math.random() * 4));
    for(var i=1;i<=9;i++)
    {
        if(i%2==0)MakeHarbour(i,"all");
        if(i==1)MakeHarbour(i,"wool");
        if(i==3)MakeHarbour(i,"brick");
        if(i==5)MakeHarbour(i,"ore");
        if(i==7)MakeHarbour(i,"grain");
        if(i==9)MakeHarbour(i,"wood");
    }
    MakeTile(1,1,2,"wool");
    MakeTile(1,2,3,"brick");
    MakeTile(1,3,4,"ore");
    MakeTile(2,1,5,"grain");
    MakeTile(2,2,6,"wood");
    MakeTile(2,3,2,"brick");
    MakeTile(2,4,8,"brick");
    MakeTile(3,1,9,"grain");
    MakeTile(3,2,10,"wood");
    MakeTile(3,3,"","dessert");
    MakeTile(3,4,12,"ore");
    MakeTile(3,5,3,"ore");
    MakeTile(4,1,4,"grain");
    MakeTile(4,2,5,"wood");
    MakeTile(4,3,6,"wool");
    MakeTile(4,4,7,"brick");
    MakeTile(5,1,8,"ore");
    MakeTile(5,2,9,"grain");
    MakeTile(5,3,12,"wood");

    MakeAndMoveThief(3,3);
}

//--UI----UI----UI----UI----UI----UI----UI----UI----UI----UI----UI----UI----UI----UI----UI----UI----UI----UI----UI--UI--

function UpdateDice(val1,val2)
{
    document.getElementById("dice1").textContent=val1;
    document.getElementById("dice2").textContent=val2;
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
function UpdateSpecialCards(specialcardvector)
{
  for(var i=1;i<=specialcardvector.length;i++)
  {
    if(document.getElementById("scard"+i)==null)
    {
      let newspecialcard= {};
      newspecialcard.html=document.createElement("div");
      newspecialcard.html.classList.add("card");
      newspecialcard.html.style.top=176+"px";
      newspecialcard.html.style.left=(i-1)*120+10+"px";
      newspecialcard.html.id="scard"+i;
      dragElement(newspecialcard.html); 
      document.getElementById("cardpadding2").appendChild(newspecialcard.html);
      if(specialcardvector[i-1]=="vp") newspecialcard.html.style.backgroundImage="url(https://i.imgur.com/cIVhMQv.png)";
      if(specialcardvector[i-1]=="soldier") newspecialcard.html.style.backgroundImage="url(https://i.imgur.com/ikUPxHo.png)";
      if(specialcardvector[i-1]=="2newroads") newspecialcard.html.style.backgroundImage="url(https://i.imgur.com/O23yKZR.png)";
      if(specialcardvector[i-1]=="monopoly") newspecialcard.html.style.backgroundImage="url(https://i.imgur.com/mbxoOLf.png)";
      if(specialcardvector[i-1]=="yop") newspecialcard.html.style.backgroundImage="url(https://i.imgur.com/H9KBWNy.png)";
    }
  }
}

function openNav() {
  UpdateDice(4,6);
  UpdateSpecialCards(specialcardvector);
  NewCards(cardvector);
  document.getElementById("myNav").style.width = "100%";
}

function closeNav() {
  document.getElementById("myNav").style.width = "0%";
}

MakeMap();

function updatenumbermat()
{
  var wood=0,wool=0,ore=0,brick=0,grain=0;
  if(document.getElementById("myNav").style.width=="100%")
  {
    for(var i=0;i<cardloc.length;i++)
    {
      if(parseInt(cardloc[i].html.style.top)>500 && parseInt(cardloc[i].html.style.top)<924 && parseInt(cardloc[i].html.style.left)>800 && parseInt(cardloc[i].html.style.left)<1300)
      {
        if(cardloc[i].mat=="wood")wood++;
        if(cardloc[i].mat=="wool")wool++;
        if(cardloc[i].mat=="ore")ore++;
        if(cardloc[i].mat=="brick")brick++;
        if(cardloc[i].mat=="grain")grain++;
        //=parseInt(document.getElementById("c"+cardloc[i].mat).textContent)+1;
      }
      document.getElementById("cwood").textContent=wood;
      document.getElementById("cwool").textContent=wool;
      document.getElementById("core").textContent=ore;
      document.getElementById("cbrick").textContent=brick;
      document.getElementById("cgrain").textContent=grain;
    }
  }
}

var intervalId = window.setInterval(function()
{
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