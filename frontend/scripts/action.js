let tried_trade=false
async function manageAction(action,player)
{
    let name=action[0]
    let info=action[1]
    if(name=='pass')
    {
        tried_trade=false
        return
    }
    else if(name=='steal')
    {
        let tile=info[0]
        let player2=info[1]
        MakeAndMoveThief(tile)
        await put('soldat',player)
        await put('steal',player,[player2])
    }
    else if(name=="drum")
    {
        let tileinfo=info
        MakeSettlement(tileinfo[0],tileinfo[1],'road',player)
        await put('placePiece',player,['drum',tileinfo[0],tileinfo[1]])
    }
    else if(name=="asezare")
    {
        let tileinfo=info
        MakeSettlement(tileinfo[0],tileinfo[1],'town',player)
        await put('placePiece',player,['oras',tileinfo[0],tileinfo[1]])
    }
    else if(name=="oras")
    {
        let tileinfo=info
        MakeSettlement(tileinfo[0],tileinfo[1],'city',player)
        await put('placePiece',player,['oras',tileinfo[0],tileinfo[1]])
    }
    else if(name=="dezvoltare")
    {
        await get('getDezv',player)
    }
    else if(name=="2resurse")
    {
        let res1=info[0]
        let res2=info[1]
        let res=[0,0,0,0,0]
        res[res1]=1
        res[res2]=1
        await put('gain2Resources',player,res)
    }
    else if(name=="2drum")
    {
        let tileinfo1=info[0]
        let tileinfo2=info[1]
        MakeSettlement(tileinfo1[0],tileinfo1[1],'road',player)
        await put('2drumuri',player)
        await put('placePiece',player,['drum',tileinfo1[0],tileinfo1[1]])
        MakeSettlement(tileinfo2[0],tileinfo2[1],'road',player)
        await put('placePiece',player,['drum',tileinfo2[0],tileinfo2[1]])
    }
    else if(name=="monopol")
    {
        let resource=info
        await put('monopol',player,resource)
    }
    else if(name=="Trade" && tried_trade==false)
    {
        tried_trade=true
        let player2=info[0]
        let recieve=info[1]
        let give=info[2]
        if(player2==0)
        {
            let cardsgiven=[0,0,0,0,0]
            let cardsrecived=[0,0,0,0,0]
            cardsgiven[give]=1
            cardsrecived[recieve]=1
            tradeProposal(cardsrecived,cardsgiven,0,player)
        }
        else
        {
            await put('playersTrade',player,[player2,[give],[recieve]])
        }
    }
    else if(tried_trade==true)
    {
        action[0]="pass"
        return
    }
}