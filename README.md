# Indian ISP Blocked Domain Checker
Check blocked domains on Indian ISPs

This is a simple Python script for checking if a website is blocked by Indian ISPs. 
From what I gathered, when a website is blocked on Indian ISPs over http, an iframe is inserted into the blocked page

![jfjsd](https://user-images.githubusercontent.com/67092879/134776713-5e48dd3c-94b2-45ac-b4f3-77cbf17f87db.PNG)

My script matches the regex to in the format "\<iframe src\=\"http\:\/\/.*:8080\/webadmin\/deny\/index\.php" to the one found on the blocked page to check if site is blocked

The script is set to check top 1 million sites by Alexa from the url http://downloads.majestic.com/majestic_million.csv Make sure that this file is in same folder as the python script

However, you can remove the CSV part all together and have it just read from a text file if you want. 

Output file snippet:

![jfjsd](https://user-images.githubusercontent.com/67092879/134776868-bd23889d-5776-4eb7-8ff2-4ecf4707085d.PNG)

Console output:

![jfjsd](https://user-images.githubusercontent.com/67092879/134776895-cc20d926-f50c-4b2b-b69c-bceb57a8ff0e.PNG)

Feel free to change code however you like
