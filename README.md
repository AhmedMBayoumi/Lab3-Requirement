# Samsung Devices API

This API allows you to manage a list of Samsung devices, including phones and tablets. It supports operations such as retrieving device information, creating new devices, updating existing devices, and deleting devices.

## API Endpoints

### 1. Get all devices

**GET** `/devices`

Retrieves a list of all Samsung devices.

**Response:**

```json
[
  {
    "id": 1,
    "name": "Samsung Galaxy S21",
    "category": "phone",
    "price": 799.99
  },
  {
    "id": 2,
    "name": "Samsung Galaxy Tab S7",
    "category": "tablet",
    "price": 649.99
  }
]
```
2. Get a single device by valid ID

GET /devices/{id}

Retrieves a specific device by its ID.

Response (valid ID):

```json
{
  "id": 1,
  "name": "Samsung Galaxy S21",
  "category": "phone",
  "price": 799.99
}
```
3. Get a single device by invalid ID

GET /devices/{id}

If the device with the specified ID does not exist, the API will return an error.

Response (invalid ID):

```json

{
  "error": "Device not found"
}
```
4. Create a new device

POST /devices

Creates a new Samsung device.

Request Body (JSON):

```json

{
  "name": "Samsung Galaxy Tab A8",
  "category": "tablet",
  "price": 299.99
}
```
Response:

```json
{
  "id": 3,
  "name": "Samsung Galaxy Tab A8",
  "category": "tablet",
  "price": 299.99
}
```
5. Create a device with missing fields (invalid input)

POST /devices

If required fields are missing in the request body, the API will return a validation error.

Request Body (Invalid JSON):

```json

{
  "name": "Samsung Galaxy Fold"
}
```
Response:

```json

{
  "error": "Missing required fields: category, price"
}
```
6. Update an existing device

PUT /devices/{id}

Updates the price of an existing device.

Request Body (JSON):

```json

{
  "price": 1099.99
}
```
Response:

```json

{
  "id": 1,
  "name": "Samsung Galaxy S21",
  "category": "phone",
  "price": 1099.99
}
```
7. Delete a device by valid ID

DELETE /devices/{id}

Deletes a Samsung device by its ID.

Response:

```json

{
  "message": "Device deleted successfully"
}
```
Authentication

All endpoints require a Bearer token in the Authorization header for authentication.

Example:

Authorization: Bearer adminSecretToken


If the token is invalid or missing, the API will return a 401 Unauthorized error.
Error Handling

In case of errors, the API returns a JSON response with an error message:

```json

{
  "error": "Unauthorized"
}
```
Setup and Running the API

    Clone the repository.

    Install the necessary dependencies with:

    bash
