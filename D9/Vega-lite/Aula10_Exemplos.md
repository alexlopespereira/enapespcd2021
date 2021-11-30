#### Mapa do Brasil com Topojson
``` 
{
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "width": 600,
  "height": 500,
  "mark": "geoshape",
  "data": {
    "url": "https://servicodados.ibge.gov.br/api/v3/malhas/paises/BR?intrarregiao=UF&formato=application/json",
    "format": {"type": "topojson", "feature": "BRUF"}
  },
  "projection": {
    "type": "mercator"
  },
  "encoding": {
    "color": {"field": "properties.codarea", "type": "quantitative"}
  }
};
```