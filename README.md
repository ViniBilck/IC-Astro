# Iniciação Científica
Compilado de códigos utilizados na IC

## Utilizar Gerador

Para rodar o Gerador de coordenadas, rode no terminal.

```powershell
python3 Gerador.py -h 1 -z 2 -m 1 -n 10000 -G  
```
Onde temos que:

|  Prefixo | Type | Comentário |
| --- | --- | --- | 
| h | Float | Comprimento da escala exponencial do disco |
| z | Float | Espessura da escala vertical do disco |
| m | Float | Massa total do disco |
| n | Int | Número de particulas geradas |
| G | Boolean | Acessa a função de gerar as coordenadas e o Plot |
### Output 
O código no momento somente retorna uma lista de coordenadas x, y, z, aleatórias que seguem  (Ou deveriam seguir) o perfil de densidade do disco de uma galáxia.
