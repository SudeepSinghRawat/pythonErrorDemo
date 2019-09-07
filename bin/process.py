
import data

def getName(roll_number):
    for obj in data.classlist :
        if obj.roll_number in roll_number:
            print(obj.name + " "+ obj.roll_number)

