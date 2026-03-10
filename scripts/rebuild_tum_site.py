from pathlib import Path
from textwrap import dedent

root = Path('.')

nav_items = [
    ('HOME', 'index.html'),
    ('UNIFORME ȘCOLARE', 'uniforme-scolare.html'),
    ('CORPORATE', 'corporate.html'),
    ('MEDICAL', 'medical.html'),
    ('HOSPITALITY', 'hospitality.html'),
    ('WORKWEAR', 'workwear.html'),
    ('DESIGN & PRODUCȚIE', 'servicii.html'),
    ('COLECȚII UNIFORME', 'catalog.html'),
    ('MĂSURĂTORI', 'configurator.html'),
    ('PROIECTE', 'portofoliu.html'),
    ('DESPRE NOI', 'despre.html'),
    ('CONTACT', 'contact.html'),
]

company_name = 'The Uniform Maker'
cta_link = 'contact.html'
cta_label = 'Solicită ofertă'


def nav(active):
    links = '\n'.join(
        f'<li><a href="{href}"{" class=\"active\"" if href == active else ""}>{label}</a></li>'
        for label, href in nav_items
    )
    return f'''
    <nav class="site-nav" id="top">
      <div class="shell nav-inner">
        <a href="index.html" class="brand" aria-label="{company_name}">
          <img src="images/logo.png" alt="{company_name}" class="brand-logo">
          <span class="brand-text">{company_name}</span>
        </a>
        <button class="nav-toggle" aria-label="Deschide meniul" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
        <div class="nav-panel">
          <ul class="nav-links">{links}</ul>
          <a href="{cta_link}" class="btn btn-primary nav-button">{cta_label}</a>
        </div>
      </div>
    </nav>
    '''


def footer():
    return '''
    <footer class="site-footer">
      <div class="shell footer-grid">
        <div>
          <h3>The Uniform Maker</h3>
          <p>Uniforme dezvoltate pentru instituții educaționale și organizații.</p>
        </div>
        <div>
          <h4>Companie</h4>
          <ul>
            <li><a href="despre.html">Despre noi</a></li>
            <li><a href="portofoliu.html">Proiecte</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>
        <div>
          <h4>Industrii</h4>
          <ul>
            <li><a href="uniforme-scolare.html">Uniforme școlare</a></li>
            <li><a href="corporate.html">Corporate</a></li>
            <li><a href="medical.html">Medical</a></li>
            <li><a href="hospitality.html">Hospitality</a></li>
            <li><a href="workwear.html">Workwear</a></li>
          </ul>
        </div>
        <div>
          <h4>Servicii</h4>
          <ul>
            <li><a href="servicii.html">Design & producție</a></li>
            <li><a href="catalog.html">Colecții uniforme</a></li>
            <li><a href="configurator.html">Măsurători</a></li>
          </ul>
        </div>
        <div>
          <h4>Contact</h4>
          <ul>
            <li><a href="mailto:contact@theuniformmaker.ro">contact@theuniformmaker.ro</a></li>
            <li><a href="tel:+40721234567">+40 721 234 567</a></li>
            <li>București, România</li>
            <li><a href="contact.html">GDPR · Termeni</a></li>
          </ul>
        </div>
      </div>
    </footer>
    '''


def page(title, description, active, body, extra_head=''):
    return dedent(f'''<!DOCTYPE html>
    <html lang="ro">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>{title}</title>
      <meta name="description" content="{description}">
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap" rel="stylesheet">
      <link rel="stylesheet" href="css/style.css">
      {extra_head}
    </head>
    <body>
      {nav(active)}
      {body}
      {footer()}
      <script src="js/main.js"></script>
    </body>
    </html>
    ''')


index_body = '''
<header class="hero hero-home">
  <div class="shell hero-grid">
    <div class="eyebrow">Design • Prototip • Producție</div>
    <h1>Uniforme școlare & uniforme profesionale</h1>
    <p class="lead">Creăm uniforme pentru instituții educaționale și organizații.</p>
    <div class="hero-actions">
      <a href="contact.html" class="btn btn-primary">Solicită ofertă</a>
      <a href="catalog.html" class="btn btn-secondary">Vezi colecțiile</a>
    </div>
  </div>
</header>

<section class="section">
  <div class="shell split-cards">
    <article class="feature-card feature-card-accent">
      <span class="section-kicker">Mod de colaborare</span>
      <h2>Design & producție uniformă</h2>
      <p>Creăm uniforma organizației tale. Design. Prototip. Producție proprie.</p>
      <a href="servicii.html" class="text-link">Solicită ofertă</a>
    </article>
    <article class="feature-card">
      <span class="section-kicker">Colecții</span>
      <h2>Colecții uniforme</h2>
      <p>Modele dezvoltate de noi. Disponibile pentru comandă și personalizare.</p>
      <a href="catalog.html" class="text-link">Vezi colecțiile</a>
    </article>
  </div>
</section>

<section class="section section-tint">
  <div class="shell">
    <div class="section-heading">
      <span class="section-kicker">Industrii</span>
      <h2>Uniforme dezvoltate pentru organizații</h2>
    </div>
    <div class="industry-grid">
      <a class="industry-card" href="uniforme-scolare.html"><div class="industry-image img-school"></div><h3>Uniforme școlare</h3><p>Colecții clare pentru instituții educaționale.</p></a>
      <a class="industry-card" href="corporate.html"><div class="industry-image img-corporate"></div><h3>Corporate</h3><p>Ținute coerente pentru echipe și recepții.</p></a>
      <a class="industry-card" href="medical.html"><div class="industry-image img-medical"></div><h3>Medical</h3><p>Uniforme funcționale pentru clinici și spitale.</p></a>
      <a class="industry-card" href="hospitality.html"><div class="industry-image img-hospitality"></div><h3>Hospitality</h3><p>Uniforme pentru hoteluri și restaurante.</p></a>
      <a class="industry-card" href="workwear.html"><div class="industry-image img-workwear"></div><h3>Workwear</h3><p>Produse rezistente pentru medii de lucru.</p></a>
    </div>
    <div class="section-cta"><a href="contact.html" class="btn btn-primary">Solicită ofertă</a></div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="section-heading">
      <span class="section-kicker">Proces</span>
      <h2>Cum dezvoltăm o uniformă</h2>
      <p>Un proces clar. De la consultanță la livrare.</p>
    </div>
    <div class="timeline">
      <div><strong>1</strong><span>Consultanță</span></div>
      <div><strong>2</strong><span>Design</span></div>
      <div><strong>3</strong><span>Prototip</span></div>
      <div><strong>4</strong><span>Testare</span></div>
      <div><strong>5</strong><span>Producție</span></div>
      <div><strong>6</strong><span>Livrare</span></div>
    </div>
    <p class="process-note">Optitex • dezvoltare produs</p>
    <div class="section-cta"><a href="contact.html" class="btn btn-secondary">Solicită ofertă</a></div>
  </div>
</section>

<section class="section section-tint">
  <div class="shell two-col tech-block">
    <div>
      <span class="section-kicker">Tehnologie</span>
      <h2>Măsurători digitale</h2>
      <p>Scanare corporală. Recomandare mărime. Centralizare automată.</p>
      <p class="process-note">Esenca</p>
      <a href="configurator.html" class="btn btn-primary">Solicită ofertă</a>
    </div>
    <div class="scan-visual">
      <div class="scan-frame"></div>
      <div class="scan-line"></div>
      <div class="scan-points"></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="section-heading">
      <span class="section-kicker">Portofoliu</span>
      <h2>Proiecte realizate</h2>
      <p>Școli. Hoteluri. Corporate. Medical.</p>
    </div>
    <div class="project-grid compact-grid">
      <article class="project-card"><div class="project-image img-school"></div><h3>Școli private</h3></article>
      <article class="project-card"><div class="project-image img-hospitality"></div><h3>Hoteluri</h3></article>
      <article class="project-card"><div class="project-image img-corporate"></div><h3>Corporate</h3></article>
      <article class="project-card"><div class="project-image img-medical"></div><h3>Medical</h3></article>
    </div>
    <div class="section-cta"><a href="portofoliu.html" class="btn btn-secondary">Vezi proiectele</a></div>
  </div>
</section>

<section class="section cta-band">
  <div class="shell centered">
    <span class="section-kicker">Call to action</span>
    <h2>Dezvoltăm uniforma organizației tale</h2>
    <p>Design. Prototip. Producție.</p>
    <a href="contact.html" class="btn btn-primary">Solicită ofertă</a>
  </div>
</section>
'''

servicii_body = '''
<header class="hero hero-inner"><div class="shell"><span class="section-kicker">Serviciu</span><h1>Design & producție uniformă</h1><p class="lead">Creăm uniforme pentru instituții de învățământ și organizații.</p><p class="hero-mini">Design digital. Prototip sigur. Producție controlată.</p><a href="contact.html" class="btn btn-primary">Solicită ofertă</a></div></header>
<section class="section"><div class="shell"><div class="section-heading"><h2>Pentru cine este acest serviciu</h2><p>Un serviciu creat pentru organizații care au nevoie de o uniformă proprie.</p></div><div class="pill-grid"><span>Școli</span><span>Companii</span><span>Clinici</span><span>Instituții</span><span>Echipe profesionale</span></div></div></section>
<section class="section section-tint"><div class="shell"><div class="section-heading"><h2>Ce producem</h2><p>Uniforme create pentru identitatea organizației tale.</p></div><div class="content-grid three"><article class="content-card"><h3>Tipuri de uniforme</h3><ul><li>uniforme școlare</li><li>uniforme corporate</li><li>uniforme medicale</li><li>uniforme hospitality</li><li>workwear</li></ul></article><article class="content-card"><h3>Ce putem include</h3><ul><li>design dedicat</li><li>croială funcțională</li><li>culori personalizate</li><li>alegere materiale</li><li>broderie sau serigrafie</li></ul></article><article class="content-card"><h3>Organizare</h3><ul><li>structură pe mărimi</li><li>validare mostre</li><li>producție în loturi</li><li>livrare planificată</li></ul></article></div><div class="section-cta"><a href="contact.html" class="btn btn-primary">Solicită ofertă</a></div></div></section>
<section class="section"><div class="shell"><div class="section-heading"><h2>Cum lucrăm</h2><p>Un proces clar. De la idee la produs final.</p></div><div class="steps-list"><article><strong>1.</strong><h3>Discuție inițială</h3><p>Înțelegem nevoile proiectului.</p></article><article><strong>2.</strong><h3>Direcție vizuală</h3><p>Stabilim stilul și structura uniformei.</p></article><article><strong>3.</strong><h3>Design digital</h3><p>Modelele sunt definite în simulare 3D.</p></article><article><strong>4.</strong><h3>Mostră digitală</h3><p>Corecțiile de croi și design se fac în simulare.</p></article><article><strong>5.</strong><h3>Prototip</h3><p>După validare, realizăm prototipul fizic.</p></article><article><strong>6.</strong><h3>Producție & livrare</h3><p>Executăm comanda organizat și livrăm conform structurii.</p></article></div></div></section>
<section class="section section-tint"><div class="shell two-col"><div><span class="section-kicker">Design și tehnologie</span><h2>Definim produsul digital înainte de producție</h2><p>Lucrăm cu proiectare digitală, dezvoltare tehnică de produs, prototipare și verificare de execuție.</p><p class="process-note">Optitex 3D • Esenca</p></div><div class="content-card"><h3>Personalizare</h3><ul><li>logo</li><li>culori</li><li>combinații de materiale</li><li>elemente distinctive</li><li>etichetare</li><li>structură pe funcții</li></ul></div></div></section>
<section class="section"><div class="shell two-col"><div class="content-card"><h3>Măsurători și organizare mărimi</h3><p>Scanare digitală, recomandare de mărime și centralizare pentru grupuri mari.</p><a href="configurator.html" class="text-link">Vezi măsurătorile</a></div><div class="content-card"><h3>Producție proprie</h3><p>Control mai bun. Execuție clară. Continuitate.</p><ul><li>control pe etape</li><li>coerență între mostră și producție</li><li>capacitate de personalizare</li><li>comunicare directă</li></ul></div></div></section>
<section class="section cta-band"><div class="shell centered"><h2>Hai să construim uniforma organizației tale</h2><p>Design digital. Prototip sigur. Producție controlată.</p><a href="contact.html" class="btn btn-primary">Solicită ofertă</a></div></section>
'''

catalog_body = '''
<header class="hero hero-inner"><div class="shell"><span class="section-kicker">Colecții</span><h1>Colecții uniforme</h1><p class="lead">Modele dezvoltate de noi. Disponibile pentru comandă și personalizare.</p><a href="contact.html" class="btn btn-primary">Solicită ofertă</a></div></header>
<section class="section"><div class="shell"><div class="section-heading"><h2>Colecții construite pentru utilizare reală</h2><p>Colecții standard care pot fi adaptate prin culoare, logo și structură de produse.</p></div><div class="content-grid three"><article class="collection-card"><div class="project-image img-school"></div><h3>Școlare</h3><p>Uniforme fete. Uniforme băieți. Tricotaje. Uniforme sport.</p><a href="uniforme-scolare.html" class="text-link">Vezi categoria</a></article><article class="collection-card"><div class="project-image img-corporate"></div><h3>Corporate</h3><p>Ținute pentru recepție, birou, front desk și echipe comerciale.</p><a href="corporate.html" class="text-link">Vezi categoria</a></article><article class="collection-card"><div class="project-image img-medical"></div><h3>Medical</h3><p>Produse pentru clinici, cabinete, spitale și laboratoare.</p><a href="medical.html" class="text-link">Vezi categoria</a></article><article class="collection-card"><div class="project-image img-hospitality"></div><h3>Hospitality</h3><p>Uniforme pentru hoteluri, restaurante și servicii premium.</p><a href="hospitality.html" class="text-link">Vezi categoria</a></article><article class="collection-card"><div class="project-image img-workwear"></div><h3>Workwear</h3><p>Produse rezistente pentru echipe operaționale și producție.</p><a href="workwear.html" class="text-link">Vezi categoria</a></article><article class="collection-card"><div class="project-image img-neutral"></div><h3>Comenzi standard</h3><p>Pentru produsele din colecții, comenzile pot începe de la 10 seturi per produs.</p><a href="contact.html" class="text-link">Solicită ofertă</a></article></div></div></section>
<section class="section section-tint"><div class="shell two-col"><div><h2>Colecțiile susțin magazinul online fără a coborî brandul</h2><p>Pagina păstrează un discurs premium și pune accentul pe calitate, nu pe volum.</p></div><div class="content-card"><h3>Poți personaliza</h3><ul><li>logo</li><li>culori</li><li>materiale</li><li>etichetare</li><li>structură pe mărimi</li></ul></div></div></section>
'''

meas_body = '''
<header class="hero hero-inner"><div class="shell"><span class="section-kicker">Măsurători</span><h1>Măsurători digitale</h1><p class="lead">Măsurători precise pentru fiecare proiect.</p><p class="hero-mini">Scanare digitală. Recomandare automată de mărimi. Centralizare rapidă a datelor.</p><a href="contact.html" class="btn btn-primary">Solicită ofertă</a></div></header>
<section class="section"><div class="shell two-col tech-block"><div><h2>Tehnologie Esenca</h2><p>O uniformă bună începe cu o mărime corectă. Putem integra scanare digitală, recomandare de mărime și tabel inteligent pentru proiecte mari.</p><ul class="check-list"><li>scanare digitală</li><li>recomandare de mărime</li><li>tabel inteligent de măsuri</li><li>centralizare pentru grupuri mari</li></ul></div><div class="scan-visual"><div class="scan-frame"></div><div class="scan-line"></div><div class="scan-points"></div></div></div></section>
<section class="section section-tint"><div class="shell"><div class="section-heading"><h2>Unde este esențial</h2><p>Această etapă este importantă pentru școli, companii și proiecte cu echipe mari.</p></div><div class="pill-grid"><span>școli</span><span>companii</span><span>clinici</span><span>hoteluri</span><span>echipe mari</span></div></div></section>
'''

portfolio_body = '''
<header class="hero hero-inner"><div class="shell"><span class="section-kicker">Proiecte</span><h1>Proiecte realizate</h1><p class="lead">Uniforme dezvoltate pentru instituții educaționale și organizații.</p><a href="contact.html" class="btn btn-primary">Solicită ofertă</a></div></header>
<section class="section"><div class="shell"><div class="project-grid"><article class="project-card"><div class="project-image img-school"></div><div class="project-meta"><span>Școli private</span><h3>Proiecte școlare</h3><p>Structuri clare de produse și mărimi.</p></div></article><article class="project-card"><div class="project-image img-corporate"></div><div class="project-meta"><span>Corporate</span><h3>Uniforme pentru echipe</h3><p>Ținute coerente pentru branduri și recepții.</p></div></article><article class="project-card"><div class="project-image img-medical"></div><div class="project-meta"><span>Medical</span><h3>Produse funcționale</h3><p>Uniforme pentru clinici și cabinete.</p></div></article><article class="project-card"><div class="project-image img-hospitality"></div><div class="project-meta"><span>Hospitality</span><h3>Experiență premium</h3><p>Uniforme pentru hoteluri și restaurante.</p></div></article></div></div></section>
'''

about_body = '''
<header class="hero hero-inner"><div class="shell"><span class="section-kicker">Despre noi</span><h1>Un partener care înțelege uniforma ca produs complet</h1><p class="lead">Design & producție în același flux. Experiență în uniforme școlare și profesionale.</p><a href="contact.html" class="btn btn-primary">Solicită ofertă</a></div></header>
<section class="section"><div class="shell two-col"><div><h2>Ce ne diferențiază</h2><ul class="check-list"><li>design & producție în același flux</li><li>personalizare reală</li><li>măsurători și organizare pe mărimi</li><li>producție proprie</li></ul></div><div class="content-card"><h3>Lucrăm pentru</h3><p>Instituții educaționale, companii, clinici, hoteluri și echipe profesionale care au nevoie de o uniformă clară, coerentă și bine executată.</p></div></div></section>
'''

contact_body = '''
<header class="hero hero-inner"><div class="shell"><span class="section-kicker">Contact</span><h1>Hai să discutăm proiectul tău</h1><p class="lead">Spune-ne de ce tip de uniformă ai nevoie și revenim cu structură și pași clari.</p></div></header>
<section class="section"><div class="shell contact-layout"><div class="content-card"><h2>Date de contact</h2><ul class="contact-list"><li><strong>Email</strong><span>contact@theuniformmaker.ro</span></li><li><strong>Telefon</strong><span>+40 721 234 567</span></li><li><strong>Adresă</strong><span>București, România</span></li></ul></div><form class="content-card contact-form"><h2>Solicită ofertă</h2><div class="form-grid"><label><span>Nume</span><input type="text" placeholder="Nume complet"></label><label><span>Email</span><input type="email" placeholder="email@companie.ro"></label><label><span>Telefon</span><input type="tel" placeholder="+40"></label><label><span>Organizație</span><input type="text" placeholder="Companie / instituție"></label><label class="full"><span>Detalii proiect</span><textarea placeholder="Tip uniformă, volum, termen, personalizare"></textarea></label></div><button type="submit" class="btn btn-primary">Trimite solicitarea</button></form></div></section>
'''

product_body = '''
<header class="hero hero-inner"><div class="shell"><span class="section-kicker">Colecții</span><h1>Produs din colecție</h1><p class="lead">Pagină demo pentru produse standard care pot fi personalizate.</p></div></header>
<section class="section"><div class="shell two-col"><div class="project-image img-neutral tall"></div><div class="content-card"><h2>Exemplu produs standard</h2><p>Produsele din colecții pot fi adaptate prin culoare, logo și structură de mărimi.</p><ul class="check-list"><li>comandă începând de la 10 seturi</li><li>logo și etichetare disponibile</li><li>organizare pe mărimi</li></ul><a href="contact.html" class="btn btn-primary">Solicită ofertă</a></div></div></section>
'''

cart_body = '''
<header class="hero hero-inner"><div class="shell"><span class="section-kicker">Comenzi</span><h1>Structura comenzilor</h1><p class="lead">Pentru proiecte personalizate, producția se organizează în funcție de numărul de persoane, tipul produselor și structura proiectului.</p><a href="contact.html" class="btn btn-primary">Discută proiectul</a></div></header>
'''

industry_pages = {
    'uniforme-scolare.html': ('Uniforme școlare', 'Colecții dezvoltate pentru instituții educaționale.', 'uniforme-scolare.html', 'uniforme fete • uniforme băieți • tricotaje • uniforme sport'),
    'corporate.html': ('Corporate', 'Ținute pentru organizații și echipe profesionale.', 'corporate.html', 'recepție • office wear • front desk • echipe comerciale'),
    'medical.html': ('Medical', 'Uniforme funcționale pentru clinici și spitale.', 'medical.html', 'clinici • cabinete • spitale • laboratoare'),
    'hospitality.html': ('Hospitality', 'Uniforme pentru hoteluri și restaurante.', 'hospitality.html', 'hoteluri • restaurante • recepție • servicii premium'),
    'workwear.html': ('Workwear', 'Produse rezistente pentru medii de lucru.', 'workwear.html', 'operațional • logistică • producție • service'),
}

for filename, (title_text, desc, active, bullets) in industry_pages.items():
    body = f'''
    <header class="hero hero-inner"><div class="shell"><span class="section-kicker">Industrie</span><h1>{title_text}</h1><p class="lead">{desc}</p><a href="contact.html" class="btn btn-primary">Solicită ofertă</a></div></header>
    <section class="section"><div class="shell two-col"><div class="project-image img-neutral tall"></div><div><h2>{title_text}</h2><p>Uniforme dezvoltate pentru proiecte în care identitatea vizuală și funcționalitatea trebuie să meargă împreună.</p><div class="pill-grid"><span>{'</span><span>'.join(bullets.split(' • '))}</span></div><div class="section-cta left"><a href="contact.html" class="btn btn-secondary">Solicită ofertă</a></div></div></div></section>
    '''
    (root / filename).write_text(page(f'{title_text} | The Uniform Maker', desc, active, body), encoding='utf-8')

files = {
    'index.html': page('The Uniform Maker | Uniforme școlare & uniforme profesionale', 'Uniforme premium pentru instituții educaționale și organizații.', 'index.html', index_body),
    'servicii.html': page('Design & producție uniformă | The Uniform Maker', 'Design, prototip și producție proprie pentru uniforme.', 'servicii.html', servicii_body),
    'catalog.html': page('Colecții uniforme | The Uniform Maker', 'Colecții uniforme disponibile pentru comandă și personalizare.', 'catalog.html', catalog_body),
    'configurator.html': page('Măsurători digitale | The Uniform Maker', 'Măsurători digitale și organizare de mărimi pentru proiecte mari.', 'configurator.html', meas_body),
    'portofoliu.html': page('Proiecte | The Uniform Maker', 'Proiecte realizate pentru școli și organizații.', 'portofoliu.html', portfolio_body),
    'despre.html': page('Despre noi | The Uniform Maker', 'Design și producție în același flux.', 'despre.html', about_body),
    'contact.html': page('Contact | The Uniform Maker', 'Solicită ofertă pentru uniforma organizației tale.', 'contact.html', contact_body),
    'produs.html': page('Produs | The Uniform Maker', 'Exemplu de produs standard din colecții.', 'catalog.html', product_body),
    'cos.html': page('Comenzi | The Uniform Maker', 'Structura comenzilor pentru proiecte personalizate.', 'contact.html', cart_body),
}

for name, content in files.items():
    (root / name).write_text(content, encoding='utf-8')
