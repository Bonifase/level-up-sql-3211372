from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.conf import settings

import sqlite3
import json

def row_to_dict(cursor: sqlite3.Cursor, row: sqlite3.Row) -> dict:
    data = {}
    for idx, col in enumerate(cursor.description):
        data[col[0]] = row[idx]
    return data

def execute_sql(db, query):
    connection = sqlite3.connect(db)
    connection.row_factory = row_to_dict
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        result = json.dumps(result)
        cursor.close()

    except sqlite3.OperationalError as error:
        print(error)
        cursor.close()
        return error

    return result


SOLUTIONS = {
    'Check Availability': '01_restaurant/solutions/01_01_invitations_so.sql',
    'Anniversary Invitation': '02_library/solutions/02_02_anniversary_invitation_so.sql',
}

# Create your views here.
@api_view(['GET', 'POST'])
def restaurant_view(request):
    query_type = request.data.get('query', 'Check Availability')
    correct_query = request.data.get('user_query',None)
    result = None
    path = settings.BASE_DIR / SOLUTIONS.get(query_type)

    # with open(path, 'r') as f:
    #     correct_query = f.read()
    print(correct_query)
    if correct_query:
        db = settings.BASE_DIR / '01_restaurant/restaurant.db'
        result = execute_sql(db, correct_query)

    return Response(result)

