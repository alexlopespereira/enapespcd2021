#### Exemplo: Anomalia de temperatura
```
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {
    "url": "https://raw.githubusercontent.com/alexlopespereira/enapespcd2021/main/data/originais/aquecimento_global/global_temperature_anomalies_tratado.csv",
    "format": {"type": "csv"}
  },
  "mark": "line",
  "encoding": {
    "x": {"timeUnit": "month", "field": "data1"},
    "y": {"field": "Anomaly", "type": "quantitative"},
    "color": {"field": "ano", "type": "ordinal", "scale": {"scheme": "turbo"}}
  }
}
```