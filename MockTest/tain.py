"""ขบวนรถธรรมดาที่ 283"""
def main(tain) :
    """ขบวนรถธรรมดาที่ 283"""
    tain_station = {}
    err = 0
    check = 0
    while True :
        satane = input()
        if satane == "Done" :
            break
        satane = satane.split(", ")
        tain_station[satane[0]] = float(satane[1])
        if float(satane[1]) - check < 0 :
            err += 1
            break
        if satane[0] == tain[1] :
            break
    value = list(tain_station.values())
    if value[len(tain_station) - 1] - value[0] < 0 or err > 0 :
        print("Error")
    else :
        print(f"{value[len(tain_station) - 1] - value[0]:.2f}")
main(input().split(", "))
