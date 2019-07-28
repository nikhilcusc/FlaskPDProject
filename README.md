# FlaskPDProject
Loads the data from PD_challange_dataset.xlsx. Plots temperature and consumption on top of each other. 
The temperature has a background fill so it is easier to differentiate between temperature and consumption.

The Slider allows to change number of steps, start index and end index. 

Because we have so many datapoints, it is advisable to update it as soon as the page has loaded.  
Here is a table of my loading times (in seconds):

|Browser->|Firefox | Chrome| 
|------------ | -------------|---------------|
|Run 1 | 301.27 | 51.94|
|Run 2 | 301.80 | 48.69|
|Average | 301.535 | 50.315|

To run Flask quickly, I have a .sh file called runFlask.sh
