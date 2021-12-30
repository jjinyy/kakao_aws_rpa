exports.handler = async (event) => {
    orchestrator.Authenticate()
}


var orchestrator = {}
var axios = require('axios')

var instance = axios.create({
  baseURL: 'https://154.10.6.152',
  timeout: 1000,
  headers: {'Authorization': 'Bearer '+orchestrator.bearerToken}
});

orchestrator.bearerToken = ''


orchestrator.Authenticate = async () => {
  return new Promise((resolve,reject) => {
        return instance({
          method: 'post',
          url: '/api/Account/Authenticate',
          data: {
            "tenancyName": "default",
            "usernameOrEmailAddress": "jjjiny",
            "password": "hb1060at^^"
          }
        }).then(result => {
          orchestrator.bearerToken = result.data.result
          resolve(true)
        })
      })    
  }

