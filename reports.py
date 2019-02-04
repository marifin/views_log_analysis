
import psycopg2

DBNAME = "news"

q_pop_article = ("1. What are the most popular three articles of all time?")

pop_article = (
    """select title, count(*) as viewed
        from articles join log
        on slug = substring(log.path from 10)
        group by title
        order by viewed desc
        limit 3;
    """)

q_pop_author = ("2. Who are the most popular article authors of all time?")

pop_author = (
    """select name, count(*) as total from articles
        join log
        on slug = substring(log.path from 10)
        join authors
        on authors.id = articles.author
        group by authors.name
        order by total desc;
    """)

q_most_errors_day = ("3. On which days did more than 1% of requests "
    "lead to errors?")

most_errors_day = (

    """With allstatus as (
         select time::date as day, count(*) as total
         from log group by day order by day),
         onepercent as (select day, total*0.01 as oneperc
         from allstatus group by day, total order by day),
         errors as (select time::date as day, count(*) as errorperday
         from log
         where status = '404 NOT FOUND' group by day order by day),
         final as (select onepercent.day as finalday,
         errors.errorperday::float as finalerror
         from errors, onepercent
         where onepercent.day = errors.day and errorperday > oneperc
         group by onepercent.day, errors.errorperday order by onepercent.day)
         select to_char(final.finalday, 'FMMonth DD, YYYY'),
         round(cast((final.finalerror/allstatus.total)*100 as numeric), 1)
         from allstatus, final where final.finalday = allstatus.day;
    """)


def run_query(query):

    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()
    conn.close()


def print_result(question, query_result):

    print(question)
    if question == q_pop_article:
        for array in query_result:
            print('   "{}"  -  {} views'.format(array[0], array[1]))

    if question == q_pop_author:
        for array in query_result:
            print('   {}  -  {} views'.format(array[0], array[1]))

    if question == q_most_errors_day:
        for array in query_result:
            print('   {}  -  {}% errors'.format(array[0], array[1]))

    print("\n\n")

query_result = run_query(pop_article)
print_result(q_pop_article, query_result)

query_result = run_query(pop_author)
print_result(q_pop_author, query_result)

query_result = run_query(most_errors_day)
print_result(q_most_errors_day, query_result)
