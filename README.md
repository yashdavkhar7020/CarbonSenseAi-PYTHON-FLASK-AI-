# Carbon Sense AI

## Overview
**Carbon Sense AI** is an AI-powered platform designed to help industries track, analyze, and reduce carbon emissions efficiently. Using real-time data processing, predictive analytics, and government-aligned recommendations, Carbon Sense AI empowers organizations to make data-driven sustainability decisions.

## Table of Contents
- [Problem Statement](#problem-statement)
- [Solution](#solution)
- [Deployed Application](#deployed-application)
- [Installation](#installation)
- [Web Application](#web-application)
  - [Frontend](#frontend)
  - [Backend](#backend)
- [Usage](#usage)
  - [Emissions Tracking](#emissions-tracking)
- [Example Login](#example-login)

## Problem Statement
Industries face growing pressure to track and reduce carbon emissions due to regulatory policies and climate change concerns. However, existing solutions are expensive, consultant-driven, and lack real-time tracking capabilities. Industries need a **cost-effective, automated, and AI-powered** tool to monitor and minimize their carbon footprint.

## Solution
**Carbon Sense AI** leverages AI-driven insights, real-time data collection, and predictive modeling to:
- Automate carbon emissions tracking.
- Provide actionable reduction strategies.
- Align with government sustainability norms.
- Offer an affordable alternative to consulting services.



## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/carbon-sense-ai.git
   ```
2. Navigate to the project directory:
   ```sh
   cd carbon-sense-ai
   ```

## Web Application
The Carbon Sense AI web platform consists of a **frontend (React/Streamlit)** and **backend (Flask API)**.

### Frontend
This folder contains the frontend code for the Carbon Sense AI web application.

#### Features
- **User Dashboard**: Visualizes emissions data with interactive charts.
- **Real-time Data Input**: Allows users to enter emissions data.
- **AI-Driven Insights**: Displays reduction strategies and analytics.

#### Installation
1. Navigate to the `frontend` directory:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Run the development server:
   ```sh
   npm run dev
   ```

### Backend
This folder contains the backend code for the Carbon Sense AI web application, built using Flask and Gunicorn.

#### Features
- **Real-time emissions tracking**
- **AI-powered carbon reduction suggestions**
- **Database storage for historical emissions data**

#### Installation
1. Navigate to the `backend` directory:
   ```sh
   cd backend
   ```
2. Create a virtual environment:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Start the Flask backend:
   ```sh
   python server.py
   ```

## Usage
### Emissions Tracking
1. **Enter emissions data** into the web dashboard.
2. **Get AI-powered recommendations** on how to reduce emissions.
3. **View trends and analytics** through charts and reports.



After logging in, you can explore features like emissions tracking, AI suggestions, and historical data analysis.

🚀 **Carbon Sense AI helps industries take actionable steps toward sustainability!**

