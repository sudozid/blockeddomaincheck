# Indian ISP Blocked Domain Checker
Check blocked domains on Indian ISPs

This is a simple Python script for checking if a website is blocked by Indian ISPs. 
From what I gathered, when a website is blocked on Indian ISPs over http, an iframe is inserted into the blocked page

TATA Transit ISPs:

![jfjsd](https://user-images.githubusercontent.com/67092879/134776713-5e48dd3c-94b2-45ac-b4f3-77cbf17f87db.PNG)

Airtel Transit ISP:

![jfjsd](https://user-images.githubusercontent.com/67092879/134777499-3fc9ae93-d37d-4c89-857f-1bc6c3a631cc.PNG)

Airtel LTE:

![jfjsd](https://user-images.githubusercontent.com/67092879/134777995-69f7aefa-5c13-427e-b99e-887714081da4.PNG)

Jio LTE:

![JIO](https://user-images.githubusercontent.com/67092879/134778036-ebc62f97-cbf7-4db1-a4cd-03b0b4bdcbd6.PNG)


My script matches the regex to in the format "\<iframe src\=\"http\:\/\/.*:8080\/webadmin\/deny\/index\.php" to the one found on the blocked page to check if site is blocked

The script is set to check top 1 million sites by Alexa from the url http://downloads.majestic.com/majestic_million.csv Make sure that this file is in same folder as the python script

However, you can remove the CSV part all together and have it just read from a text file if you want.

**NOTE: Keep in mind that there is no exception handling on this yet, so there is a chance that if network is unreliable, the script may fail to request and check certain sites.**

Output file snippet:

![jfjsd](https://user-images.githubusercontent.com/67092879/134776868-bd23889d-5776-4eb7-8ff2-4ecf4707085d.PNG)

Console output:

![jfjsd](https://user-images.githubusercontent.com/67092879/134776895-cc20d926-f50c-4b2b-b69c-bceb57a8ff0e.PNG)

Feel free to change code however you like
