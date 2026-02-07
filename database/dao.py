from database.DB_connect import DBConnect
from model.team import Team

class DAO:
    @staticmethod
    def get_anni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct year
                    from team t
                    where year >= 1980 """

        cursor.execute(query)

        for row in cursor:
            anno = row["year"]
            result.append(anno)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_squadre_stipendi(anno):
        conn = DBConnect.get_connection()

        result = {}

        cursor = conn.cursor(dictionary=True)
        query = """ select t.id as id, t.team_code as team_code, t.name as name, sum(salary) as salary
                    from team t, salary s
                    where s.team_id = t.id and t.year = %s
                    group by t.id
                    order by sum(salary) DESC """

        cursor.execute(query,(anno,))

        for row in cursor:
            team_id = row["id"]
            code = row["team_code"]
            name = row["name"]
            salary = row["salary"]
            team = Team(team_id, code, name, salary)
            result[team_id] = team

        cursor.close()
        conn.close()
        return result