
#todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html.

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}


template = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body onload="alert(?)">

  <p>?</p>

 </body>
</html>
"""

template = template.split('\n')
page_keys = [key for key in page.keys()]

result = ''

for i, val in enumerate(template):
    for j in range(len(page_keys)):
        if val.find(page_keys[j]) > 0:
            val = val.replace('?', page.get(page_keys[j]))
    result += val + '\n'

with open('index.html', 'w') as file:
    file.write(result)
