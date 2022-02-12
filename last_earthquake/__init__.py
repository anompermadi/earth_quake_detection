def data_extraction():
    """
    Date: 11 Februari 2022
    Time: 21:25:16 WIB
    Magnitude: 5.2
    Depth: 10 km
    Location: Lat=5.77 LU Lon=124.43 BT
    Description: 267 km BaratLaut TAHUNA-KEP.SANGIHE-SULUT
    Impact: tidak berpotensi TSUNAMI
    :return:
    """
    res = dict()
    res["date"] = "11 Februari 2022"
    res["time"] = "21:25:16 WIB"
    res["magnitude"] = 5.2
    res["depth"] = "10 km"
    res["location"] = {"lat": "5.77 LU",
                       "lon": "124.43 BT"}
    res["description"] = "267 km BaratLaut TAHUNA-KEP.SANGIHE-SULUT"
    res["impact"] = "tidak berpotensi TSUNAMI"
    return res


def show_data(result):
    print("Last Indonesia earth quake")
    print(f"Date {result['date']}")
    print(f"Time {result['time']}")
    print(f"Magnitude {result['magnitude']}")
    print(f"Depth {result['depth']}")
    print(f"Location: Lat = {result['location']['lat']}, Lon = {result['location']['lon']}")
    print(f"Description {result['description']}")
    print(f"Impact {result['impact']}")