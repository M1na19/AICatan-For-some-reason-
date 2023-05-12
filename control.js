const axios = require('axios');
function get(request,player_turn)
{
    axios.get('http://localhost:5000',{
    params:{
      'action': request, 
      'player': player_turn
    }
    .then(response => {
        return response.data;
      })
      .catch(error => {
        console.error(error);
      })
    })
}
function put(request,player_turn,information)
{
    axios.put('http://localhost:5000',{
    params:{
      'action': request, 
      'player': player_turn,
      'info':information
    }
    .catch(error => {
        console.error(error);
      })
    })
}
function post(staringPlayer,nrPlayers)
{
    axios.put('http://localhost:5000',{
    params:{
      'sp': staringPlayer,
      'nrP': nrPlayers
    }
    .then(response => {
        return response.data;//asta e sub forma de config de tileuri
        //config de tileuri e basicly o matrice de 19 pe 2, adica 19 tileuri care au 2 valori
        //cele 2 valori sunt resursa si valoare
      })
    .catch(error => {
        console.error(error);
      })
    })
}