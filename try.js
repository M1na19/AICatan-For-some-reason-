const axios = require('axios');

axios.post('http://localhost:5000',{
    startplayer: 0,
    numberofplayers:4
})
.then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });








  axios.get('http://localhost:5000',{
    params:{
      'action': 'zar', 
      'player':'none',
      'info':'none'
    }
})
.then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });