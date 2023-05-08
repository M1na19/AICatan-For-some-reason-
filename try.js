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
    params:{'action': 'zar'}
})
.then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });
  axios.put('http://localhost:5000',{
    data:{'toput':'life'},
    params:{'action': 'zar'}
})
.then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });