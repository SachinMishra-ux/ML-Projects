## Dockerization of prediction Service

- go to the Prediction_Service folder. Then Start docker demon
- then
```
docker build -t houseprice . # homeprice means name of the image  & . means from current directory
```

```
docker run houseprice
```
```
docker run -p 8501:8501 houseprice
```