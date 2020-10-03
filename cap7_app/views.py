from django.shortcuts import render, HttpResponse, redirect
import psycopg2.extras


# Create your views here.


def home(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")

    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute('SELECT * FROM nota;')

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    params = {'notas': result}

    return render(request, 'inicio.html', params)


def insertar(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")

    prioridad = request.POST['prioridad']
    titulo = request.POST['subject']
    contenido = request.POST['msg']

    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO nota VALUES ('{prioridad}', '{titulo}', '{contenido}')")

    conn.commit()

    cursor.close()
    conn.close()

    return redirect('inicio')


def filtrar(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")

    prioridad = request.GET.get('get_prioridad', default=None)

    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM Nota;")

    result = cursor.fetchall()

    conn.commit()

    cursor.close()
    conn.close()

    params = {'notas': result}

    return render(request, 'inicio.html', params)


def select(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM nota")

    html = '<html>'

    columns = [col[0] for col in cursor.description]

    for column in columns:
        html += str(column) + '|'

    html += '<br>'

    for empleado in cursor.fetchall():
        for columna in empleado:
            html += str(columna) + '|'
        html += '<br>'

    html += '</html>'

    cursor.close()
    conn.close()

    return HttpResponse(html)


def delete(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")

    cursor = conn.cursor()
    cursor.execute("DELETE FROM nota")

    conn.commit()

    cursor.close()
    conn.close()

    return HttpResponse('Borrado')
