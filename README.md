# gemastik-ml

This project was generated via [manage-fastapi](https://ycd.github.io/manage-fastapi/)! :tada:

## License

This project is licensed under the terms of the MIT license.

## Endpoint

- **URL:** `http://localhost:8000/v1/`
- **Method:** `POST`
- **Request Body:**

```json
{
    "nitrogen": 42,
    "phosphorous": 90,
    "potash": 43,
    "temperature": 20,
    "humidity": 100,
    "ph": 6.5,
    "rainfall": 200
}
```

- **Response:**

```json
{
    "message": "Hello World",
    "plan_recomendation": "papaya"
}
```

### Description

This API endpoint accepts a POST request to `/v1/` and expects a JSON payload in the request body. The payload should contain the following fields:

- `nitrogen` (float): The nitrogen value.
- `phosphorous` (float): The phosphorous value.
- `potash` (float): The potash value.
- `temperature` (float): The temperature value.
- `humidity` (float): The humidity value.
- `ph` (float): The pH value.
- `rainfall` (float): The rainfall value.

The API will process the input data and return a JSON response with the following fields:

- `message` (string): A greeting message, in this case, "Hello World".
- `plan_recomendation` (string): A recommendation for a plant, in this case, "papaya".

This endpoint can be used to send agricultural data and receive a plan recommendation along with a greeting message.

Make sure to replace `http://localhost:8000` with the appropriate base URL of your deployed FastAPI application.
