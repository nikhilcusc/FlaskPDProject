# FlaskPDProject
Loads the data from PD_challange_dataset.xlsx. Plots temperature and consumption on top of each other using ChartJS. 
The temperature has a background fill so it is easier to differentiate between temperature and consumption.

The Slider allows to change number of steps, start index and end index. To use preset step values use the toggle button. This cycles through, hourly, daily, biweekly, monthly and yearly data.

Because we have so many datapoints, it is advisable to update it as soon as the page has loaded. The landing page has default slider values.
The default value of steps is 50 steps. When you click on update the graphs picks every 50th points to display so it is easier to view.  

Here is a table of my loading times (in seconds):

|Browser->|Firefox | Chrome| 
|------------ | -------------|---------------|
|Run 1 | 301.27 | 51.94|
|Run 2 | 301.80 | 48.69|
|Average | 301.535 | 50.315|

To run Flask quickly, I have a .sh file called runFlask.sh

## Screenshots
Landing page
![Screenshot1](/Screenshots/graph_landing.JPG)
Other Pages
![Screenshot2](/Screenshots/graph_screenshot2.JPG)
![Screenshot3](/Screenshots/graph_monthly.JPG)


## D3 approach
This method has a problem where d3 linechart plots only some points, about 4500 points out of 35181. Please find code on linechart branch.

If you have any solutions, please post it here:
[d3-linechart-plots-only-some-points](https://stackoverflow.com/questions/57137577/d3-linechart-plots-only-some-points)
TIA
