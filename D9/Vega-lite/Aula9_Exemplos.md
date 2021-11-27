#### Exemplo: Importar dados em formato json
```
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {
    "url": "https://raw.githubusercontent.com/alexlopespereira/enapespcd2021/main/data/originais/aquecimento_global/global_temperature_anomalies_tratado.json",
    "format": {"type": "json", "property": "data.values"}
  },
  "mark": "line",
  "encoding": {
    "x": {"timeUnit": "month", "field": "data1"},
    "y": {"field": "Anomaly", "type": "quantitative"},
    "color": {"field": "ano", "type": "ordinal", "scale": {"scheme": "turbo"}}
  }
}
```

#### Exemplo: Scatter Plot de CO2 vs Temperatura (sem filtro)
```
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {
    "url":"https://raw.githubusercontent.com/alexlopespereira/enapespcd2021/main/data/originais/aquecimento_global/temperature_anomalies_co2.csv", 
  "format":{"type": "csv"}
  },
  "width": 400,
  "mark": "point",
  "encoding": {
    "x": {"field": "co2", "type": "quantitative"},
    "y": {"field": "Anomaly", "type": "quantitative"}    
  } 
}
```

#### Exemplo: Scatter Plot de CO2 vs Temperatura (com filtro)
```
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {
    "url":"https://raw.githubusercontent.com/alexlopespereira/enapespcd2021/main/data/originais/aquecimento_global/temperature_anomalies_co2.csv", 
  "format":{"type": "csv"}
  },
  "width": 400,
  "mark": "point",
  "transform": [ {"filter": {"field":"mes", "equal":"jun"} }   ],
  "encoding": {
    "x": {"field": "co2", "type": "quantitative"},
    "y": {"field": "Anomaly", "type": "quantitative"}    
  } 
}
```


###Exemplo Scatter plot e regressao linear da precipitação e vento em seattle
```
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {"url": "data/seattle-weather.csv"},
  "layer": [
    {
      "mark": "point",
      "encoding": {
        "x": {"field": "wind","type": "quantitative"},
        "y": {"field": "precipitation", "type": "quantitative"
        }
      }
    },
    {
      "mark": "line",
      "transform": [{"regression": "precipitation", "on":"wind"}],
      "encoding": {
        "x": {"field": "wind", "type": "quantitative"},
        "y": {"field": "precipitation","type": "quantitative"},
        "color":{"value":"red"}
      }      
    }
  ]
}
```