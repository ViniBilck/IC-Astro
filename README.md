# Iniciação Científica
Compilado de códigos utilizados na IC, para aprender como gerar galáxias para utilizar nas simulações com Gadget-4

# Utilizar Gerador

Para rodar o Gerador de coordenadas, rode no terminal.

```powershell
python3 Gerador.py -h_D 1 -z_D 2 -m_D 1 -n_D 10000 -G  
```
Onde temos que:

|  Prefixo | Type | Comentário |
| --- | --- | --- | 
| h_D | Float | Comprimento da escala exponencial do disco |
| z_D | Float | Espessura da escala vertical do disco |
| m_D | Float | Massa total do disco |
| n_D | Int | Número de particulas geradas |

### Output 
O código no momento somente retorna uma lista de coordenadas x, y, z, aleatórias que seguem  (Ou deveriam seguir) o perfil de densidade do disco de uma galáxia.
