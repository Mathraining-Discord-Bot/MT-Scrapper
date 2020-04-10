<h1 align="center">Welcome to MT-Scrapper 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version- 0.0.2-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: GNU GPLv3" src="https://img.shields.io/badge/License-GNU GPLv3-yellow.svg" />
  </a>
  <a href="https://twitter.com/coco33920" target="_blank">
    <img alt="Twitter: coco33920" src="https://img.shields.io/twitter/follow/coco33920.svg?style=social" />
  </a>
</p>

> The Scrapper for the Mathraining Website 

### 🏠 [Homepage](https://mathraining.be)

## Install

```bash
python3 -m pip install mathraining-scrapper
```

## Usage

**mathsite**
```python
#Import the mathsite library 
from mathraining.scrapper import mathsite
Mathraining = mathsite.Mathraining() #Create the Mathraining object
#Get the 10th best correctors sorted by total number of corrections
correctors = Mathraining.top_correctors(10)
#Get the 10th best correctors sorted by number of corrections within the last 2 weeks
correctors = Mathraining.top_correctors(10, True)
print(correctors)
```

**mathuser**
```python
from mathraining.scrapper import mathuser
User = mathuser.User(10) #Create the object user of id 10
print(User.name()) #print the name of the User
print(User.info()) #print all the informations about this User
```

See all the documentation here : https://therewillbeadocumentationsomeday.iassureyou

## Author

👤 **Charlotte Thomas**

* Twitter: [@coco33920](https://twitter.com/coco33920)
* Github: [@coco33920](https://github.com/coco33920)

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_