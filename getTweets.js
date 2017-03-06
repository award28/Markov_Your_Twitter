var Twitter = require('twitter');
var config = require('./config/config.json'); 

var client = new Twitter({
    consumer_key: config.consumer_key,
    consumer_secret: config.consumer_secret,
    access_token_key: config.access_token_key,
    access_token_secret: config.access_token_secret
});
 
var params = {
    screen_name: 'award2828',
    count: 3200
};

var tweetStr = "";
client.get('statuses/user_timeline', params, function(error, tweets, response) {
    if (!error) {
        for(var i = 0; i < tweets.length; i++) {
            if(!tweets[i].retweeted_status)
                tweetStr += tweets[i].text + "\n";
        }
        var spawn = require("child_process").spawn;
        var process = spawn('python3',["./markov.py", tweetStr]);

        process.stdout.on('data', function (data){
            /*client.post('statuses/update', {status: data.toString()},  function(error, tweet, response) {
                  if(error) throw error;
                    console.log(tweet);  // Tweet body. 
            });*/
            console.log(data.toString());
            // Do something with the data returned from python script
        });
    }
    else
        console.log(error);
});
