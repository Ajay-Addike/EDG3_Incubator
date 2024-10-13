# EDG3 - AI-Powered Business Incubation Website

This project is an AI-powered platform called **EDG3**, designed to assist users in generating business ideas and strategies through an interactive AI chatbot interface. The website has a cyberpunk-inspired theme and provides responses to user inputs in an engaging, card-based format.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Details](#api-details)
- [License](#license)

## Features

- Interactive AI chatbot interface that responds to user prompts.
- Cyberpunk-themed design with dynamic card-based UI.
- Modal-based expanded views for in-depth details.
- Fetches and displays responses from an external API.
- API integration with **EDG3 Incubator** for business incubation advice.

## Technologies Used

- **HTML/CSS**: For structuring and styling the webpage.
- **JavaScript**: For handling user inputs and rendering responses.
- **Flask**: Backend web framework used for handling API calls.
- **Flask-CORS**: For handling cross-origin resource sharing.
- **Bootstrap 5.3**: For responsive design.
- **Requests**: To handle external API requests.

## Installation

To run this project locally, follow these steps:

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/edg3-ai-incubator.git
    ```

2. Navigate to the project directory:
    ```bash
    cd edg3-ai-incubator
    ```

3. Create and activate a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the Flask development server:
    ```bash
    python app.py
    ```

2. Open your browser and navigate to `http://localhost:5000` to view the application.

3. Interact with the chatbot by entering your business-related prompts, and receive helpful insights from the AI.

## API Details

The chatbot interface makes a POST request to the EDG3 Incubator API hosted on Azure.

- **Endpoint**: `https://edg3incubator-dndyakd9f6a0hbhk.eastus-01.azurewebsites.net/api/chat`
- **Method**: `POST`
- **Request body**:
    ```json
    {
      "prompt": "<your-prompt-here>"
    }
    ```

The API returns a structured response, which is then displayed in a card format on the UI.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
