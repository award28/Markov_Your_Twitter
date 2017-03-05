var Twitter = require('twitter');
var config = require('./config/config.json'); 

var client = new Twitter({
    consumer_key: config.consumer_key,
    consumer_secret: config.consumer_secret,
    access_token_key: config.access_token_key,
    access_token_secret: config.access_token_secret
});
 
var params = {screen_name: 'award2828'};
client.get('statuses/user_timeline', params, function(error, tweets, response) {
    if (!error) {
        console.log(tweets.length);
        for(var i = 0; i < tweets.length; i++) {
            if(!tweets[i].retweeted_status)
                console.log(tweets[i].text)
        }
    }
    else
        console.log(error);
});
