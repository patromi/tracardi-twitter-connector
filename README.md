# Twitter Connector

The purpose of this plugin is sending tweets via twitter app

# Configuration

This node requires configuration. You need have a dev account in twitter https://apps.twitter.com/.
Next create your own app. If you don't know how: https://smashballoon.com/doc/create-your-own-twitter-app/

**Important**
You need to add at least `Read and write permissions`.

## Message configuration
* id - Enter your resource id

Open your app in dev panel and click the Keys and tokens:

![Keys](https://cdn.discordapp.com/attachments/840335225287475260/898977586351312896/Untitled.png)

* consumer_key: None, You can find in Consumer Keys API Key and Secret 
* consumer_secret: None, - You can find it in Consumer Keys API Key and Secret 
* access_token: None - You can find it in Authentication Tokens Access Token and Secret
* access_token_secret: None - You can find it in Authentication Tokens Access Token and Secret
* message: None - Type the text you want to tweet
## Example of action configuration

```json
{
    "source": {
                "id": "55584df6-9ee3-4acd-a0ea-e555122f3dbc"
                },
    "config": {
        "consumer_key": "",
        "consumer_secret": "",
        "access_token": "",
        "access_token_secret": ""
},
    "message": {"message": "Welcome!"}

}
```



# Input payload

This node does not process input payload.

# Output

This node only return True if tweet send successfully
