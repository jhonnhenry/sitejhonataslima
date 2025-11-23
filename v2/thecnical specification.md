# PROJETO: Landing Page Pessoal - Jhonatas Lima (JHL Software)
**Arquivo Mestre de Especificação (TDD + Conteúdo)**

> **INSTRUÇÃO PARA A IA (Claude Code/Cursor):**
> Você atuará como um **Senior Frontend Developer & UI Designer**.
> Sua tarefa é gerar um arquivo único `index.html` contendo todo o CSS (Tailwind via CDN), JavaScript e HTML necessários.
> O design deve ser **pixel-perfect**, responsivo e seguir estritamente o "Design System" baseado na logo da marca descrito abaixo.

---

## 1. DESIGN SYSTEM & IDENTIDADE VISUAL

### 1.1. Paleta de Cores (Baseada na Logo JHL)
A logo possui um fundo "Slate Blue" e texto "Cream". Vamos expandir isso para um **Dark Mode Corporativo**.

* **Background Principal (Deep Navy):** `#0f172a` (Slate 900) - Para o fundo da página.
* **Surface/Cards (Lighter Slate):** `#1e293b` (Slate 800) - Para cartões de projetos e seções.
* **Primary Brand Color (Slate Blue):** `#334155` (Slate 700) a `#475569` (Slate 600) - Para fundos de destaque sutil.
* **Accent/Highlight (Cream/Off-White):** `#fefce8` (Yellow 50) ou `#f1f5f9` (Slate 100) - Usar para textos de destaque, bordas finas e botões primários. **Esta é a cor de contraste da logo.**
* **Interactive Action (Soft Blue):** `#38bdf8` (Sky 400) - Apenas para hover de links e ícones, para garantir acessibilidade sobre o fundo escuro.

### 1.2. Tipografia
* **Fonte Principal:** 'Inter' ou 'Outfit' (Google Fonts).
* **Pesos:** Light (300) para corpo, Semi-Bold (600) para títulos, Bold (700) para números.

### 1.3. Estética & Efeitos (CSS Moderno)
* **Glassmorphism:** No Header e em alguns cards (`bg-slate-900/80 backdrop-blur-md`).
* **Bento Grid:** Layout em grade assimétrica para a seção de projetos.
* **Glow Effects:** Sombras sutis coloridas atrás da foto de perfil e botões (`shadow-cyan-500/20`).
* **Scroll Reveal:** Elementos devem surgir com `fade-up` suave.

---

## 2. ESTRUTURA TÉCNICA (HTML/Stack)

* **Framework CSS:** Tailwind CSS v3.4 (via Script CDN).
* **Ícones:** Lucide Icons (via Script CDN - `unpkg.com/lucide@latest`).
* **Fontes:** Google Fonts (Importar Inter).
* **Scripts:** Alpine.js (Opcional) ou Vanilla JS puro para interações (Menu Mobile e Scroll Reveal).

---

## 3. CONTEÚDO E ARQUITETURA DE INFORMAÇÃO

### 3.1. Header (Navegação Fixa)
* **Logo (Esquerda):** Usar texto "JHL Software" (estilizado com a fonte, cor Cream) ou placeholder para a imagem da logo.
* **Menu (Direita):** Home, Sobre, Time, Clientes, Projetos.
* **Botão CTA:** "Fale Comigo" (Estilo: Outline Cream).

### 3.2. Hero Section (Dobra Principal)
* **Layout:** Centralizado ou 2 Colunas (Texto Esq / Imagem Dir).
* **Elemento Visual:** Foto do Jhonatas com um círculo de fundo sutil (cor Slate Blue).
* **Conteúdo:**
    * *Badge:* "Tech Lead & Solutions Architect"
    * *H1:* **Desenvolvedor | Tech Lead | Fundador da JHL Software**
    * *Subtítulo:* "Com 20 anos de experiência em T.I., sou especialista em transformar desafios de negócio em software robusto. Focado no ecossistema Microsoft (C#, .NET, Azure e SQL Server), atuo de ponta a ponta: da arquitetura da solução à entrega final."
    * *CTA Button:* "Ver Portfólio" (Fundo Cream, Texto Dark Blue).

### 3.3. Seção "Sobre Mim" (Bio & Formação)
* **Design:** Layout lado a lado. Foto profissional vs Texto.
* **Texto:**
    "Olá, sou Jhonatas Lima.
    Minha trajetória na tecnologia é pautada pela busca constante por excelência e qualificação. Tudo começou com uma base sólida: em 2005 formei-me **Técnico em Informática pelo IFTO** e, em 2013, consolidei meu conhecimento como **Bacharel em Sistemas de Informação pela Faculdade Católica do Tocantins**.
    Hoje, com duas décadas de carreira, aplico essa expertise acadêmica e prática como **Tech Lead e Fundador da JHL Software**. Meu foco é desenhar a arquitetura ideal no ecossistema Microsoft — com ênfase em soluções na nuvem com Azure — para garantir que a tecnologia gere crescimento real para meus clientes em todo o Brasil.
    Acredito que a tecnologia deve servir às pessoas. Esse compromisso com a qualidade que levo para os códigos, também dedico à minha vida pessoal, onde construí minha família. Para mim, o sucesso é o equilíbrio entre uma solução técnica impecável e um lar feliz."

### 3.4. Seção "Nosso Time" (Equipe)
* **Conceito:** "Quem faz acontecer".
* **Texto Intro:** "Acredito que grandes projetos não são construídos apenas com códigos complexos, mas com **parcerias sólidas**. Na JHL Software, a tecnologia é o meio, mas as pessoas são o motor. Nossa cultura é pautada na colaboração intensa e na troca de conhecimento."
* **Cards:** 3 Cards alinhados horizontalmente. Design limpo, fundo Slate-800, foto circular, nome em destaque (Cor Cream) e ícone do GitHub.
    1.  **Hugo Capucho** - Desenvolvedor Full Stack - [GitHub](https://github.com/HCapucho)
    2.  **Fernando Bolani** - Desenvolvedor Full Stack - [GitHub](https://github.com/fbolani)
    3.  **Guilherme Rudio** - Desenvolvedor Full Stack - [GitHub](https://github.com/Rudio1)

### 3.5. Seção "Clientes" (Prova Social)
* **Efeito:** "Infinite Marquee" (Carrossel automático contínuo).
* **Estilo:** Logos em tom monocromático (Branco com baixa opacidade) que ficam coloridas ou 100% brancas ao passar o mouse.
* **Lista:** AFS Locações, Claro, Consul, Brastemp, Governo do Tocantins, Defensoria Pública do Tocantins, Tribunal de Justiça do Tocantins.
* **Intro:** "A credibilidade se constrói com resultados consistentes. Tive a honra de colaborar com grandes marcas nacionais e instituições públicas."

### 3.6. Seção "Portfólio em Destaque" (Projetos - Bento Grid)
* **Layout:** Grid CSS Complexo (Bento Box). Projetos maiores ocupam 2 colunas.
* **Estilo dos Cards:** Fundo Slate-800, Borda fina Slate-700. Hover: Borda Cream/White e leve "Lift".
* **Conteúdo dos Cards (Resumido para UI):**

    * **Card 1 (Destaque - Governo TO):**
        * *Tag:* Alta Escala / Oracle
        * *Título:* Gestão de Folha de Pagamento (55k Vidas)
        * *Desc:* Migração crítica de legado (Adabas) para Oracle DB e implantação do sistema Ergon. Superando desafios onde equipes anteriores falharam.
        * *Link:* [Ver Notícia](https://www.to.gov.br/secom/novo-sistema-para-folha-de-pagamento-sera-implantado/5mwuv74td6rz)

    * **Card 2 (Destaque - AFS Locações):**
        * *Tag:* ERP / .NET
        * *Título:* ERP Corporativo End-to-End
        * *Desc:* Sistema completo construído do zero: Financeiro, Contábil, CRM, Gestão de Pneus e Suprimentos.

    * **Card 3 (DPE Tocantins):**
        * *Tag:* SOAP / Integração
        * *Título:* Automação Jurídica e-Proc
        * *Desc:* Algoritmo de distribuição automática de processos e endpoints SOAP para integração MNI 2.2.2.

    * **Card 4 (Whirlpool - Consul/Brastemp):**
        * *Tag:* Big Data / B2B
        * *Título:* Sistema +Top (Incentivo de Vendas)
        * *Desc:* Processamento de vendas de grandes varejistas (Havan, Bemol) para pontuação e resgate de prêmios.

    * **Card 5 (TJTO - DorinaPDF):**
        * *Tag:* Open Source / Acessibilidade
        * *Título:* Projeto DorinaPDF
        * *Desc:* Solução multiplataforma para validação de acessibilidade em documentos jurídicos para deficientes visuais.
        * *Link:* [Acessar Projeto](https://dorinapdf.azurewebsites.net/)

    * **Card 6 (Claro):**
        * *Tag:* High Traffic / Web
        * *Título:* Portal Promocional Gamificado
        * *Desc:* Sistema de "Roleta Premiada" para campanha de Dia das Mães com alto volume de acessos simultâneos.

### 3.7. Footer
* Texto: "Jhonatas Lima © 2025 - JHL Software. Construindo o futuro com .NET e Azure."
* Links Sociais: Ícones para GitHub, LinkedIn, Instagram.

---

## 4. INSTRUÇÕES FINAIS DE CODIFICAÇÃO

1.  **Código Único:** Gere tudo dentro de um arquivo HTML. Use `<style>` para customizações CSS extras que o Tailwind não cobrir (ex: animações de keyframes) e `<script>` no final do body.
2.  **Mobile First:** Garanta que o Grid de projetos se transforme em uma coluna única em telas pequenas.
3.  **Imagens:** Utilize placeholders do *Unsplash Source* ou *Placehold.co* com temas de tecnologia ("code", "server", "team", "office") para ilustrar onde as imagens reais entrarão. Para a logo, use um retângulo SVG simples com o texto "JHL" se não puder carregar imagem externa.
4.  **Paleta:** Garanta que o contraste entre o texto `Slate-400` e o fundo `Slate-900` seja legível. Use a cor "Cream" (`#fefce8`) para títulos importantes para mimetizar a identidade da marca.