# background-changer
this script is ran from the command line and takes -t as an argument when calling the program 

![cmd_usage](https://user-images.githubusercontent.com/68308394/155227574-23e47350-c1b5-4e2a-83a6-c2c687ce3f03.PNG)

with the -t argument called you can set an integer after it and the is the interval at which the program will rotate the background for the desktop 

the program reads the backgrounds from an img file that is kept locally 
![read_file](https://user-images.githubusercontent.com/68308394/155227849-b1d24485-f242-4d2b-b542-ed6102b1b8dc.PNG)
These imgs are dowloaded and stored so that it can be read in and processed for faster load times its better compared to an http request to get an img each time it
changes the background 

i had my time interval set to 1 minute so the program will rotate the image every minute and the images fit the screen extreamly well 
![background-change1](https://user-images.githubusercontent.com/68308394/155228143-10fb0a90-ec2c-4e23-ab0d-815efc66d017.PNG)
![background-change2](https://user-images.githubusercontent.com/68308394/155228165-0b582e81-80a5-4bc0-9758-f9ceeb252f00.PNG)
