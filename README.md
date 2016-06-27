# Imgist - As simple Python app to generate graph images

## Syntax for generating the image: 

#### Examples: 
```
/graph/Monthly_Graph/?x=m&y=1,2,3,4,5&a=20160501
/graph/Weekly_Graph/?x=w&y=1,2,3,4,5
/graph/Daily_Graph/?x=d&y=1,2,3,4,5
```

#### General Syntax: 
```
/graph/<graph_title>/?x=<time_periods>&y=<y_coordinates>[&a=<anchor_date>]
```
graph title = User defined title for the graph, with underscore (_) to represent spaces. (optional)

time period = Periodicy of the graph which can be monthly, weekly, or daily. Acceptable values are: `m`, `w`, or `d`

y coodinates = comma seperated numbers; final datapoint goes last 

anchor date = the date of the final data point in yyyymmdd format. if ommited, imgist will assume today's date (optional)


## Licensing

Imgist is open sourced under the MIT license. See <https://opensource.org/licenses/MIT>

```
Copyright (c) 2016 Kinnek, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```