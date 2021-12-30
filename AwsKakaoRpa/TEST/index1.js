var https = require('https');

exports.handler = function(event) {
	https.postMessage("https://154.10.6.1");
	//token = getToken("default", "admin", "1234qwer!");
}

var https = require('https');

exports.handler = function(event, context) {
  https.post('https//hansol/api/account/authenticate',  function(userString) {
    statusCode: 200,
    console.log('Success');
  }).on('error', function(error) {
    console.log('Failed');
  });
};

return {
            login : function (user_id, password, callback) {
                OPTIONS.url = 'https://hansol/api/account/authenticate';
                OPTIONS.body = JSON.stringify({
                    "user_id": user_id,
                    "password": password
                });
                .post(OPTIONS, function (err, res, result) {
                    statusCodeErrorHandler(res.statusCode, callback, result);
                });
            }
        };
        
        
        exports.handler = async (event) => {
    // TODO implement
    const response = {
        statusCode: 200,
        body: JSON.stringify('Hello Lambda'),
    };
    return response;
};

var request = require('request');
var https = require('https');

exports.handler = function(event, context) {
     https.post('https//hansol/api/account/authenticate',
     headers: {'Content-Type': 'application/json'}
     username: JSON.stringify('jjjiny'),
     password: JSON.stringify('hb1060at^^');
     );}
     
     
     exports.handler = function(event, context) {
    console.log("** Sarc event :", JSON.stringify(event));
    var name = event.myname + ' from Sarc'; 
    context.succeed('** Hello Lambda from ' + name);
};