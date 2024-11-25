from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReportCreateForm, ReportEditForm  # Supondo que você tenha esses forms criados
from .models import Report
from django.contrib import messages


def home_view(request):
    reports = Report.objects.all()

    categoria = request.GET.get('categoria', '')
    if categoria:
        reports = reports.filter(categoria=categoria)

    prioridade = request.GET.get('prioridade', '')
    if prioridade:
        reports = reports.filter(prioridade=prioridade)

    cidade = request.GET.get('cidade', '')
    if cidade:
        reports = reports.filter(cidade=cidade)

    bairro = request.GET.get('bairro', '')
    if bairro:
        reports = reports.filter(bairro=bairro)

    cidades = Report.objects.values_list('cidade', flat=True).distinct()
    bairros = Report.objects.values_list('bairro', flat=True).distinct()

    context = {
        'reports': reports,
        'cidades': cidades,
        'bairros': bairros,
    }

    return render(request, 'reports/home.html', context)


def report_create_view(request):
    form = ReportCreateForm()  

    if request.method == 'POST':
        form = ReportCreateForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.autor = request.user  
            report.save()
            messages.success(request, 'Relato criado com sucesso!')
            return redirect('home')
    
    return render(request, 'reports/report_create.html', {'form': form})


def report_delete_view(request, pk):
    report = get_object_or_404(Report, id=pk)

    if request.method == 'POST':
        report.delete()
        messages.success(request, 'Relato deletado com sucesso!')
        return redirect('home')
        
    return render(request, 'reports/report_delete.html', {'report': report})


def report_edit_view(request, pk):
    report = get_object_or_404(Report, id=pk)  
    form = ReportEditForm(instance=report)

    if request.method == 'POST':
        form = ReportEditForm(request.POST, request.FILES, instance=report) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Relato atualizado com sucesso!')
            return redirect('home')
    
    context = {
        'report': report,
        'form': form,
    }
    return render(request, 'reports/report_edit.html', context)
