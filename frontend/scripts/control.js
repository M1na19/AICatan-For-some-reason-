
async function get(request,player_turn,info)
{
  let data;
    await axios.get('http://localhost:8080',{
    params:{
      'action': request, 
      'player': player_turn,
      'info':info
    }
  })
    .then(response => {
        data=response.data;
      })
    .catch(error => {
        console.error(error);
      })
    return data;
}
async function put(request,player_turn,information)
{
    await axios.put('http://localhost:8080',{
    params:{
      'action': request, 
      'player': player_turn,
      'info':information
    }
  })
    .catch(error => {
        console.error(error);
      })
}
async function post(staringPlayer,nrPlayers)
{
  let data;
    await axios.post('http://localhost:8080',{
    params:{
      'startplayer': staringPlayer,
      'numberofplayers': nrPlayers
    }
  })
    .then(response => {
        data=response.data;
        
        //asta e sub forma de config de tileuri
        //config de tileuri e basicly o matrice de 19 pe 2, adica 19 tileuri care au 2 valori
        //cele 2 valori sunt resursa si valoare
      })
    .catch(error => {
        console.error(error);
      })
    return data
}
// async function test()
// {
//   await post(0,4)
//   await put('placePiece',0,['asezare',8,6])
// }
// test()
