

# Python Citation Project

## Description
This project is a Python script that fetches data from a paginated API endpoint provided by BeyondChats. It identifies sources for each response and returns the citations as a JSON array. Additionally, there is an optional Flask app provided for a user-friendly interface to access the citations.

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Saherpathan/Citation_project.git
   cd Citation_project
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Script

To run the script and fetch citations from the API, execute the following command:
```bash
python main.py
```

The citations will be printed to the console.

### Running the Flask App 

1. Ensure Flask is installed:
   ```bash
   pip install Flask
   ```

2. Run the Flask app:
   ```bash
   python app.py
   ```

3. Access the endpoint:
   Open your browser and navigate to [http://127.0.0.1:5000/citations](http://127.0.0.1:5000/citations) to view the citations in a user-friendly interface.

## Project Structure

- `main.py`: The main Python script for fetching data and processing citations.
- `app.py`: Flask application script for providing a user interface.
- `requirements.txt`: Contains a list of Python dependencies.
- `README.md`: This file providing information about the project.

## API Endpoints

`/citations`: Returns citations for all objects retrieved from the API.

<<<<<<< HEAD
## Credits

This project is developed as part of the assignment by BeyondChats.

=======
>>>>>>> 09aed04 (Updates)
## License

[MIT License](LICENSE)

## Contributor
SAHER PATHAN