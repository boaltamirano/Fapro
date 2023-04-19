## Get development unit 

```sh
curl -X GET '{{host}}/unitDevelop?date=10-1-2022' 
```

### Query Parameters

| Field     | Type                  | Description                                                 |
|-----------|-----------------------|-------------------------------------------------------------|
| date    | `string` **required** | La fecha de la que se va a obtener la unidad de formato. |
### Response

```json
{
    "Unidad de Fomento": 31044.63
}
```

<br>

[`Back`](../README.md)