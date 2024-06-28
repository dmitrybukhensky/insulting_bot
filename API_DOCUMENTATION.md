### API Documentation for "Хуефицикатор" Bot

#### Overview
The "Хуефицикатор" Bot API provides a simple interface for interacting with the bot's core functionalities: processing messages to apply the bot's unique transformation logic, and generating insults. This document outlines how to interact with the API endpoints.

---

### Base URL
The base URL for the API is the domain where the bot is hosted. For local development, this might be `http://127.0.0.1:5000`. Replace this base URL with your production URL when deployed.

---

### Endpoints

#### Process Message
- **URL:** `/process`
- **Method:** `POST`
- **Description:** Processes a given message using the bot's logic and returns the transformed message.
- **Body Parameters:**
  - `message`: The message text to be processed (String).
- **Success Response:**
  - **Code:** 200 OK
  - **Content:** `{ "processed_message": "Transformed message text" }`
- **Error Response:**
  - **Code:** 400 BAD REQUEST
  - **Content:** `{ "error": "Message is required" }`
- **Example:** 
  ```json
  {
    "message": "Пример"
  }
  ```

#### Generate Insult
- **URL:** `/get_insult`
- **Method:** `GET`
- **Description:** Generates a random insult.
- **Success Response:**
  - **Code:** 200 OK
  - **Content:** `{ "insult": "Insult text" }`
- **Error Response:**
  - **Code:** 500 INTERNAL SERVER ERROR
  - **Content:** `{ "error": "An error occurred" }`

---

### Usage Example

#### Process Message with cURL
```bash
curl -X POST http://127.0.0.1:5000/process \
     -H "Content-Type: application/json" \
     -d '{"message": "Пример"}'
```

#### Get Insult with cURL
```bash
curl http://127.0.0.1:5000/get_insult
```

---

### Error Handling
Errors are returned as standard HTTP status codes. The body of an error response will contain more details about the nature of the error.

- `400 Bad Request`: Your request is invalid or missing required parameters.
- `500 Internal Server Error`: We had a problem with our server. Try again later.

---

### Security
Ensure secure transmission of your requests by using HTTPS and keep your bot token confidential. Do not expose sensitive or personal information through the API.

---

### Support
For any issues or questions regarding the API, please contact the support team at `support@example.com`.

---

**Note:** This documentation assumes a local development setup. Adjust URLs and deployment configurations as necessary for your production environment.