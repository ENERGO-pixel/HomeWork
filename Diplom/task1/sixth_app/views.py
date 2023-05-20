import csv
import datetime
import json
from .models import GameModel
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
import os.path

def upload_data(request):
    with open('vgsales.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            try:
             _, created = GameModel.objects.get_or_create(
                                                    platform=row[2],
                                                    name=row[1],
                                                    year=datetime.date(int(row[3]), 1, 1),
                                                    genre=row[4], publisher=row[5], na_sales=row[6],
                                                    eu_sales=row[7], jp_sales=row[8],
                                                    other_sales=row[9], global_sales=row[10], )

            except:
                    pass
        return HttpResponse("Done!")
# with open('test.json') as f:
#     reader = json.load(f)
#     for row in reader:
#         try:
#             _, created = JSon.objects.get_or_create(
#
#                 MatchNumber=row['MatchNumber'],
#                 RoundNumber=row['RoundNumber'],
#                 DateUtc=row['DateUtc'],
#                 Location=row['Location'],
#                 HomeTeam=row['HomeTeam'],
#                 AwayTeam=row['AwayTeam'],
#                 Group=row['Group'],
#                 HomeTeamScore=row['HomeTeamScore'],
#                 AwayTeamScore=row['AwayTeamScore'],
#
#             )
#             path = os.path.join('sixth_app', 'testtext')
#             file = open(path, 'w')
#             for row in JSon.objects.all():
#                 print(row)
#                 file.write(f'\nMatchNumber - {row.MatchNumber}\
#                                         \nRoundNumber-{row.RoundNumber}\
#                                         \nDateUtc - {row.DateUtc}\
#                                         \nLocation - {row.Location}\
#                                         \nHomeTeam - {row.HomeTeam}\
#                                         \nAwayTeam - {row.AwayTeam}\
#                                         \nGroup - {row.Group}\
#                                         \nHomeTeamScore - {row.HomeTeamScore}\
#                                         \nAwayTeamScore - {row.AwayTeamScore}\
#                                         \n***')
