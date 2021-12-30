module.exports = function (callee) {
    function API_Call(callee) {
        var OPTIONS = {
            headers: {'Content-Type': 'application/json'},
            url: null,
            body: null
        };
        var HOST = null;
        return {
            login : function (callback) {
                OPTIONS.url = 'https://hansol/api/account/authenticate';
                OPTIONS.body = JSON.stringify({
                    "user_id": "jjjiny",
                    "password": "hb1060at^^"
                });
            }
        };
    }
    var INSTANCE;
    if (INSTANCE === undefined) {
        INSTANCE = new API_Call(callee);
    }
    return INSTANCE;
};