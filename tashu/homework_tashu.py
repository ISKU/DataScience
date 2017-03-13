import csv
from operator import itemgetter


def get_top10_station(tashu_dict, station_dict):
    """
    [역할]
    정류장 Top10 출력하기
    대여 정류장과 반납정류장을 합한 총 사용빈도수 Top10

    [입력]
    tashu_dict : csv.DictReader 형태의 타슈대여정보
    station_dict : csv.DictReader 형태의 정류장 정보

    [출력]
    Top10 정류장 리스트
    ex.) [[정류장 이름1, 정류장 번호1, 정류장1 count], [정류장 이름2, 정류장 번호2, 정류장2 count], .....] 형태
    """

    station_list = [{}]
    rent_list = []

    for info in station_dict :
        station_list.append(info)

    for i in range(0, 227, 1) :
        rent_list.append({'station': i, 'count': 0})

    for rent in tashu_dict :
        if rent['RENT_STATION'] == '' or rent['RETURN_STATION'] == '' :
            continue
        rent_list[int(rent['RENT_STATION'])]['count'] += 1
        rent_list[int(rent['RETURN_STATION'])]['count'] += 1

    rent_list.sort(key = itemgetter('count'), reverse = True)
   
    result = []
    for i in range(0, 10, 1) :
        result.append([\
            station_list[rent_list[i]['station']]['NAME'],\
            str(rent_list[i]['station']),\
            rent_list[i]['count'] ])

    return result
 
def get_top10_trace(tashu_dict, station_dict):
    """
    [역할]
    경로 Top10 출력하기
    (대여정류장, 반납정류장)의 빈도수 Top10

    [입력]
    tashu_dict : csv.DictReader 형태의 타슈대여정보
    station_dict : csv.DictReader 형태의 정류장 정보

    [출력]
    Top10 경로 리스트
    ex.) [[출발정류장 이름1, 출발정류장 번호1, 반납정류장 이름1,
        반납정류장 번호2, 경로 count], [출발정류장 이름2, 출발정류장 번호2,
        반납정류장 이름2,  반납정류장 번호2, 경로count2], .....] 형태
    """

    w, h = 227, 277
    rent_list = [[0 for x in range(w)] for y in range(h)]
    station_list = [{}]

    for info in station_dict :
        station_list.append(info)

    for i in range(1, 227, 1) :
        for j in range(1, 227, 1) :
            rent_list[i][j] = {'rent': i, 'return': j, 'count': 0}

    for rent in tashu_dict :
        if rent['RENT_STATION'] == '' :
            continue
        if rent['RETURN_STATION'] == '' :
            continue

        rent_list[int(rent['RENT_STATION'])][int(rent['RETURN_STATION'])]['count'] += 1

    linearlist = []
    for i in range(1, 227, 1) :
        for j in range(1, 227, 1) :
            linearlist.append(rent_list[i][j])

    linearlist.sort(key = itemgetter('count'), reverse = True)

    result = []
    for i in range(0, 10, 1) :
        result.append([\
            station_list[linearlist[i]['rent']]['NAME'],\
            str(linearlist[i]['rent']),\
            station_list[linearlist[i]['return']]['NAME'],\
            str(linearlist[i]['return']),\
            linearlist[i]['count'] ])

    return result

