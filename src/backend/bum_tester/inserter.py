#! python3
from models import Answer, Question

file = open("../../assets/answers.txt", "r").read()
for i in file.split("\n"):
    a = i.split('|', maxsplit=1)
    q = Answer(document_id=int(a[0][:-1]), answer=a[1])
    q.save()