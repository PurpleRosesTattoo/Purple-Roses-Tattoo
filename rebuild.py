from pathlib import Path
import re, zipfile, json

root=Path('/mnt/data/build3'); path=root/'index.html'; html=path.read_text(encoding='utf-8')

# Remove all incremental styles after the base stylesheet, preserving all body markup.
style_pat=re.compile(r'<style(?:\s+id="([^"]+)")?[^>]*>.*?</style>',re.S|re.I)
styles=list(style_pat.finditer(html))
base=styles[0].group(0)
keep_ids=set()
# Replace all styles except first with empty; keep first in place.
new=[]; last=0
for i,m in enumerate(styles):
    new.append(html[last:m.start()])
    if i==0: new.append(base)
    last=m.end()
new.append(html[last:])
html=''.join(new)

final_css=r'''<style id="PR-FINAL-2026">
:root{--pr-purple:#9b4de5;--pr-pink:#c54be0;--pr-blue:#4b86e8;--pr-white:#f5f2fb}
html,body{width:100%;max-width:100%;overflow-x:hidden}html{scroll-behavior:smooth}body{min-width:0}
.wrap{width:min(1240px,calc(100% - 42px));max-width:100%;margin-inline:auto}
/* HERO — everything shares one physical center axis */
.hero{min-height:100svh;display:flex;align-items:center;padding:110px 0 70px;position:relative;overflow:hidden}
.hero-grid{width:min(100%,1080px)!important;margin-inline:auto!important;display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;gap:10px!important;text-align:center!important}
.hero-grid>div:first-child{order:2!important;width:100%!important;display:flex!important;flex-direction:column!important;align-items:center!important;text-align:center!important}
.hero-art{order:1!important;width:100%!important;height:clamp(330px,52vw,570px)!important;display:flex!important;align-items:center!important;justify-content:center!important;margin-inline:auto!important;position:relative!important}
.hero-logo{display:block!important;width:min(500px,82vw)!important;max-height:540px!important;height:auto!important;margin:0 auto!important;position:relative!important;left:0!important;right:0!important;mix-blend-mode:normal!important;filter:drop-shadow(0 18px 45px rgba(124,69,216,.22))!important;animation:prHeroFloat 6s ease-in-out infinite}
@keyframes prHeroFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
.hero h1{width:100%!important;margin:12px auto 24px!important;text-align:center!important;line-height:.82!important}.hero .eyebrow,.hero .hero-copy,.hero .hero-actions{margin-left:auto!important;margin-right:auto!important;text-align:center!important}
.hero-copy{width:min(100%,720px)!important;max-width:720px!important;font-size:18px;line-height:1.7}.hero-actions{display:flex!important;justify-content:center!important;align-items:center!important;flex-wrap:wrap!important;gap:12px;margin-top:28px!important}
.hero .orb,.hero .orn,.hero .decor-vine,.hero .botanical-vine,.hero .edge-vine,.hero .v3-vine,.hero .vine-layer,.hero .real-vine,.hero .section-vines{display:none!important}
/* VINES — ONLY in the gaps between sections */
.pr-vine-zone{position:relative!important;width:100vw!important;margin-left:calc(50% - 50vw)!important;margin-right:calc(50% - 50vw)!important;height:clamp(120px,15vw,190px)!important;overflow:hidden!important;pointer-events:none!important;isolation:isolate!important;border:0!important;padding:0!important}
.pr-vine{position:absolute!important;width:min(55vw,650px)!important;height:auto!important;max-width:none!important;opacity:0!important;visibility:visible!important;will-change:transform,opacity,filter!important;filter:drop-shadow(0 0 9px rgba(73,103,220,.20))!important;z-index:1!important}
.pr-vine.left{left:0!important;top:10%!important;transform:translate3d(-108%,0,0)!important;transform-origin:left center!important}.pr-vine.right{right:0!important;top:52%!important;transform:translate3d(108%,0,0) scaleX(-1)!important;transform-origin:right center!important}
.pr-vine.left.second{top:52%!important}.pr-vine.right.second{top:10%!important}
/* ARTISTS — whole card moves as one object */
.artist{will-change:transform,opacity,filter!important;backface-visibility:hidden;transform-origin:center center}.artist-photo{will-change:transform!important}
/* GALLERIES — no fade-in, only tiny depth */
.gallery .card{opacity:1!important;will-change:transform!important;transition:transform .28s ease,filter .28s ease!important}.gallery .card img{will-change:transform!important;transition:transform .25s ease!important}.gallery .card:hover img{transform:scale(1.018)!important}
#flashs .gallery .meta,#realisations .gallery .meta{display:none!important}#flashs .gallery .card,#realisations .gallery .card{border:0;background:transparent;box-shadow:none}
/* TITLES — fill sweep, like the reference video, not opacity */
.pr-ink-title{--ink-progress:0%;position:relative!important;color:transparent!important;background-image:linear-gradient(90deg,var(--pr-white) 0%,var(--pr-white) calc(var(--ink-progress) - 1%),rgba(245,242,251,.14) calc(var(--ink-progress) + 1%),rgba(245,242,251,.14) 100%)!important;background-clip:text!important;-webkit-background-clip:text!important;-webkit-text-fill-color:transparent!important;-webkit-text-stroke:1px rgba(245,242,251,.76)!important;will-change:background-image!important}
.hero h1.pr-ink-title{--ink-progress:100%;-webkit-text-stroke:0!important}
section{position:relative;overflow:visible}section>.wrap{position:relative;z-index:3}.section-head,.story,.artists,.gallery,.studio-grid,.location,.booking-grid{position:relative;z-index:3}
.scroll-progress{position:fixed;left:0;top:0;width:100%;height:2px;z-index:1000;background:rgba(255,255,255,.05);pointer-events:none}.scroll-progress span{display:block;width:100%;height:100%;transform:scaleX(0);transform-origin:left;background:linear-gradient(90deg,var(--pr-purple),var(--pr-pink),var(--pr-blue));box-shadow:0 0 12px rgba(192,68,200,.55)}
@media(max-width:900px){.wrap{width:calc(100% - 28px)}.hero{padding:88px 0 58px}.hero-art{height:350px!important}.hero-logo{width:min(390px,82vw)!important;max-height:350px!important}.hero h1{font-size:clamp(64px,16vw,105px)!important}.hero-copy{font-size:16px;line-height:1.65}.pr-vine-zone{height:145px!important}.pr-vine{width:min(68vw,500px)!important}}
@media(max-width:560px){section{padding:78px 0}.hero{padding:82px 0 55px}.hero-art{height:300px!important}.hero-logo{width:min(300px,78vw)!important;max-height:300px!important}.hero h1{font-size:17vw!important;line-height:.84!important}.hero-copy{width:100%!important;font-size:15px}.hero-actions{width:100%!important}.hero-actions .btn{flex:1 1 100%}.pr-vine-zone{height:120px!important}.pr-vine{width:78vw!important}.pr-vine.left{top:7%!important}.pr-vine.right{top:53%!important}.pr-vine.left.second{top:53%!important}.pr-vine.right.second{top:7%!important}.section-head h2,.story h2,.booking h2{font-size:clamp(48px,14vw,70px)!important;line-height:.86!important}}
@media(prefers-reduced-motion:reduce){.hero-logo{animation:none}.pr-ink-title{--ink-progress:100%!important}}
</style>'''
html=html.replace('</head>',final_css+'</head>')

# Remove all old generated vine zones.
html=re.sub(r'\s*<div class="pr-vine-zone".*?</div>\s*','\n',html,flags=re.S)
# Insert exactly one pair-of-pairs in every gap between the 7 sections, never after the last.
sec_pat=re.compile(r'<section\b[^>]*>.*?</section>',re.S|re.I)
secs=list(sec_pat.finditer(html))
# Build from end to preserve offsets.
pairs=[('vine-new-04.png','vine-new-07.png'),('vine-new-06.png','vine-new-04.png'),('vine-new-07.png','vine-new-06.png'),('vine-new-05.png','vine-new-07.png'),('vine-new-04.png','vine-new-06.png'),('vine-new-07.png','vine-new-05.png')]
for i in range(len(secs)-2,-1,-1):
    a,b=pairs[i]
    zone=f'''\n<div class="pr-vine-zone" aria-hidden="true" data-vine-zone>\n<img class="pr-vine left" src="{a}" alt="">\n<img class="pr-vine right" src="{b}" alt="">\n<img class="pr-vine left second" src="{b}" alt="">\n<img class="pr-vine right second" src="{a}" alt="">\n</div>\n'''
    pos=secs[i].end()
    html=html[:pos]+zone+html[pos:]

# Replace all scripts after the first functional base with one clean functional controller.
script_pat=re.compile(r'<script(?:\s+id="([^"]+)")?[^>]*>.*?</script>',re.S|re.I)
scripts=list(script_pat.finditer(html))
# Keep none of the old scripts; insert clean one before </body>.
for m in reversed(scripts):
    html=html[:m.start()]+html[m.end():]
functional=r'''<script id="PR-FUNCTIONAL">
(()=>{
 const progress=document.querySelector('.scroll-progress span');
 const filters=[...document.querySelectorAll('.filter')], cards=[...document.querySelectorAll('.gallery .card')];
 const lb=document.getElementById('lightbox'), lbImg=document.getElementById('lightboxImg'), lbCap=document.getElementById('lightboxCaption');
 filters.forEach(btn=>btn.addEventListener('click',()=>{filters.forEach(b=>b.classList.remove('active'));btn.classList.add('active');const f=btn.dataset.filter;cards.forEach(c=>c.dataset.hidden=(f!=='all'&&c.dataset.artist!==f)?'true':'false')}));
 cards.forEach(card=>card.addEventListener('click',()=>{const img=card.querySelector('img');if(!img||!lb)return;lbImg.src=img.currentSrc||img.src;lbImg.alt=img.alt||'';lbCap.textContent=card.dataset.caption||'';lb.classList.add('open');document.body.style.overflow='hidden'}));
 const close=()=>{lb?.classList.remove('open');document.body.style.overflow=''};document.querySelector('.close')?.addEventListener('click',close);lb?.addEventListener('click',e=>{if(e.target===lb)close()});document.addEventListener('keydown',e=>{if(e.key==='Escape')close()});
 document.getElementById('bookingForm')?.addEventListener('submit',e=>{e.preventDefault();const d=new FormData(e.currentTarget);const subject=encodeURIComponent('Demande de rendez-vous — Purple Roses Tattoo');const body=encodeURIComponent(`Nom / prénom : ${d.get('name')}\nE-mail : ${d.get('email')}\nTéléphone : ${d.get('phone')}\nType de projet : ${d.get('type')}\nArtiste : ${d.get('artist')}\n\nProjet :\n${d.get('message')}`);location.href=`mailto:purplerosestattoo@outlook.fr?subject=${subject}&body=${body}`});
 const clamp=(v,a=0,b=1)=>Math.max(a,Math.min(b,v)),ease=t=>t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2;
 const zones=[...document.querySelectorAll('.pr-vine-zone')], artists=[...document.querySelectorAll('.artist')], gallery=[...document.querySelectorAll('#flashs .gallery .card,#realisations .gallery .card')], titles=[...document.querySelectorAll('.section-head h2,.story h2,.flash-note h3,.studio-label h3,.booking h2')];
 titles.forEach(t=>t.classList.add('pr-ink-title'));
 let raf=0;
 function render(){
  raf=0;const vh=innerHeight||1;
  if(progress){const max=document.documentElement.scrollHeight-vh;progress.style.transform=`scaleX(${max>0?scrollY/max:0})`}
  zones.forEach(z=>{const r=z.getBoundingClientRect();const p=clamp((vh*.80-r.top)/(vh*.50));const e=ease(p);z.querySelectorAll('.pr-vine').forEach((v,vi)=>{const right=v.classList.contains('right'),travel=(1-e)*112,y=(vi%2?1:-1)*(1-e)*6,rot=(right?1:-1)*(1-e)*2;v.style.opacity=(.98*e).toFixed(3);v.style.transform=right?`translate3d(${travel}%,${y}px,0) scaleX(-1) rotate(${rot}deg)`:`translate3d(${-travel}%,${y}px,0) rotate(${rot}deg)`;v.style.filter=`drop-shadow(0 0 ${6+7*e}px rgba(73,103,220,${.14+.18*e}))`})});
  artists.forEach((c,i)=>{const r=c.getBoundingClientRect(),p=clamp((vh*.90-r.top)/(vh*.64)),e=ease(p),dir=i===0?-1:1;c.style.opacity=(.20+.80*e).toFixed(3);c.style.filter=`blur(${(1-e)*.8}px)`;c.style.transform=`translate3d(${(1-e)*dir*72}px,${(1-e)*28}px,0) rotate(${(1-e)*dir*1.8}deg)`;const photo=c.querySelector('.artist-photo');if(photo)photo.style.transform=`scale(${1.055-.055*e}) translate3d(${(1-e)*-12*dir}px,0,0)`});
  gallery.forEach((c,i)=>{const r=c.getBoundingClientRect(),p=clamp((vh*.95-r.top)/(vh*.78)),e=ease(p),dir=i%2?-1:1;c.style.transform=`translate3d(${dir*(1-e)*7}px,${(1-e)*7}px,0)`});
  titles.forEach(t=>{const r=t.getBoundingClientRect(),p=clamp((vh*.88-r.top)/(vh*.58)),e=ease(p);t.style.setProperty('--ink-progress',`${(e*100).toFixed(2)}%`)});
 }
 function req(){if(!raf)raf=requestAnimationFrame(render)} addEventListener('scroll',req,{passive:true});addEventListener('resize',req,{passive:true});render();
})();
</script>'''
html=html.replace('</body>',functional+'</body>')
path.write_text(html,encoding='utf-8')

# Validate
h=html
report={
 'sections':len(re.findall(r'<section\b',h,re.I)),
 'zones_between_sections':len(re.findall(r'class="pr-vine-zone"',h)),
 'vine_png_refs':len(re.findall(r'class="pr-vine (?:left|right)',h)),
 'old_scripts':sorted(re.findall(r'<script id="([^"]+)"',h)),
 'hero_grid_2col':bool(re.search(r'\.hero-grid[^}]*grid-template-columns',h)),
 'ink_titles_selector':len(re.findall(r'\.section-head h2,\.story h2,\.flash-note h3,\.studio-label h3,\.booking h2',h)),
 'gallery_opacity_zero':bool(re.search(r'\.gallery \.card\{[^}]*opacity:0',h)),
 'missing_refs':[]
}
for ref in re.findall(r'(?:src|href)="([^"#?]+)"',h,re.I):
 if ref.startswith(('http://','https://','mailto:','tel:','data:','javascript:','//','/')):continue
 if not (root/ref).exists():report['missing_refs'].append(ref)
report['missing_refs']=sorted(set(report['missing_refs']))
print(json.dumps(report,ensure_ascii=False,indent=2))
out=Path('/mnt/data/purple_roses_tattoo_FINAL_2026_VERIFIED.zip')
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
 for p in root.rglob('*'):
  if p.is_file() and p.name not in {'original.html','rebuild.py'}:z.write(p,p.relative_to(root))
print(out)
