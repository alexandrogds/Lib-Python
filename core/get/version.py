
"""
"""

def function(*args, **wargs):
  """wargs[project, key]; issues implementeds are labeled confirmed
  version=retirado da tag do git que é no padrão 1.0 2.0 3.0 ou 1.0.0 2.0.0 3.0.0 o que importa é o primeiro digito, todos os outros digitos sao zerados
  quantidade de arquivos
  quantidade de classes
  quantidade de funções
  quantidade de issues confirmados, note que difere dos issues implementados mas devem envolver esses
  quantidade de linhas de codigo=esse falta fazer, deve ser o antipenultimo
  
  precisa-se definir um versionamento para projetos npm que aceitam exatamente somente 3 no formato 0.0.0
  """
  from core import map_wargs
  map_wargs(**wargs)
  from pathlib import Path
  project = Path(project).resolve()
  from core import tag
  tag = tag(project)
  if tag.find('fatal') == 0:
    tag = 1
  else:
    tag = tag.strip()
  a = int(a.split('.')[0]) + 1
  from core import count_files_recursive as count
  b = count(project)
  from core import count_keys_in_files_recursive as count
  c = count(path=project, key='class')
  d = count(path=project, key='def')
  from core import count_issues_implemented as count
  e = count(path=project, mode=count.COMMIT_EQUALS_ISSUES, issues='confirmed')
  return f'{a}.{b}.{c}.{d}.{e}'
