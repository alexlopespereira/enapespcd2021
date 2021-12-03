#### Histograma com threshold
``` 
{"$schema": "https://vega.github.io/schema/vega-lite/v5.json",
"data": {"values": [{"Day": 1, "Value": 54.8},{"Day": 2, "Value": 112.1},{"Day": 3, "Value": 63.6},{"Day": 4, "Value": 37.6},{"Day": 5, "Value": 79.7},{"Day": 6, "Value": 137.9},{"Day": 7, "Value": 120.1},{"Day": 8, "Value": 103.3},{"Day": 9, "Value": 394.8},{"Day": 10, "Value": 199.5},{"Day": 11, "Value": 72.3},{"Day": 12, "Value": 51.1},{"Day": 13, "Value": 112.0},{"Day": 14, "Value": 174.5},{"Day": 15, "Value": 130.5}]},      
"layer": [  {
    "mark": "bar",
    "encoding": {
      "x": {"field": "Day", "type": "ordinal"},
      "y": {"field": "Value", "type": "quantitative"}
    }
  }, 
  {
    "mark": "bar",
    "transform": [{"filter": "datum.Value >= 300"},{"calculate": "300", "as": "baseline"}
    ],
    "encoding": {
      "x": {"field": "Day", "type": "ordinal"},
      "y": {"field": "baseline", "type": "quantitative", "title": "PM2.5 Value"},
      "y2": {"field": "Value"},
      "color": {"value": "red"}
    }  }]}
```
