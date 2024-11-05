# Random Item Pair Generator
This Streamlit application allows users to input two lists of items and generates randomized pairs between them. It's particularly useful for tasks like creating random team assignments, pairing questions and answers, or any scenario requiring random pairings.

# Features
* **Random Pair Generation:** Produces random pairs from two user-provided lists.
* **Customizable Appearance:** Utilizes Streamlit's theming and custom CSS for an enhanced visual experience.

# Installation
Clone the Repository:

``git clone https://github.com/yourusername/random-item-pair-generator.git
cd random-item-pair-generator
``

Create and Activate a Virtual Environment:

``python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
``

Install Dependencies:

``pip install -r requirements.txt``

Note: Ensure that requirements.txt includes all necessary dependencies, such as streamlit.

# Usage
Run the Application:

``streamlit run app.py``

Access the App:

Open your web browser and navigate to http://localhost:8501 to interact with the app.

# How to Use
Input Items:

* Enter items for List 1 in the first text area, separated by commas.
* Enter items for List 2 in the second text area, separated by commas.

Generate Pairs:

Click the "Generate Random Pairs" button.
The app will display randomized pairs, ensuring the number of pairs matches the length of the shorter list.

# Customization

* Theming: Modify the .streamlit/config.toml file to adjust the app's theme, including colors and fonts.
* CSS Styling: Update the custom CSS within the app.py file to change the appearance of buttons, text areas, and other elements.

# License
This project is licensed under the GPL-3 License. See the LICENSE file for details.

