from clean_data import remove_duplicates

def data_setup():
    driver_data = {}
    sortedArray = remove_duplicates()
    count = 0
    for name in sortedArray:
        driver_data[count] = name
        count += 1

    return driver_data

def driver_search(driverId):
    driver_data = data_setup()
    if driverId in driver_data:
        return driver_data[driverId]
    else:
        return -1
    
print(driver_search(1052))