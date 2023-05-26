

var nrJucatori=4;
async function OnStartGame()
{
    lockMenu()
    for(var i=0;i<nrJucatori;i++)
    {
        if(i==0)
        {
            await showAvialable(await get("posibile_asezari",i),0,false);
            await showAvialable(await get("posibile_drumuri",i),0,false);
            await put("place_piece",0,chosedPosition);
        }
        else
        {
            MakeSettlement(await get("Ai_start_asezare",i),"town",i);
        }
    }
    for(var i=nrJucatori-1;i>=1;i++)
    {
        if(i==0)
        {
            await showAvialable(await get("posibile_asezari",i),0,false);
            await showAvialable(await get("posibile_drumuri",i),0,false);
            await put("place_piece",0,chosedPosition); 
            unlockMenu()
        }
        else
        {
            let AIChosed=await get("Ai_start_asezare",i);
            MakeSettlement(AIChosed,"town",i);
        }

    }
}

async function TheGame()
{
    while(!await get("gameWon",0))
    {
        for(let i=0;i<=nrJucatori;i++)
        {
            if(i==0)
            {
                await playerGame(i)
            }
            else
            {
                let action=["",""]
                while(action[0]!="pas")
                {
                    action=await get("AIaction",i)
                    manageAction(action)
                }
            }
        }
    }
}
async function test()
{
    
    await MakeMap(await post(0,4))
    await put('putData',0,[[5,5,5,5,5],[1,1,1,1,1]])
    await put('putData',1,[[1,1,1,1,1],[1,1,1,1,1]])
    await put('placePiece',0,['asezare',8,6])
    MakeSettlement(8,6,'town',0)
    await put('placePiece',0,['drum',8,7])
    MakeSettlement(8,7,'drum',0)
    await put('placePiece',1,['asezare',5,6])
    MakeSettlement(5,6,'town',1)
    await put('placePiece',1,['drum',5,7])
    MakeSettlement(5,7,'drum',1)
    await put('placePiece',2,['asezare',2,6])
    MakeSettlement(2,6,'town',2)
    await put('placePiece',2,['drum',2,7])
    MakeSettlement(2,7,'drum',2)
    await put('placePiece',3,['asezare',12,6])
    MakeSettlement(12,6,'town',3)
    await put('placePiece',3,['drum',12,7])
    MakeSettlement(12,7,'drum',3)
    await put('placePiece',0,['asezare',8,6])
    MakeSettlement(8,6,'town',0)
    await put('placePiece',0,['drum',8,7])
    MakeSettlement(8,7,'drum',0)
    await put('placePiece',1,['asezare',5,6])
    MakeSettlement(5,6,'town',1)
    await put('placePiece',1,['drum',5,7])
    MakeSettlement(5,7,'drum',1)
    await put('placePiece',2,['asezare',2,6])
    MakeSettlement(2,6,'town',2)
    await put('placePiece',2,['drum',2,7])
    MakeSettlement(2,7,'drum',2)
    await put('placePiece',3,['asezare',12,6])
    MakeSettlement(12,6,'town',3)
    await put('placePiece',3,['drum',12,7])
    MakeSettlement(12,7,'drum',3)
    
    await TheGame()
}

test()
