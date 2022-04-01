## PublicWWW Scraper (Api)

This script is capable of getting unlimited data from publicwww.com which can be hard and very slow using selenium or other scraping tools


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install beautifulsoup4
```

## Usage

```bash
python main.py
```
## Steps
 - Change Cookies 

   Go to line 4 and add new cookies from the publicwww request in your browser (chrome/firefox devtool)
```python
COOKIES = ""  
```


 - Changing keywords list

   Go to line 61 and add/remove keywords
```python
keywords = ['notification', 'email', 'email newsletter']  
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## To-Do
 - Adding Threads
 - Bypassing Cookies
 - Bypassing shadow ban


## License
[MIT](https://choosealicense.com/licenses/mit/)