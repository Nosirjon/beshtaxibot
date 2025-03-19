from django.shortcuts import render
from django.http import HttpResponse

def main(requeests):
    return render(requeests, 'main/index.html')