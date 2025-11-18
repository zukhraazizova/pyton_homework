from smartphone import Smartphone


catalog =[
    Smartphone("samsung","s25","+712345678"),
    Smartphone("iphone","17pro","+78906543"),
    Smartphone("xioami","13","+789065432"),
    Smartphone("poco","f7","+78564542"),
    Smartphone("honor","13i","+73563562")
]

for smartphone in catalog: 
    print(smartphone.brand, "-", smartphone.model, ".", smartphone.phone)
