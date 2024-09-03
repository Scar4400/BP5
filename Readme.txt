### Running the Application

1. **Install dependencies**:
    
    ```bash
    pip install -r requirements.txt
    
    ```
    
2. **Build the Docker images**:
    
    ```bash
    docker-compose build
    
    ```
    
3. **Run the containers**:
    
    ```bash
    docker-compose up
    
    ```
    
4. **Access the API**:
    - The Flask API will be available at `http://localhost:5000/predict`.
    - You can test the API with a `POST` request.

---

This streamlined guide incorporates data fetching, preprocessing, feature engineering, model training, and API serving, all within a Dockerized environment. Let me know if you need any more assistance!
