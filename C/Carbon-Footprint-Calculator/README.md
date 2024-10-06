# **Carbon Footprint Calculator**

An interactive web application that calculates your annual carbon footprint based on your daily activities, including transportation, home energy use, dietary habits, and waste management. The goal is to raise environmental awareness and encourage sustainable living by providing personalized feedback and suggestions for reducing carbon emissions.

---

## **Table of Contents**

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)

---

## **Features**

- **Transportation Emissions Calculation**
  - Calculates emissions from car travel, public transportation, and flights.
- **Home Energy Use Analysis**
  - Accounts for electricity, natural gas, fuel oil, and propane usage.
- **Dietary Impact Assessment**
  - Considers the carbon footprint of different diets: meat-heavy, average, vegetarian, and vegan.
- **Waste and Recycling Evaluation**
  - Factors in recycling habits and their impact on emissions.
- **User-Friendly Web Interface**
  - Interactive forms for data input and clear presentation of results.
- **Personalized Suggestions**
  - Offers practical tips to reduce your carbon footprint based on your inputs.
- **Responsive Design**
  - Accessible on various devices, including desktops, tablets, and mobile phones.

---

## **Prerequisites**

- **Python 3.7 or higher**
- **pip package manager**
- **Virtual Environment (optional but recommended)**

---

## **Installation**

Follow these steps to set up the project on your local machine.

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/carbon-footprint-calculator.git
cd carbon-footprint-calculator
```

### **2. Create a Virtual Environment**

It's recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

### **3. Upgrade pip**

```bash
pip install --upgrade pip
```

### **4. Install Dependencies**

```bash
pip install -r requirements.txt
```

Ensure that the installed packages match the versions specified in `requirements.txt`:

```
Flask==2.3.2
Werkzeug==3.0.4
```

### **5. Run the Application**

```bash
python app.py
```

The application will start running on `http://127.0.0.1:5000/`.

---

## **Usage**

### **Access the Application**

Open your web browser and navigate to `http://127.0.0.1:5000/`.

### **Input Your Data**

1. **Transportation Emissions**

   - Enter your average weekly miles driven by car.
   - Provide your car's fuel efficiency (mpg).
   - Input miles traveled by bus and train.
   - Specify the number of flights taken per year.

2. **Home Energy Use**

   - Enter your average monthly electricity usage in kWh.
   - Provide natural gas, fuel oil, and propane usage if applicable.

3. **Dietary Impact**

   - Select your diet type from the options provided.

4. **Waste and Recycling**
   - Indicate whether you recycle paper, plastic, glass, and metal.

### **Calculate and View Results**

- Click the **Calculate** button to submit your data.
- The results page will display:
  - A breakdown of your annual emissions by category.
  - Total annual emissions in pounds and metric tons of CO₂.
  - Comparison with the national average.
  - Personalized suggestions to reduce your carbon footprint.

### **Calculate Again**

- Use the **Calculate Again** button to return to the input form and reassess with different data.

---

## **Project Structure**

```
carbon-footprint-calculator/
├── app.py
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── index.html
│   └── results.html
├── static/
│   ├── style.css
├── README.md
```

- **app.py**: The main Flask application file containing routes and logic.
- **requirements.txt**: Lists the Python dependencies and their versions.
- **templates/**: Contains HTML templates for rendering web pages.
  - **base.html**: The base template that includes common elements.
  - **index.html**: The home page with the input form.
  - **results.html**: Displays calculation results and suggestions.
- **static/**: Stores static files like CSS and images.
  - **style.css**: Custom styles for the application.
  - **screenshots/**: Contains images used in the README.
- **README.md**: Comprehensive guide and documentation for the project.

---

## **Technologies Used**

- **Programming Language**: Python 3
- **Web Framework**: Flask
- **Frontend Libraries**:
  - **Bootstrap 5**: For responsive design and styling.
- **HTML/CSS**: Web page structure and styles.

### **Troubleshooting**

#### **ImportError: cannot import name 'url_quote' from 'werkzeug.urls'**

If you encounter the following error:

```
ImportError: cannot import name 'url_quote' from 'werkzeug.urls'
```

This is due to a version incompatibility between Flask and Werkzeug. Ensure that you have compatible versions installed:

- **Flask**: `2.3.2` or higher
- **Werkzeug**: `3.0.4` or compatible with your Flask version

#### **Steps to Resolve**

1. **Update `requirements.txt`**:

   ```
   Flask==2.3.2
   Werkzeug==3.0.4
   ```

2. **Reinstall Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Verify Installed Versions**:

   ```bash
   pip show Flask
   pip show Werkzeug
   ```

## **Contact**

For any questions or suggestions, feel free to reach out:

- **Email**: aswinpkumar03@gmail.com
- **GitHub**: [AswinPKumar01](https://github.com/AswinPKumar01)

---

Thank you for using the Carbon Footprint Calculator! Together, let's make a positive impact on the environment.
