import asyncio
from time import sleep

from data import get_data
import route

if __name__=="__main__":
    get_data()
    route.app.run(debug=True)