# Initial Condition Astro
Gerador de posições aleatórias de particulas seguindo perfis de densidade de componentes gal

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
O código no momento somente retorna uma lista de coordenadas x, y, z, aleatórias que seguem o perfil de densidade do disco, do bojo e halo de uma galáxia.
Utilizando ```config.ini```


<img src='https://raw.githubusercontent.com/ViniBilck/IC-Astro/main/IMG/example.png'></img>
