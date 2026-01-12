from database.DB_connect import DBConnect
from model.team import Team

class DAO:
    @staticmethod
    def get_squadre_anno(year):
        conn = DBConnect.get_connection()

        result = []         # Lista di oggetti Team filtrati per anno

        cursor = conn.cursor(dictionary=True)
        query = """ select s.team_id as id, s.team_code as code, name, sum(salary) as salary
                    from salary s, team t 
                    where t.id = s.team_id and s.year = %s
                    group by s.team_id """

        cursor.execute(query,(year,))

        for row in cursor:
            team = Team(id = row['id'],
                        code = row['code'],
                        name = row['name'],
                        salary = row['salary'])
            result.append(team)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_years():
        conn = DBConnect.get_connection()

        result = []  # Lista di anni

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct year
                    from salary"""

        cursor.execute(query, )

        for row in cursor:
            result.append(row['year'])

        cursor.close()
        conn.close()
        return result