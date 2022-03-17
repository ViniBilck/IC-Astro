# Iniciação Científica
Compilado de códigos utilizados na IC

## Utilizar Gerador

Para rodar o Gerador de coordenadas, rode no terminal.

```powershell
python3 Gerador.py -ho 10 -z 0.3 -m 1 -n 10000 -G  
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
| c | Boolean | Permite o arquivo config.ini |
| s | Boolean | Acessa a função para salvar as coordenadas em HDF5 |
| CG | Boolean | Acessa a função de gerar as coordenadas e o Plot utilizando um arquivo config.ini |
| G | Boolean | Acessa a função de gerar as coordenadas e o Plot |
### Output 
O código no momento somente retorna uma lista de coordenadas x, y, z, aleatórias que seguem  (Ou deveriam seguir) o perfil de densidade do disco de uma galáxia.
Utilizando ```ho = 10, z = 0.3, m = 1, n = 40000```


<img src='https://raw.githubusercontent.com/ViniBilck/IC-Astro/main/IMG/example.png'></img>
