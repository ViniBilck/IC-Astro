# Iniciação Científica
Compilado de códigos utilizados na IC

## Utilizar Gerador

Para rodar o Gerador de coordenadas, rode no terminal.

```powershell
python3 Gerador.py -ho 1 -z 2 -m 1 -n 10000 -G  
```
ou

```powershell
python3 Gerador.py -c config.ini -CG  
```
Onde temos que:

|  Prefixo | Type | Comentário |
| --- | --- | --- | 
| ho | Float | Comprimento da escala exponencial do disco |
| z | Float | Espessura da escala vertical do disco |
| m | Float | Massa total do disco |
| n | Int | Número de particulas geradas |
| G | Boolean | Acessa a função de gerar as coordenadas e o Plot |
### Output 
O código no momento somente retorna uma lista de coordenadas x, y, z, aleatórias que seguem  (Ou deveriam seguir) o perfil de densidade do disco de uma galáxia.
Utilizando h0 = 10, z = 0.3, m = 1, n = 40000


<img src='https://github.com/ViniBilck/IC-Astro/blob/main/IMG/Example.png'></img>
