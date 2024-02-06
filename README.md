# CLI Habit Tracking app

A Habit Tracking app designed to monitor daily and weekly habits. 
This app allows you to create one of five preset habits, check them off, 
analyze your progress, and stay motivated with habit streaks. 
It's an easy-to-use tool to help you establish positive habits.

## Features of the app
- Create: Choose from a list of 5 pre-set habits and set their period (daily or weekly).
- Check off: Mark your habits as completed to keep track of your progress.
- Analyze: View a list of all habits, habits with the same period, and the longest streaks.
- Motivate: Use streaks to stay motivated and establish positive habits.

## Installation

To get started, make sure you have Python installed on your machine. 
Then, clone this repository and navigate to the project directory.

```shell
pip install -r requirements.txt
```
For Questionary to work correctly you might need to change a few settings:
In main.py - rightclick the folder. Select "Modify run configeration" 
Then click on Modify options as indicated with the screenshot below:

!(![image](https://github.com/Jacobventer/Habit-Tracker/assets/149387555/9a0dd814-55f6-4eda-b3eb-768470bc504b)
)

Make sure that "Emulate terminal in output console is turned on"

![Output console](![image](https://github.com/Jacobventer/Habit-Tracker/assets/149387555/8076af52-6962-4461-b1c8-e95c6df202ff))


## Usage
Start the CLI app by running:
```shell
python main.py

```

Follow the instructions on the screen to create habits , 
check them off, and analyze your progress. 

Use the arrow keys and enter to select the desired option:

![Main menu](![image](https://github.com/Jacobventer/Habit-Tracker/assets/149387555/bf8a6140-79d7-40d3-a016-377fc8acddb8))

Use the easy to use menu to navigate to the desired option

![5 pre set habits](![image](https://github.com/Jacobventer/Habit-Tracker/assets/149387555/f8e4e723-258f-4edc-ae48-9a2c581d598d))

## Testing
To run the tests for the app, ensure you have the pytest package installed.
If not, you can install it using:
```shell
pip install pytest
``` 
Then run the tests with:

```shell
pytest test.py
``` 
Note: Ensure that you have the required dependencies installed before running tests.

Testing is a crucial part of the software development lifecycle, contributing to the creation
of high-quality and reliable software. It provides assurance that the code behaves
as it should and help teams deliver better products to users.

Feedback is welcome.


## Contributing
If you have suggestions or encounter issues, feel free to open an issue or create a pull request.
