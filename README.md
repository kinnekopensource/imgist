# Imgist - As simple Python app to generate graph images

## Syntax for generating the image: 

#### Examples: 
```
/graph/Monthly_Graph/?x=m&y=1,2,3,4,5&a=20160501
/graph/Weekly_Graph/?x=w&y=1,2,3,4,5
/graph/Daily_Graph/?x=d&y=1,2,3,4,5
```

#### General Syntax: 
/graph/<graph_title>/?x=<time_periods>&y=<y_coordinates>[&a=<anchor_date>]

graph title = User defined title for the graph, with underscore (_) to represent spaces. (optional)
time period = Periodicy of the graph which can be monthly, weekly, or daily. Acceptable values are: `m`, `w`, or `d`
y coodinates = comma seperated numbers; final datapoint goes last 
anchor date = the date of the final data point in yyyymmdd format. if ommited, imgist will assume today's date (optional)
