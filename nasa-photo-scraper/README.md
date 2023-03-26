# NASA daily photo scraper 

<img src="Images/readme_img.jpg"
     alt="Markdown Monster icon"
     />

## Description

This is a script that aims to download all the images from the daily image archive of NASA and save them locally.


## Getting Started

### Dependencies

* Python 3
* Ubuntu (or any other Unix system) 

### Installing

* Clone the main repository
* ``pip install -r requirements.txt``

### Executing program

* ``python3 index.py``
<br> If you want to modify the amount of images that the program will put you can modify the hard_limit variable, -1 to download all, and any other positive number to download that certain amount.

### Trouble shooting
* If the program has problems make sure you don't delete the Images folder that comes with the program, it will break it. If you want to move the program to another place make sure to create a `Images` folder along it.

## Help

This script at the moment only is tested in Unix, running it in Windows might result in errors.

## Authors
[@marc-marcos](https://github.com/marc-marcos)

## License

This project is licensed under the GPL License - see the LICENSE.md file for details