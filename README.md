# TimeSeries-Forecaster-AI (Docker Edition)

Automatic ARIMA + GARCH forecasting pipeline deployed using a **multi-container Docker architecture**.

This version of the project focuses on containerization, reproducibility, and orchestration using Docker Compose, as required for the TP “Run your software anywhere with Docker” in the Technological Foundations of Computer Science course.

##  Objective

The goal of this project is to demonstrate how a data science pipeline can be:
- split into **multiple logical steps**,
- executed in **separate Docker containers**,
- orchestrated using **docker compose**,
- and produce persistent results using **Docker volumes**.

##  Application Architecture (Multi-Container)

The pipeline is divided into **three containers**, each with a single responsibility:

1. **data-ingestor**
   - Loads and cleans the raw time-series dataset
   - Saves the cleaned data to a shared volume

2. **model-trainer**
   - Trains ARIMA and GARCH models
   - Generates forecasts
   - Saves results to a shared volume

3. **visualizer**
   - Generates and saves forecast visualizations (PNG)
   - Uses outputs produced by previous containers

All containers share a common directory using Docker volumes.

##  Project Structure
```
TimeSeries-Forecaster-AI/
├── data/
│ └── gld_price_data.csv
├── src/
│ ├── init.py
│ ├── preprocess.py
│ ├── models.py
│ ├── train.py
│ └── visualize.py
├── shared/
│ ├── processed/ # cleaned data
│ ├── models/ # trained models / forecasts
│ └── outputs/ # figures and final results
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── pyproject.toml
├── poetry.lock
└── README.md
```
## Requirements

Before running the application, make sure you have:

- **Docker Desktop** installed
- **Docker Compose** enabled (included with Docker Desktop)

No Python or Poetry installation is required on the host machine.

## How to Run the Application (Required by the TP)

### Step 1 — Clone the repository
```bash
git clone https://github.com/jouinisayf/TimeSeries-Forecaster-AI-Docker-Edition-
cd TimeSeries-Forecaster-AI
```

### Step 2 — Build and start the containers
```bash
docker compose up --build
```

This command will:
build the Docker image, start the three containers in the correct order and execute the full forecasting pipeline automatically.

### Step 3 — Check the results on your local machine

All results are persisted using Docker volumes and available locally in the shared/ directory:
```
shared/
├── processed/
│   └── cleaned_series.csv
├── models/
│   └── forecast.csv
└── outputs/
    └── forecast.png

cleaned_series.csv → cleaned time-series data

forecast.csv → numerical forecast results

forecast.png → ARIMA + GARCH forecast visualization
```

### Stop the application

To stop and remove the containers:
```bash
docker compose down
```
The generated results remain available in the shared/ directory.

## Validation for the TP

This project satisfies the requirements:

Multi-container Docker application

Docker Compose orchestration

Clear execution steps using docker compose up

Persistent outputs using volumes

Reproducible execution on any machine

## License

This project is released under the MIT License.
