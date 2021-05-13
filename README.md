# General Info  
<ul>
    <li>Developed on Fedora Linux, Python 3.9</li>
    <li>Tested on Linux and Windows 10</li>
</ul>

## Features
Bonuses are completed so you can sort data by retweet, reply, like or date.

## Installation
Clone the project and create a virtual environment and activate it. Then install requirements by:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```
 After running server you can see results in http://127.0.0.1:5000
 
## Used Libraries
<ul>
    <li>Flask</li>
    <li>Twint</li>
</ul>
 You can find Twint dependencies in requirements.txt
 
## Notes

  If you run the project first time, It'll use the data fetched before. That's why if you
want to use new data, you have to delete tweet_data.csv file first. 
