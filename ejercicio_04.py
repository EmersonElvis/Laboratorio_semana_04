'''Diseñe un programa que lea un vector y calcule si hay
un número que sea igual a la suma de los demás elementos
del vector.'''

vector = [80, 30, 50, 70, 100, 60, 40]

def suma_vector(a):
    nueva=[]
    for elemento in a:
        suma = elemento
        for i in range(len(a)):
            for j in range(len(a)):
                if i == j:
                    continue    
                if suma==a[i]+a[j]:
                    nueva_l=[]
                    nueva_l.append(a[i])
                    nueva_l.append(a[j])
                    nueva_l.append(suma)
                    nueva.append(nueva_l)
    for ele in nueva:
        if ele==ele:
            nueva.remove(ele)
    return  nueva

print(vector)
res=suma_vector(vector)
print(res)
