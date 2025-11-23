# JHL Software - Landing Page

> Portfólio profissional de Jhonatas Lima - Tech Lead & Solutions Architect

[![Live Demo](https://img.shields.io/badge/demo-live-success)](https://www.jhonataslima.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 📋 Sobre o Projeto

Landing page moderna e responsiva desenvolvida para apresentar o portfólio profissional da JHL Software. O projeto consolida o melhor de duas versões anteriores (v1 e v2) em uma experiência de usuário otimizada, com design moderno e performance aprimorada.

### ✨ Características Principais

- **Design Moderno**: Interface dark com sistema de cores profissional (slate/sky/yellow)
- **Totalmente Responsivo**: Experiência otimizada para mobile, tablet e desktop
- **Performance Otimizada**: Animações suaves com IntersectionObserver API
- **Acessível**: Estrutura semântica e navegação por teclado
- **SEO Friendly**: Meta tags otimizadas e estrutura HTML semântica

## 🚀 Demonstração

Acesse a versão live: [https://www.jhonataslima.com/](https://www.jhonataslima.com/)

## 🎨 Seções

### 1. Header/Navegação
- Logo oficial JHL Software
- Menu desktop com 5 links principais
- Menu mobile full-screen com animação slide-in
- Botão CTA "Fale Comigo"
- Glassmorphism com backdrop blur

### 2. Hero Section
- Badge "Tech Lead & Solutions Architect"
- Título principal com gradiente
- Foto de perfil com efeito grayscale invertido
- Badge flutuante "20+ Anos de Experiência"
- Dois CTAs principais

### 3. Sobre Mim
- Biografia completa
- Ênfase nas formações acadêmicas
- Badges de educação (IFTO 2005 / Católica 2013)
- Foto profissional com efeitos

### 4. Equipe
- Apresentação da filosofia de equipe
- Grid com 3 membros
- Links para LinkedIn e GitHub de cada membro

### 5. Clientes
- Marquee infinito com animação suave
- Cards grandes (280px) com hover effects
- 7 clientes em destaque

### 6. Projetos
- **Bento Grid assimétrico** para layout dinâmico
- Formato **Challenge/Solution** detalhado
- 6 projetos principais:
  - AFS Locações (destaque full-width)
  - Governo do Tocantins
  - DorinaPDF
  - DPE Tocantins
  - Consul & Brastemp
  - Claro

### 7. Footer/Contato
- CTA de contato integrado
- Botão de email direto
- Links para redes sociais
- Copyright e tagline

### 8. Back-to-Top
- Botão flutuante
- Aparece após scroll de 300px
- Smooth scroll para o topo

## 🛠️ Tecnologias Utilizadas

### Frontend
- **HTML5**: Estrutura semântica
- **CSS3**: Animações e efeitos modernos
- **JavaScript (ES6+)**: Vanilla JS, sem frameworks
- **Tailwind CSS v3.4+**: Framework CSS utilitário
- **Lucide Icons**: Biblioteca de ícones moderna
- **Google Fonts (Inter)**: Tipografia profissional

### Features Técnicas
- **IntersectionObserver API**: Scroll reveal performático
- **CSS Grid & Flexbox**: Layout responsivo
- **CSS Custom Properties**: Sistema de cores
- **Keyframe Animations**: Animações suaves
- **Glassmorphism**: Efeitos modernos de blur

## 📦 Estrutura do Projeto

```
sitejhonataslima/
├── index.html              # Arquivo principal (single-page)
├── img/                    # Imagens do site
│   ├── logo JHL Software.png
│   ├── jhon01.png         # Hero photo
│   ├── jhon02.png         # About photo
│   ├── jhon03.png         # Team intro photo
│   ├── clients/           # Logos dos clientes
│   ├── afsLocacoes.png    # Screenshots dos projetos
│   ├── governoTocantins.jpg
│   ├── dorinaPDF.png
│   ├── DPE-TO_01.jpg
│   ├── whirlpool.png
│   ├── claromaes.png
│   ├── hugoCapucho.png    # Team photos
│   ├── fBolani.jpeg
│   └── guilhermeRudio.jpeg
├── v1/                     # Versão anterior 1 (referência)
├── v2/                     # Versão anterior 2 (referência)
└── README.md              # Este arquivo
```

## 🎯 Design System

### Paleta de Cores

```css
/* Backgrounds */
--slate-900: #0f172a;    /* Deep Navy */
--slate-850: #172033;    /* Custom darker slate */
--slate-800: #1e293b;    /* Surface/Cards */

/* Accent Colors */
--yellow-50: #fefce8;    /* Cream (brand accent) */
--sky-400: #38bdf8;      /* Interactive blue */
--slate-700: #334155;    /* Borders */
--slate-400: #94a3b8;    /* Text secondary */
--slate-300: #cbd5e1;    /* Text primary */
```

### Tipografia

- **Família**: Inter (Google Fonts)
- **Pesos**: 300 (Light), 400 (Regular), 600 (Semi-Bold), 700 (Bold)
- **Tamanhos**:
  - H1: 3xl-6xl (clamp responsivo)
  - H2: 3xl-4xl
  - H3: xl-3xl
  - Body: base-lg

### Animações

- **Scroll Reveal**: Fade-up com IntersectionObserver
- **Marquee**: Horizontal infinito (25s linear)
- **Float**: Badge flutuante (3s ease-in-out)
- **Hover**: Transform, opacity, border transitions

## 🚀 Como Usar

### Opção 1: Acesso Direto
Simplesmente abra o arquivo `index.html` em qualquer navegador moderno.

### Opção 2: Servidor Local
```bash
# Usando Python 3
python -m http.server 8000

# Usando Node.js (http-server)
npx http-server

# Usando PHP
php -S localhost:8000
```

Acesse: `http://localhost:8000`

## 📱 Responsividade

O site é totalmente responsivo com breakpoints otimizados:

- **Mobile**: < 768px (1 coluna, menu full-screen)
- **Tablet**: 768px - 1024px (2 colunas em grids)
- **Desktop**: > 1024px (3 colunas, layout completo)

## ⚡ Performance

- **Lazy Loading**: Imagens carregam sob demanda
- **IntersectionObserver**: Animações otimizadas
- **CSS Minificado**: Classes Tailwind eficientes
- **Single Page**: Sem navegação entre páginas
- **CDN**: Recursos externos via CDN

## 🔧 Customização

### Alterar Cores
Edite as classes Tailwind no arquivo `index.html` ou adicione custom properties no `<style>`.

### Adicionar Projetos
Adicione novos cards na seção `#projetos` seguindo o padrão do Bento Grid:
- Use classes `lg:col-span-X` para controlar largura
- Mantenha estrutura Challenge/Solution para projetos maiores

### Atualizar Conteúdo
Todo o conteúdo está em português dentro do `index.html`:
- Textos: Direto no HTML
- Imagens: Diretório `/img/`
- Links: Atributos `href`

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

**Jhonatas Lima**
- Tech Lead & Solutions Architect
- Website: [JHL Software](https://www.jhonataslima.com/)
- LinkedIn: [@jhonataslima](https://www.linkedin.com/in/jhonataslima/)
- GitHub: [@jhonnhenry](https://github.com/jhonnhenry)
- Instagram: [@jhonatashenrique](https://www.instagram.com/jhonatashenrique/)
- Email: contato@jhonataslima.com

## 🙏 Agradecimentos

Landing page desenvolvida com:
- [Tailwind CSS](https://tailwindcss.com/)
- [Lucide Icons](https://lucide.dev/)
- [Google Fonts (Inter)](https://fonts.google.com/specimen/Inter)
- [Unsplash](https://unsplash.com/) (imagens de referência nas versões anteriores)

---

**Construindo o futuro com o que há de melhor no mundo da tecnologia** 🚀

🤖 Generated with [Claude Code](https://claude.com/claude-code)
