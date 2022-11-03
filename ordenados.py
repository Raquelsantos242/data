#etapa 4
#atexe3
import psutil

#paso 1 - cria a lista de processos
l = []
for p in psutil.process_iter():
    p = p.as_dict()
    
    d = {"pid": p['pid'], "nome": p['name'], "memoria": p['memoria_info'][0] // 1024 ** 2}
    l.append(d)
    
#passo 2- ordena a lista pelo perc_cpu decrescente
def comp_processo(p):
    return p['memoria']

l.sort(key=comp, processp, reverse=True)