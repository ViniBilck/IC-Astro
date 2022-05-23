# Iniciação Científica
Compilado de códigos utilizados na IC

## Utilizar Gerador

Para rodar o Gerador de coordenadas, rode no terminal.

```powershell
python3 -c confi.ini -s
```

Onde temos que:

|  Prefixo | Type | Comentário |
| --- | --- | --- | 
| c | Boolean | Permite o arquivo config.ini |
| s | Boolean | Acessa a função para salvar o arquivo de condição inicial em HDF5 |

### Output 
O código no momento somente retorna uma lista de coordenadas x, y, z, aleatórias que seguem  (Ou deveriam seguir) o perfil de densidade do disco de uma galáxia.
Utilizando ```ho = 10, z = 0.3, m = 1, n = 40000```


<img src='https://raw.githubusercontent.com/ViniBilck/IC-Astro/main/IMG/example.png'></img>
