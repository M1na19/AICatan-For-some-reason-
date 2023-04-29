var tiles = [];

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

class settlement {
  type

  constructor()
};

function MakeSettlement(pozx,pozy,type,player)
{
    let newsettlement = {};

    newsettlement.html= document.createElement("img");

    pozx=pozx*2-1+Math.abs(3-Math.floor(pozy/2));
    pozy=pozy+Math.floor((pozy-1)/2);

    newsettlement.html.style.top = pozy*60 + "px";
    newsettlement.html.style.left = pozx*104+60 + "px";

    if(type=="town")
      newsettlement.html.src="https://i.imgur.com/lEuOmXn.png";
    else
      newsettlement.html.src="https://i.imgur.com/FnMNoFx.png";
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

MakeSettlement(1,1,"town",1)
MakeSettlement(1,2,"town",2)
MakeSettlement(1,3,"city",3)
MakeSettlement(2,11,"city",4)
MakeSettlement(5,5,"town",2)
MakeSettlement(4,8,"town",3)
MakeSettlement(3,3,"city",4)
MakeSettlement(4,11,"city",1)

function MakeMap()
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
}

/// To do buildings/ Cards/ Playable Area

MakeMap();
