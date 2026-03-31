---
tags:
  - squads
  - ia
  - agentes
  - automacao
aliases:
  - Xquads
  - Squads IA
---

# Squads IA

13 squads especializados com 150 agentes, 128 tasks, 28 workflows e 1 orquestrador.

Protocolo de roteamento: [[squads/orquestrador|Orquestrador]]

---

## Orquestrador

### [[squads/orquestrador|Orquestrador]] — Protocolo de Roteamento
Cerebro que recebe qualquer pedido, faz perguntas minimas, monta o time certo e executa em cadeia.
Nao e um agente — e o protocolo que o Claude segue pra mobilizar squads.

---

## Estrategia e Lideranca

### [[squads/advisory-board/advisory-board|Advisory Board]] — 11 agentes
Conselho estrategico virtual com pensadores lendarios.
`@board-chair` `*diagnose` `*board-meeting` `*decision-framework`
Agentes: Ray Dalio, Charlie Munger, Naval Ravikant, Peter Thiel, Reid Hoffman, Simon Sinek, Brene Brown, Patrick Lencioni, Derek Sivers, Yvon Chouinard

### [[squads/c-level-squad/c-level-squad|C-Level Squad]] — 6 agentes
C-suite virtual completa.
`@vision-chief` `*diagnose` `*executive-strategy` `*org-health`
Agentes: Vision Chief (CEO), COO, CMO, CTO, CIO, CAIO

---

## Vendas e Negocios

### [[squads/hormozi-squad/hormozi-squad|Hormozi Squad]] — 16 agentes
Frameworks de Alex Hormozi para escalar negocios.
`@hormozi-chief` `*diagnose` `*business-turnaround` `*offer-pipeline`
Agentes: Offers, Leads, Pricing, Closer, Ads, Content, Hooks, Launch, Retention, Scale, Models, Audit, Copy, Workshop, Advisor

### [[squads/copy-squad/copy-squad|Copy Squad]] — 23 agentes
Elite de copywriting — 22 copywriters lendarios + 1 orquestrador.
`@copy-chief` `*diagnose` `*copy-project` `*swipe-analysis`
Agentes: Gary Halbert, David Ogilvy, Eugene Schwartz, Claude Hopkins, Dan Kennedy, Frank Kern, Russell Brunson, Stefan Georgi, Gary Bencivenga, John Carlton, Joe Sugarman, Robert Collier, Ben Settle, Andre Chaperon, Dan Koe, Jim Rutz, Clayton Makepeace, David Deutsch, Todd Brown, Jon Benson, Ry Schwartz, Parris Lampropoulos

---

## Marketing e Trafego

### [[squads/traffic-masters/traffic-masters|Traffic Masters]] — 16 agentes
Dominio de trafego pago em todas as plataformas.
`@traffic-chief` `*diagnose` `*traffic-audit` `*campaign-plan`
Agentes: Pedro Sobral, Kasim Aslam, Molly Pittman, Ralph Burns, Tom Breeze, Depesh Mandalia, Nicholas Kusmich, Ad Midas, Media Buyer, Ads Analyst, Creative Analyst, Performance Analyst, Pixel Specialist, Scale Optimizer, Fiscal

### [[squads/brand-squad/brand-squad|Brand Squad]] — 15 agentes
Estrategia de marca — 10 pensadores lendarios de branding.
`@brand-chief` `*diagnose` `*brand-sprint` `*positioning`
Agentes: David Aaker, Al Ries, Marty Neumeier, Kevin Keller, Alina Wheeler, Jean-Noel Kapferer, Byron Sharp, Donald Miller, Denise Yohn, Emily Heyward, Archetype Consultant, Naming Strategist, Domain Scout, Miller Sticky Brand

### [[squads/movement/movement|Movement]] — 7 agentes
Construir movimentos que transcendem marcas e produtos.
`@movement-chief` `*diagnose` `*movement-design`
Agentes: Movement Architect, Fenomenologo, Identitario, Estrategista de Ciclo, Manifestador, Analista de Impacto

---

## Conteudo e Narrativa

### [[squads/storytelling/storytelling|Storytelling]] — 12 agentes
Mestres de narrativa — mitologia, roteiro, pitch, apresentacao.
`@story-chief` `*diagnose` `*story-craft` `*pitch-design`
Agentes: Joseph Campbell, Dan Harmon, Blake Snyder, Shawn Coyne, Keith Johnstone, Nancy Duarte, Oren Klaff, Park Howell, Matthew Dicks, Kindra Hall, Marshall Ganz

---

## Tecnologia e Design

### [[squads/design-squad/design-squad|Design Squad]] — 8 agentes
Design operations — experts + especialistas + orquestrador.
`@design-chief` `*diagnose` `*design-audit` `*design-system`
Agentes: Brad Frost (Atomic Design), Dan Mall (Design Leadership), Dave Malouf (Design Ops), Design System Architect, UI Engineer, UX Designer, Visual Generator

### [[squads/claude-code-mastery/claude-code-mastery|Claude Code Mastery]] — 8 agentes
Dominio completo do Claude Code — hooks, skills, MCP, plugins.
`@claude-mastery-chief` `*diagnose` `*optimize-setup`
Agentes: Hooks Architect, Skill Craftsman, MCP Integrator, Config Engineer, Swarm Orchestrator, Project Integrator, Roadmap Sentinel

### [[squads/cybersecurity/cybersecurity|Cybersecurity]] — 15 agentes
Seguranca ofensiva e defensiva — pentest, red/blue team, AppSec.
`@cyber-chief` `*diagnose` `*security-audit` `*threat-model`
Agentes: Georgia Weidman, Peter Kim, Jim Manico, Chris Sanders, Marcus Carey, Omar Santos, + 9 especialistas operacionais

### [[squads/data-squad/data-squad|Data Squad]] — 7 agentes
Estrategistas data-driven — analytics, CLV, growth, comunidade.
`@data-chief` `*diagnose` `*data-audit` `*growth-analysis`
Agentes: Avinash Kaushik (Analytics), Peter Fader (CLV), Sean Ellis (Growth), Wes Kao (Cohorts), Nick Mehta (Customer Success), David Spinks (Community)

---

## Como usar

**Modo automatico (recomendado):**
Descreva o que precisa em linguagem natural. O [[squads/orquestrador|Orquestrador]] identifica os squads certos, monta o pipeline e executa.

**Modo direto:**
1. Ative o orquestrador do squad: `@hormozi-chief`, `@copy-chief`, etc.
2. Use `*diagnose` para triagem do problema
3. O orquestrador delega para os agentes certos
4. Ou ative um agente direto: `@ray-dalio`, `@gary-halbert`, etc.

---

## Links
- [[squads/orquestrador|Orquestrador]] — Protocolo de roteamento inteligente
