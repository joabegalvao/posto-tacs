# Posto Tacs | Landing page

Página única, estática, em HTML, CSS e JavaScript puro. Não há etapa de build
nem dependências de execução: basta servir a pasta.

## Como visualizar

```bash
# na raiz do projeto
python3 -m http.server 4177
# abra http://localhost:4177
```

Qualquer servidor estático funciona (Nginx, Apache, Netlify, Vercel, Hostinger).
Publique `index.html` e a pasta `assets/`. A pasta `tools/` não precisa ir para
o servidor.

### Materiais de origem

Os arquivos enviados pelo cliente ficam reunidos na pasta
`materiais-de-origem/`, que não faz parte do repositório: ela existe só na
pasta local do projeto e é ignorada pelo git. As imagens que o site usa já
estão prontas em `assets/img`.

```
materiais-de-origem/
  logo/          Posto Tacs logo.png
  fotos/         onze capturas de tela do Instagram do posto
  avaliacoes/    fotos de perfil de quem avaliou
  dados.txt      recebido vazio
```

Só é preciso ter os originais para rodar `tools/optimize-images.py`, ou seja,
para trocar ou reprocessar uma foto.

| Arquivo de origem | Conteúdo | Usado em |
| --- | --- | --- |
| `logo/Posto Tacs logo.png` | Símbolo "P" branco sobre azul, 400 x 400 px | cabeçalho, rodapé, ícones e imagem de compartilhamento |
| `fotos/Screenshot 2026-09-29 102027.png` | Posto à noite | hero e imagem de compartilhamento |
| `fotos/Screenshot 2026-09-29 101826.png` | Arte "Aqui, cada gota vale a pena", com a bomba | combustível (só a bomba, recortada) |
| `fotos/Screenshot 2026-09-29 101849.png` | Fachada da Tacs Go com carro verde | conveniência |
| `fotos/Screenshot 2026-09-29 102108.png` | Área coberta com mesas | conveniência |
| `fotos/Screenshot 2026-09-29 102054.png` | Interior da conveniência | conveniência |
| `fotos/Screenshot 2026-09-29 102040.png` | Área coberta, outro ângulo | não usada |
| `fotos/Screenshot 2026-09-29 101743.png` | Arte "Aqui vale a parada" | só o texto |
| `fotos/Screenshot 2026-09-29 101516.png` | Arte "Cerveja gelada" | só o texto |
| `fotos/Screenshot 2026-09-29 101527.png` | Arte "Café e pausa" | só o texto |
| `fotos/Screenshot 2026-09-29 101537.png` | Arte "Troca de óleo" | só o texto |
| `fotos/Screenshot 2026-09-29 101547.png` | Arte "Qualidade comprovada" | só o texto |
| `avaliacoes/Thiago_Pacheco.png`, `Jessica_Cristina.png`, `Marcos Gonçalves.png` | Fotos de perfil, 72 x 72 px | avaliações |

## Repositório

| Item | Valor |
| --- | --- |
| Endereço | `git@github.com:joabegalvao/posto-tacs.git` |
| Página | https://github.com/joabegalvao/posto-tacs |
| Visibilidade | pública (conferida em 29/09/2026) |
| Branch | `main` |

O repositório guarda só o que o site precisa para funcionar e ser mantido:
`index.html`, `assets/`, `tools/`, `README.md` e `.gitignore`.

```bash
git clone git@github.com:joabegalvao/posto-tacs.git
```

Um clone novo abre e publica o site normalmente. Só não roda o script de
imagens, que depende da pasta `materiais-de-origem/`.

## Dados do cliente

Recebidos em 29/09/2026.

### Informados no briefing

| Dado | Valor |
| --- | --- |
| Nome | Posto Tacs |
| Segmento | Posto de combustível |
| Produtos e serviços | Combustível, troca de óleo e serviços, bebidas, café, pães |
| Público | Qualquer pessoa |
| WhatsApp | 044991144534, publicado como (44) 99114-4534 |
| Instagram | https://www.instagram.com/postotacs |

### Lidos nas artes do próprio posto

Estes dados não vieram no texto do briefing. Foram lidos nas artes do
Instagram do posto, enviadas como material.

| Dado | Valor | Onde aparece |
| --- | --- | --- |
| Endereço | Praça José de Bonifácio, 44, Maringá, PR | artes "No Posto Tacs tem..." e bandeira na pista |
| Horário | Aberto 24hs todos os dias | artes "No Posto Tacs tem..." |
| Troca de óleo | "Agende seu atendimento" | arte "Troca de óleo" |
| Combustível | "Combustível testado", "Motor protegido", "Qualidade comprovada" | artes da bomba |
| Frases da marca | "Aqui vale a parada", "Aqui, cada gota vale a pena" | artes |
| Conveniência | Tacs Go Conveniência | fachada |
| Grupo | "Empresa do grupo: Tacs Company" | rodapé de uma arte |

### Avaliações como foram recebidas

Texto original, antes de qualquer correção.

- **Thiago Pacheco:** Melhor lugar que já abasteci atendimento excepcional
  combustível muito bom nunca tive problemas ótimo preço excelente localização
  muito obrigado por entregar em um serviço com tanta excelência assim parabéns
- **Jessica Cristina:** Hoje passei neste posto de gasolina e tive uma
  experiência excelente! Fui muito bem atendida, com muita educação, atenção e
  agilidade.
- **Marcos Gonçalves:** Atendimento excelente no período da madrugada. Fui
  muito bem atendido pelo Micael e pelo frentista Ederson, que foram educados,
  prestativos e atenciosos.

## Estratégia

| Definição | Decisão |
| --- | --- |
| Proposta de valor | Uma parada que resolve tudo: combustível testado, troca de óleo e conveniência, a qualquer hora |
| Principal objeção | "Posso confiar no combustível? E vou ser bem atendido, mesmo de madrugada?" |
| Conversão prioritária | Conversa no WhatsApp, em especial para agendar a troca de óleo |
| Ação secundária | Abrir a rota até o posto |
| Ação de apoio | Seguir o Instagram @postotacs |

## Seções da página

| Ordem | Seção | Âncora | Conteúdo |
| --- | --- | --- | --- |
| 1 | Cabeçalho | | Símbolo, nome, navegação e CTA de WhatsApp. Fixo no topo |
| 2 | Hero | `#inicio` | "Aqui vale a parada", dois botões, foto do posto à noite e três fatos |
| 3 | Combustível | `#combustivel` | Quatro pontos e uma frase de cliente |
| 4 | Troca de óleo | `#troca-de-oleo` | Três passos e botão de agendamento |
| 5 | Conveniência | `#conveniencia` | Três fotos da Tacs Go e o que tem lá |
| 6 | Avaliações | `#avaliacoes` | Três depoimentos de clientes, um em destaque |
| 7 | Onde fica | `#onde-fica` | Endereço, horário, WhatsApp, Instagram e mapa |
| 8 | Chamada final | | WhatsApp e rota |
| 9 | Rodapé | | Endereço, atendimento e redes sociais |

Componente de apoio: botão flutuante de WhatsApp, no canto inferior direito,
em todas as telas.

## Estrutura de arquivos

```
index.html                 conteúdo e SEO
assets/css/styles.css      estilos (tokens de cor e tipografia no topo)
assets/js/main.js          menu e revelação na rolagem
assets/img/                imagens otimizadas (geradas pelo script)
assets/fonts/              Barlow e Barlow Condensed (arquivos locais)
tools/optimize-images.py   gera assets/img a partir dos originais
materiais-de-origem/       arquivos do cliente (só na pasta local, fora do git)
```

## Como atualizar o conteúdo

| O que mudar | Onde |
| --- | --- |
| Textos e endereço | `index.html` (seções comentadas) |
| Número e mensagem do WhatsApp | `index.html`: procure por `wa.me/` (8 ocorrências). O texto vem depois de `?text=`, com espaços escritos como `%20` e acentos codificados |
| Endereço do mapa | `index.html`: procure por `google.com/maps` (6 ocorrências, uma delas no `<iframe>`) |
| Horário | `index.html`: hero, seção "Onde fica", rodapé e bloco JSON-LD no `<head>` |
| Cores e fontes | `assets/css/styles.css`, bloco `:root` |
| Fotos | substitua o original, ajuste a lista `PHOTOS` em `tools/optimize-images.py` e rode o script |
| Foto com texto ou marca aplicada | acrescente o arquivo à lista `CROPS` do script (esquerda, topo, direita, base, em pixels) e rode o script |
| Avaliações | `index.html`, seção "AVALIAÇÕES". Fotos de perfil: lista `AVATARS` do script |

Há duas mensagens de WhatsApp:

| Onde | Mensagem |
| --- | --- |
| Cabeçalho, hero, "Onde fica", chamada final, rodapé e botão flutuante | Olá! Vi o site do Posto Tacs e quero mais informações. |
| Seção "Troca de óleo" e rodapé | Olá! Vi o site do Posto Tacs e quero agendar uma troca de óleo. |

Para gerar as imagens (requer Pillow e a pasta `materiais-de-origem/`):

```bash
python3 tools/optimize-images.py
```

Se a proporção de uma foto mudar, atualize `width` e `height` da tag `<img>`
correspondente no `index.html`, para não haver salto de layout.

### Cache do navegador

Os arquivos de estilo e script são chamados com versão: `styles.css?v=1` e
`main.js?v=1`. Ao alterar um deles, aumente o número no `index.html` para que
os visitantes recebam a versão nova.

## Identidade visual

| Token | Cor | Origem |
| --- | --- | --- |
| `--blue` | `#003E80` | fundo do logo |
| `--white` | `#FFFFFF` | o "P" do logo |
| `--blue-500`, `--blue-600` | `#1560D4`, `#0F4FB3` | azul da cobertura iluminada, nas fotos: botões |
| `--sky`, `--sky-200` | `#5AA2FF`, `#A9CEFF` | azul claro das luzes: destaques sobre fundo escuro |
| `--night`, `--night-800`, `--night-line` | `#060D1A`, `#0C1628`, `#1D2B44` | céu das fotos noturnas: fundos escuros e linhas |
| `--mist`, `--line` | `#F1F4F8`, `#D9E0E9` | fundos claros e linhas |
| `--ink`, `--ink-soft`, `--night-soft` | `#0B1524`, `#4B5869`, `#A7B4C6` | textos |
| `--whatsapp` | `#25D366` | verde oficial do WhatsApp, usado só no botão flutuante |

Tipografia: Barlow Condensed (títulos em caixa alta, com itálico nos destaques)
e Barlow (textos). A família Barlow nasceu inspirada nas placas de estrada, e
o itálico condensado é parente do letreiro "POSTO TACS" da fachada.

Elementos que vêm da marca e do posto:

- Página escura no topo e no rodapé, como as fotos noturnas do posto, que é
  aberto 24 horas.
- Azul em dois tons: o do logo, mais fechado, e o da cobertura iluminada, mais
  vivo.
- Traço inclinado antes dos rótulos de seção, no mesmo ângulo do corte do "P".
- Filete azul deslocado atrás da foto principal.

### Tratamento do logo

O arquivo recebido traz só o símbolo: o "P" branco sobre um quadrado azul, com
400 x 400 px. Nada foi redesenhado. O script uniformiza o azul do fundo, que
tinha pequenas variações de compressão.

No cabeçalho e no rodapé, o símbolo aparece ao lado do nome "Posto Tacs"
escrito em Barlow Condensed itálico. Esse nome é texto da página, não o
letreiro oficial da marca.

### Tratamento das fotos

As fotos recebidas são capturas de tela, de 626 a 814 px de largura. O script
remove 2 px de cada borda e gera versões menores. Nenhuma foto é ampliada.

Dois recortes retiram textos aplicados sobre as fotos:

- Na arte da bomba, fica só a bomba, sem o cartão de texto e sem a faixa da
  base.
- Na foto da fachada, sai a assinatura do posto aplicada na base.

As quatro artes "No Posto Tacs tem..." não entraram como imagem. Elas usam
fotos genéricas com texto por cima, e a página já apresenta as mesmas
informações em texto.

## Decisões de conteúdo

- Os fatos da página vêm do briefing e das artes do próprio posto, listados
  acima. Não há preços, bandeira de combustível, métricas ou promessas
  inventadas.
- "Marca própria" foi entendida como a marca Posto Tacs e sua conveniência,
  Tacs Go.
- O título do hero, "Aqui vale a parada", e o da seção de combustível, "Cada
  gota vale a pena", são frases do próprio posto.
- "Combustível testado" e "motor protegido" são afirmações do posto. A página
  não explica como o teste é feito, porque isso não foi informado.
- "E serviços": o briefing cita "troca de óleo e serviços" sem dizer quais. A
  página apresenta só a troca de óleo.
- Mesas no salão e na área coberta foram descritas a partir das fotos.
- Bebida alcoólica: a página cita cerveja, como a arte do posto, e acrescenta
  o aviso "Se for dirigir, não beba".
- "O Posto Tacs está aberto agora", na chamada final, vale porque o posto
  funciona 24 horas, todos os dias.
- Avaliações: as palavras são as enviadas pelo cliente. A de Thiago Pacheco
  veio sem pontuação. Foram acrescentados pontos, vírgulas e maiúsculas, e
  retirado um "em" sobrando ("entregar em um serviço" virou "entregar um
  serviço"). As outras duas estão como recebidas.
- A frase em destaque na seção de combustível é um trecho da avaliação de
  Thiago Pacheco.
- A foto de perfil de Marcos Gonçalves traz um selo laranja com estrela, que
  já vem no arquivo recebido.
- Avaliações sem estrelas e sem citação de fonte, porque nota e origem não
  foram informadas.
- O mapa da seção "Onde fica" é um mapa do Google incorporado. Ele só carrega
  quando o visitante chega perto da seção. O Google mostra no mapa a nota e o
  número de avaliações do posto; esses números não foram escritos na página.
- Não há telefone fixo, porque só foi informado o WhatsApp.
- Não há formulário, porque não existe destino de envio definido.
- A foto do hero não tem legenda.
- O ícone do botão flutuante é escuro sobre o verde, e não branco, para manter
  contraste suficiente.

## Testes realizados

Executados em 29/09/2026, em Chromium automatizado (Playwright).

- Revisão visual das capturas de tela: página inteira em 390 e 1440 px.
- Sem rolagem horizontal e com o título do hero em duas linhas nos tamanhos
  320, 360, 390, 600, 768, 900, 1024, 1200, 1440 e 1920 px.
- Sem erros de console e sem imagens quebradas.
- 39 verificações automáticas aprovadas: menu no celular (toque, Esc, toque
  fora, foco), âncoras, botão flutuante de WhatsApp (posição, nome acessível,
  sem cobrir o texto do rodapé), mapa com título e carregamento adiado,
  revelação na rolagem, link de pular para o conteúdo, foco visível, destino
  e atributos de todos os links, mensagens do WhatsApp, hierarquia de títulos
  e atributos das imagens.
- O mapa foi aberto no teste e mostrou o marcador "Posto Tacs" na Praça José
  de Bonifácio, 44, Zona 01.
- Página utilizável sem JavaScript.
- Animações desligadas quando o sistema pede movimento reduzido.
- Contraste AA em todos os textos (mínimo de 5,74:1).
- Carga inicial no celular de 227 KB, medida em tela de densidade 3x, sem
  saltos de layout (CLS 0). Página inteira: 433 KB, sem contar o mapa.
- O mapa do Google soma cerca de 1,8 MB, baixados só quando o visitante chega
  à seção "Onde fica".

Não testado: Safari, Firefox e aparelhos físicos. Dos links externos, foi
conferido apenas o endereço, não o conteúdo de destino. Isso inclui o
WhatsApp: não foi verificado se o número responde.

## Histórico de ajustes

| Ajuste | Arquivos |
| --- | --- |
| Versão inicial da página | todos |

## Créditos e licenças

- Logo, fotos, artes, avaliações e fotos de perfil: fornecidos pelo cliente.
- Barlow e Barlow Condensed: SIL Open Font License 1.1, obtidas do Google Fonts
  e hospedadas localmente.
- Ícones: desenhados para este projeto. Ícone do WhatsApp: Simple Icons (CC0).
- Mapa: Google Maps, incorporado.

## Pendências que dependem do cliente

- Confirmar os dados lidos nas artes: endereço, funcionamento 24 horas todos
  os dias e troca de óleo com agendamento.
- Informar se a troca de óleo também funciona 24 horas ou tem horário próprio.
- Dizer quais são os outros serviços além da troca de óleo.
- Explicar como o combustível é testado, caso se queira detalhar a seção.
- Confirmar que o WhatsApp (44) 99114-4534 atende dúvidas e agendamentos.
- Fotos originais em alta resolução. As atuais são capturas de tela e limitam
  o tamanho das imagens na página.
- Logo completo, com o nome, em vetor (SVG, AI ou PDF). O arquivo recebido traz
  só o símbolo.
- Foto da troca de óleo no próprio posto, se houver.
- Domínio de publicação, para completar `og:image` com URL absoluta e adicionar
  `link rel="canonical"`.
- Origem das avaliações (por exemplo, o link do perfil no Google), caso se
  queira citar a fonte, e autorização dos clientes para uso de nome e foto. A
  foto de perfil de Jessica Cristina mostra a família, com crianças.
- Autorização dos funcionários citados pelo nome na avaliação de Marcos
  Gonçalves.
- Nota no Google: em 29/09/2026 o mapa mostrava nota 4,7 com 175 avaliações.
  Se o cliente confirmar e quiser, esse dado pode entrar na página com link
  para o perfil.
- Fotos de perfil das avaliações têm 72 x 72 px. Ficam nítidas no tamanho usado
  (48 px), mas não podem ser ampliadas.
